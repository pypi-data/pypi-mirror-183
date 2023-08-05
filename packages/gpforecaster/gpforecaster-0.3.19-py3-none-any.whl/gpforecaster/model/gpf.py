from datetime import timedelta
import os
import time
from pathlib import Path
import psutil
from typing import Dict, Union, Tuple, Optional
import random

import numpy as np
import torch
import gpytorch
import pickle
import matplotlib.pyplot as plt
from gpytorch.mlls import SumMarginalLogLikelihood
from gpytorch.likelihoods import GaussianLikelihood
from gpytorch.models import IndependentModelList
from gpytorch.likelihoods import LikelihoodList
from sklearn.preprocessing import StandardScaler

from gpforecaster import __version__
from gpforecaster.utils.logger import Logger
from gpforecaster.model.gp import ExactGPModel, SparseGPModel
from gpforecaster.model.mean_functions import PiecewiseLinearMean
from gpforecaster.results.calculate_metrics import CalculateResultsBottomUp


class GPF:
    """
    A class for training and forecasting hierarchical time series datasets with Gaussian Process models.

    Parameters:
        dataset: Name of the dataset.
        groups: Dictionary containing the train and predict groups.
        input_dir: Directory where input files are stored
        n_samples: Number of samples to draw from the posterior distribution
        store_prediction_samples: Whether to store the prediction samples
        store_prediction_points: Whether to store the prediction points.
        log_dir: Directory where log files are stored. Default is '.'.
        inducing_points_perc: Percentage of inducing points to use.
        gp_type: Type of GP: exact, sparse, etc

    Attributes:
        dataset (str): Name of the dataset.
        groups (dict): Dictionary containing the train and predict groups.
        input_dir (str): Directory where input files are stored.
        timer_start (float): Start time of the training process.
        wall_time_train (float): Wall time for training.
        wall_time_predict (float): Wall time for prediction.
        wall_time_total (float): Total wall time.
        n_samples (int): Number of samples to draw from the posterior distribution.
        store_prediction_samples (bool): Whether to store the prediction samples.
        store_prediction_points (bool): Whether to store the prediction points.
        train_x (torch.Tensor): Tensor with the training data input.
        train_y (torch.Tensor): Tensor with the training data output.
        test_x (torch.Tensor): Tensor with the test data input.
        test_y (torch.Tensor): Tensor with the test data output.
        original_data (np.ndarray): Orignal dataset
        original_data_transformed (np.ndarray): Orignal dataset transformed
        n_train (int): Number of training samples
        n_test (int): Number of testing samples
        s (int): Number of time series
        losses (list): List of losses during training.
        val_losses (list): List of validation losses during training.
        model_version (str): Version of the model.
        logger_train (Logger): Logger for the training process.
        logger_metrics (Logger): Logger for the metrics.
    """

    def __init__(
        self,
        dataset: str,
        groups: dict,
        input_dir: str = "./",
        n_samples: int = 500,
        store_prediction_samples: bool = False,
        store_prediction_points: bool = False,
        log_dir: str = ".",
        inducing_points_perc: float = 0.5,
        gp_type: str = "exact",
    ):
        self.dataset = dataset
        self.groups = groups
        self.input_dir = input_dir
        self.timer_start = time.time()
        self.wall_time_train = None
        self.wall_time_predict = None
        self.wall_time_total = None
        self.original_data = groups["predict"]["data_matrix"]

        self.groups, self.scaler = self._preprocess(self.groups)
        self._create_directories()
        self.n_samples = n_samples
        self.store_prediction_samples = store_prediction_samples
        self.store_prediction_points = store_prediction_points

        self.train_x = torch.arange(groups["train"]["n"])
        self.train_x = self.train_x.type(torch.DoubleTensor)
        self.train_x = self.train_x.unsqueeze(-1)
        self.train_y = torch.from_numpy(groups["train"]["data"])

        self.test_x = torch.arange(groups["train"]["n"], groups["predict"]["n"])
        self.test_x = self.test_x.type(torch.DoubleTensor)
        self.test_x = self.test_x.unsqueeze(-1)
        self.test_y = torch.from_numpy(
            groups["predict"]["data_matrix"][groups["train"]["n"] :]
        )

        self.original_data_transformed = groups["predict"]["data_matrix"]

        self.n_train = groups["train"]["n"]
        self.n_predict = groups["predict"]["n"]
        self.s = groups["train"]["s"]

        self.gp_type = gp_type
        #self.inducing_points = torch.linspace(
        #    0,
        #    self.n_train,
        #    int(perc_inducing_points * self.n_train),
        #    dtype=torch.double
        #)
        self.inducing_points = torch.rand(
            int(inducing_points_perc * self.n_train),
            dtype=torch.double
        ) * self.n_train
        self.losses = []
        self.val_losses = []
        self.mll = None

        self.model_version = __version__

        self.logger_train = Logger(
            "train", dataset=self.dataset, to_file=True, log_dir=log_dir
        )
        self.logger_metrics = Logger(
            "metrics", dataset=self.dataset, to_file=True, log_dir=log_dir
        )

    def _create_directories(self):
        # Create directory to store results if does not exist
        Path(f"{self.input_dir}results").mkdir(parents=True, exist_ok=True)

    def _preprocess(self, groups):
        scaler = StandardScaler()
        scaler.fit(self.groups["train"]["data"])
        groups["train"]["data"] = scaler.transform(groups["train"]["data"])
        groups["predict"]["data_matrix"] = scaler.transform(
            groups["predict"]["data_matrix"]
        )

        return groups, scaler

    def _build_mixtures(self):
        """
        Build the mixtures matrix.

        Returns:
            known_mixtures (np.ndarray): The mixtures matrix.
            n_groups (int): number of groups.

        Example:
                Group1     |   Group2
            GP1, GP2, GP3  | GP1, GP2
            0  , 1  , 1    | 0  , 1
            1  , 0  , 0    | 1  , 0
            0  , 1, , 1    | 0  , 1
            1  , 0  , 1    | 1  , 0
        """
        idxs = []
        for k, val in self.groups["train"]["groups_idx"].items():
            idxs.append(val)

        idxs_t = np.array(idxs).T

        n_groups = np.sum(
            np.fromiter(self.groups["train"]["groups_n"].values(), dtype="int32")
        )
        known_mixtures = np.zeros((self.groups["train"]["s"], n_groups))
        k = 0
        for j in range(self.groups["train"]["g_number"]):
            for i in range(np.max(idxs_t[:, j]) + 1):
                idx_to_1 = np.where(idxs_t[:, j] == i)
                known_mixtures[:, k][idx_to_1] = 1
                k += 1

        top_level = np.ones((known_mixtures.shape[0], 1))
        known_mixtures = np.concatenate((known_mixtures, top_level), axis=1)
        n_groups += 1

        return known_mixtures, n_groups

    def _build_cov_matrices(self):
        """
        Build the covariance matrices.

        Parameters:
            mixtures (np.ndarray): The mixtures matrix.

        Returns:
            covs (list): List of covariance functions.
            known_mixtures (np.ndarray): The mixtures matrix.
            n_groups (int): number of groups.
        """
        known_mixtures, n_groups = self._build_mixtures()
        covs = []
        for i in range(1, n_groups + 1):
            # RBF kernel
            rbf_kernel = gpytorch.kernels.RBFKernel()
            rbf_kernel.lengthscale = torch.tensor([1.0])
            scale_rbf_kernel = gpytorch.kernels.ScaleKernel(rbf_kernel)
            scale_rbf_kernel.outputscale = torch.tensor([0.5])

            # Periodic Kernel
            periodic_kernel = gpytorch.kernels.PeriodicKernel()
            periodic_kernel.period_length = torch.tensor([self.groups["seasonality"]])
            periodic_kernel.lengthscale = torch.tensor([0.5])
            scale_periodic_kernel = gpytorch.kernels.ScaleKernel(periodic_kernel)
            scale_periodic_kernel.outputscale = torch.tensor([1.5])

            # Cov Matrix
            cov = scale_rbf_kernel + scale_periodic_kernel
            covs.append(cov)

        return covs, known_mixtures, n_groups

    def _apply_mixture_cov_matrices(self):
        """
        Apply the mixture covariance matrices and create the final list of covariance functions.

        Returns:
            mixed_covs (cov): The list of mixture covariance functions.
        """
        covs, known_mixtures, n_groups = self._build_cov_matrices()

        # apply mixtures to covariances
        selected_covs = []
        mixed_covs = []
        for i in range(self.groups["train"]["s"]):
            mixture_weights = known_mixtures[i]
            for w_ix in range(n_groups):
                w = mixture_weights[w_ix]
                if w == 1.0:
                    selected_covs.append(covs[w_ix])
            mixed_cov = selected_covs[0]
            for cov in range(1, len(selected_covs)):
                mixed_cov += selected_covs[
                    cov
                ]  # because GP(cov1 + cov2) = GP(cov1) + GP(cov2)
            mixed_covs.append(mixed_cov)
            selected_covs = []  # clear out cov list

        return mixed_covs

    def _build_model(
        self, x: torch.Tensor, y: torch.Tensor
    ) -> Tuple[list[GaussianLikelihood], list[ExactGPModel]]:
        """
        Build the model.

        Parameters:
            x: Measures
            y: Observations.

        Returns:
            likelihood_list: List of GP models.
            model_list: List of likelihoods.
        """
        mixed_covs = self._apply_mixture_cov_matrices()
        n_changepoints = 4
        changepoints = np.linspace(0, self.groups["train"]["n"], n_changepoints + 2)[
            1:-1
        ]

        model_list = []
        likelihood_list = []
        for i in range(self.groups["train"]["s"]):
            likelihood_list.append(GaussianLikelihood())
            if self.gp_type == "exact":
                model_list.append(
                    ExactGPModel(
                        train_x=x,
                        train_y=y[:, i],
                        likelihood=likelihood_list[i],
                        cov=mixed_covs[i],
                        changepoints=changepoints,
                        mean_func=PiecewiseLinearMean,
                    )
                )
            elif self.gp_type == "sparse":
                model_list.append(
                    SparseGPModel(
                        train_x=x,
                        train_y=y[:, i],
                        likelihood=likelihood_list[i],
                        cov=mixed_covs[i],
                        changepoints=changepoints,
                        mean_func=PiecewiseLinearMean,
                        inducing_points=self.inducing_points,
                    )
                )

        return likelihood_list, model_list

    def early_stopping(self, patience: int):
        losses = [x for x in self.val_losses if x is not None]
        losses.reverse()
        non_decreasing = 0
        for x, y in zip(losses, losses[1:]):
            if np.round(x, 2) >= np.round(y, 2):
                non_decreasing += 1
            else:
                break

        if non_decreasing > patience:
            return True
        else:
            return False

    @staticmethod
    def _create_scheduler(
        scheduler_type: str, optimizer: torch.optim.Optimizer, epochs: int, gamma: float
    ) -> Optional[torch.optim.lr_scheduler._LRScheduler]:
        """
        Creates a scheduler for the learning rate of an optimizer.

        Parameters
            scheduler_type: The type of scheduler to use. One of 'step', 'exponential', 'cosine', or 'none'.
            optimizer: The optimizer for which to create the scheduler.
            epochs: The number of epochs to train the model.

        Returns
            Optional
                The created scheduler, or None if `scheduler_type` is 'none'.
        """
        if scheduler_type == "step":
            scheduler = torch.optim.lr_scheduler.StepLR(
                optimizer, step_size=10, gamma=gamma
            )
        elif scheduler_type == "exponential":
            scheduler = torch.optim.lr_scheduler.ExponentialLR(optimizer, gamma=gamma)
        elif scheduler_type == "cosine":
            scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
                optimizer, T_max=epochs
            )
        else:
            scheduler = None
        return scheduler

    def train(
        self,
        lr: float = 1e-2,
        epochs: int = 500,
        early_stopping: bool = True,
        patience: int = 4,
        weight_decay: float = 1e-4,
        verbose: bool = True,
        track_mem: bool = False,
        scheduler_type: str = "cosine",
        gamma_rate: float = 0.95,
    ) -> Tuple[IndependentModelList, LikelihoodList]:
        """
        Train the model.

        Parameters:
            lr: Learning rate.
            epochs: Number of epochs
            early_stopping: Perform early stopping
            patience: Parameter to early stopping
            weight_decay: Weight decay
            verbose: Print outputs when training
            track_mem: Track and log RAM usage
            scheduler_type: Type of scheduler to use to update the learning rate
            gamma_rate: Gamma rate for the scheduler types

        Returns:
            tuple: Tuple containing the trained model and the likelihood.
        """
        i = 0
        loss = None
        val_loss = None

        likelihood_list, model_list = self._build_model(x=self.train_x, y=self.train_y)

        model = IndependentModelList(*model_list)
        likelihood = LikelihoodList(*likelihood_list)

        self.mll = SumMarginalLogLikelihood(likelihood, model)

        model.train()
        likelihood.train()

        optimizer = torch.optim.Adam(
            model.parameters(), lr=lr, weight_decay=weight_decay
        )  # Includes GaussianLikelihood parameters
        scheduler = self._create_scheduler(
            scheduler_type, optimizer, epochs, gamma_rate
        )

        for i in range(epochs):
            optimizer.zero_grad()
            output = model(*model.train_inputs)
            loss = -self.mll(output, model.train_targets)
            self.losses.append(loss.item())

            if early_stopping:
                if i % 5 == 0:
                    model.eval()
                    likelihood.eval()
                    val_loss = self.validate(model)
                    if self.early_stopping(patience=patience):
                        break
                    if verbose:
                        print(
                            f"Iter {i}/{epochs} - Loss: {np.round(loss.item(), 3)}, Validation Loss: {np.round(val_loss, 3)}"
                        )
                    # switch to train mode
                    model.train()
                    likelihood.train()
                else:
                    self.val_losses.append(None)
            else:
                if verbose:
                    print(f"Iter {i}/{epochs} - Loss: {np.round(loss.item(), 3)}")

            loss.backward()
            optimizer.step()
            # Step the scheduler
            if scheduler:
                scheduler.step()

            if i % 30 == 0 and track_mem:
                # Track RAM usage
                process = psutil.Process(os.getpid())
                mem = process.memory_info().rss / (1024**3)
                self.logger_train.info(f"train used {mem:.3f} GB of RAM")

        self.wall_time_train = time.time() - self.timer_start
        td = timedelta(seconds=int(time.time() - self.timer_start))
        self.logger_train.info(f"Num epochs {i}")
        self.logger_train.info(f"wall time train {str(td)}")

        self.logger_train.info(f"Loss {np.round(loss.item(), 2)}")
        if early_stopping:
            self.logger_train.info(f"Val Loss {np.round(val_loss, 2)}")

        return model, likelihood

    def validate(self, model: IndependentModelList) -> float:
        """
        Validate the model.

        Parameters:
            model (ExactGPModel): The GP model.
            mll ():

        Returns:
            float: The negative log likelihood of the model on the validation set.
        """
        with torch.no_grad(), gpytorch.settings.fast_pred_var():
            likelihood_list_val, model_list_val = self._build_model(
                x=self.test_x, y=self.test_y
            )
            model_val = gpytorch.models.IndependentModelList(*model_list_val)
            val_output = model(*model_val.train_inputs)
            val_loss = -self.mll(val_output, model_val.train_targets)
            self.val_losses.append(float(val_loss.item()))
        return val_loss.item()

    def plot_losses(self, start_idx: int = 5):
        n_iterations = np.arange(len(self.losses[start_idx:]))
        plt.plot(n_iterations, self.losses[start_idx:])
        plt.plot(n_iterations, self.val_losses[start_idx:], marker="*")
        timestamp = time.strftime("%Y%m%d-%H%M%S", time.gmtime())
        plt.savefig(
            f"./plots/gpf_loss_{self.dataset}_{timestamp}.pdf",
            format="pdf",
            bbox_inches="tight",
        )
        plt.show()

    def predict(
        self,
        model: IndependentModelList,
        likelihood: LikelihoodList,
        clip: bool = True,
    ) -> np.ndarray:
        """
        Make predictions with the model.

        Parameters:
            model: The GP model.
            likelihood: The likelihood function.
            clip: Whether to clip negative predictions to zero. Default is True.

        Returns:
            numpy.ndarray: Array of shape (n_samples, n_prediction_points, n_groups)
                containing the prediction samples.
        """
        timer_start = time.time()

        model.eval()
        likelihood.eval()

        with torch.no_grad(), gpytorch.settings.fast_pred_var():
            test_x = torch.arange(self.groups["predict"]["n"]).type(torch.DoubleTensor)
            predictions = likelihood(
                *model(*[test_x for i in range(self.groups["predict"]["s"])])
            )

        i = 0
        samples = np.zeros(
            (self.n_samples, self.groups["predict"]["n"], self.groups["predict"]["s"])
        )
        for pred in predictions:
            samples[:, :, i] = np.random.normal(
                pred.mean.detach().numpy(),
                np.sqrt(pred.variance.detach().numpy()),
                size=(self.n_samples, self.groups["predict"]["n"]),
            )
            i += 1

        samples = np.transpose(samples, (1, 2, 0))

        # transform back the data
        samples = (
            samples * np.sqrt(self.scaler.var_)[np.newaxis, :, np.newaxis]
        ) + self.scaler.mean_[np.newaxis, :, np.newaxis]
        self.groups["train"]["data"] = self.scaler.inverse_transform(
            self.groups["train"]["data"]
        )
        self.groups["predict"]["data_matrix"] = self.scaler.inverse_transform(
            self.groups["predict"]["data_matrix"]
        )

        # Clip predictions to 0 if there are negative numbers
        if clip:
            samples[samples < 0] = 0

        self.wall_time_predict = time.time() - timer_start
        return samples

    def store_metrics(self, res):
        with open(
            f"{self.input_dir}results/results_gp_cov_{self.dataset}_{self.model_version}.pickle",
            "wb",
        ) as handle:
            pickle.dump(res, handle, pickle.HIGHEST_PROTOCOL)

    def metrics(
        self, samples: np.ndarray
    ) -> Dict[str, Dict[str, Union[float, np.ndarray]]]:
        """
        Calculate evaluation metrics for the predictions.

        Parameters:
            samples: Array of shape (n_samples, n_prediction_points, n_groups)
                containing the prediction samples.

        Returns:
            dict: Dictionary with the evaluation metrics. The keys are the metric names,
                and the values are dictionaries with the results for each group.
        """
        calc_results = CalculateResultsBottomUp(
            samples,
            self.groups,
            self.store_prediction_samples,
            self.store_prediction_points,
        )
        res = calc_results.calculate_metrics()
        for metric, results in res.items():
            for group, result in results.items():
                if "ind" not in group:
                    self.logger_metrics.info(
                        f"{metric} for {group}: {np.round(result, 2)}"
                    )

        self.wall_time_total = time.time() - self.timer_start

        res["wall_time"] = {}
        res["wall_time"]["wall_time_train"] = self.wall_time_train
        res["wall_time"]["wall_time_predict"] = self.wall_time_predict
        res["wall_time"]["wall_time_total"] = self.wall_time_total

        return res

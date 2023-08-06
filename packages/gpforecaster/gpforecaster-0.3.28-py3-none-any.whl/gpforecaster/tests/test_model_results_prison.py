import pickle
import shutil
import unittest

import numpy as np
from numpy.testing import assert_array_almost_equal
import tsaugmentation as tsag

from gpforecaster.model.gpf import GPF


class TestModel(unittest.TestCase):
    def setUp(self):
        self.data = tsag.preprocessing.PreprocessDatasets("prison").apply_preprocess()
        self.n = self.data["predict"]["n"]
        self.s = self.data["train"]["s"]
        shutil.rmtree("./data/original_datasets")
        self.gpf = GPF("prison", self.data)

    def test_correct_train(self):
        model, like = self.gpf.train(epochs=10)
        self.assertIsNotNone(model)

    def test_predict_shape(self):
        model, like = self.gpf.train(epochs=10)
        samples = self.gpf.predict(model, like)
        self.assertTrue(samples.shape == (self.n, self.s, 500))

    def test_results_interval(self):
        model, like = self.gpf.train(epochs=100)
        samples = self.gpf.predict(model, like)
        res = self.gpf.metrics(samples)
        self.assertLess(res["mase"]["bottom"], 2.5)

    def test_wall_time(self):
        model, like = self.gpf.train(epochs=10)
        samples = self.gpf.predict(model, like)
        res = self.gpf.metrics(samples)
        self.assertLess(res["wall_time"]["wall_time_total"], 100)

    def test_output_results(self):
        model, like = self.gpf.train(epochs=10)
        samples = self.gpf.predict(model, like)
        res = self.gpf.metrics(samples)
        self.gpf.store_metrics(res)
        with open(
            f"{self.gpf.input_dir}results/results_gp_cov_{self.gpf.dataset}_{self.gpf.model_version}.pickle",
            "rb",
        ) as handle:
            output_res = pickle.load(file=handle)
        self.assertIsNotNone(output_res["mase"]["bottom"])

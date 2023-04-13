import unittest
import os
import pandas as pd
import tensorflow as tf
from src import model_training

# This test suite includes four test methods:
# test_preprocess_data: Tests that the preprocess_data function returns the expected shapes for train_data, train_labels, test_data, and test_labels.
# test_build_model: Tests that the build_model function returns a Keras Sequential model with the expected architecture.
# test_train_model: Tests that the train_model function returns a trained model with reasonable performance.
# test_save_model: Tests that the save_model function saves the model in the expected format and location.


class TestModelTraining(unittest.TestCase):

    def setUp(self):
        self.social_media_data = pd.read_csv('data/raw_data/social_media_data.csv')
        self.news_articles_data = pd.read_csv('data/raw_data/news_articles_data.csv')
        self.company_websites_data = pd.read_csv('data/raw_data/company_websites_data.csv')
        self.train_data, self.train_labels, self.test_data, self.test_labels = model_training.preprocess_data(self.social_media_data, self.news_articles_data, self.company_websites_data)
        self.model = model_training.build_model()
        self.model.compile(loss='mse', optimizer='adam', metrics=['mae'])

    def tearDown(self):
        tf.keras.backend.clear_session()
        os.remove('data/models/machine_learning_model')

    def test_preprocess_data(self):
        # Test that preprocess_data function returns the expected shapes for train_data, train_labels, test_data, and test_labels
        self.assertEqual(self.train_data.shape, (80, 3))
        self.assertEqual(self.train_labels.shape, (80, 1))
        self.assertEqual(self.test_data.shape, (20, 3))
        self.assertEqual(self.test_labels.shape, (20, 1))

    def test_build_model(self):
        # Test that build_model function returns a Keras Sequential model with the expected architecture
        self.assertIsInstance(self.model, tf.keras.Sequential)
        self.assertEqual(len(self.model.layers), 3)
        self.assertIsInstance(self.model.layers[0], tf.keras.layers.Dense)
        self.assertEqual(self.model.layers[0].units, 64)
        self.assertEqual(self.model.layers[0].activation, 'relu')
        self.assertIsInstance(self.model.layers[1], tf.keras.layers.Dense)
        self.assertEqual(self.model.layers[1].units, 64)
        self.assertEqual(self.model.layers[1].activation, 'relu')
        self.assertIsInstance(self.model.layers[2], tf.keras.layers.Dense)
        self.assertEqual(self.model.layers[2].units, 1)

    def test_train_model(self):
        # Test that train_model function returns a trained model with reasonable performance
        trained_model = model_training.train_model(self.model, self.train_data, self.train_labels, self.test_data, self.test_labels)
        self.assertIsNotNone(trained_model)
        evaluation = trained_model.evaluate(self.test_data, self.test_labels)
        self.assertLess(evaluation[0], 0.1)
        self.assertLess(evaluation[1], 0.3)

    def test_save_model(self):
        # Test that save_model function saves the model in the expected format and location
        trained_model = model_training.train_model(self.model, self.train_data, self.train_labels, self.test_data, self.test_labels)
        model_training.save_model(trained_model, 'data/models/machine_learning_model')
        self.assertTrue(os.path.exists('data/models/machine_learning_model'))

if __name__ == '__main__':
    unittest.main()

import unittest
import pandas as pd
from app.src.app_ideas_generation import AppIdeasGenerator

# This implementation includes three test cases:
# test_preprocess_data: tests that the preprocess_data function returns a non-empty output when given a list of sample text data.
# test_generate_app_ideas: tests that the generate_app_ideas function returns a non-empty output when given a valid investor ID.
# test_rank_app_ideas: tests that the rank_app_ideas function returns a non-empty output when given a DataFrame of app ideas, an
# investor background, and investor interests.


class TestAppIdeasGeneration(unittest.TestCase):
    def setUp(self):
        self.app_ideas_generator = AppIdeasGenerator()

    def test_preprocess_data(self):
        # Test that the preprocess_data function returns a non-empty output
        text_data = ["This is a test sentence", "Another sentence"]
        processed_data = self.app_ideas_generator.preprocess_data(text_data)
        self.assertIsNotNone(processed_data)
        self.assertNotEqual(len(processed_data), 0)

    def test_generate_app_ideas(self):
        # Test that the generate_app_ideas function returns a non-empty output
        investor_id = 1 # Assuming that there's an investor with ID 1 in the investor_data
        app_ideas = self.app_ideas_generator.generate_app_ideas(investor_id)
        self.assertIsNotNone(app_ideas)
        self.assertNotEqual(len(app_ideas), 0)

    def test_rank_app_ideas(self):
        # Test that the rank_app_ideas function returns a non-empty output
        app_ideas = pd.DataFrame({'app_idea': ['idea 1', 'idea 2', 'idea 3']})
        investor_background = 'technology'
        investor_interests = 'health'
        ranked_app_ideas = self.app_ideas_generator.rank_app_ideas(app_ideas, investor_background, investor_interests)
        self.assertIsNotNone(ranked_app_ideas)
        self.assertNotEqual(len(ranked_app_ideas), 0)

if __name__ == '__main__':
    unittest.main()

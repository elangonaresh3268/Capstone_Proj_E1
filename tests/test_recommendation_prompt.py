import unittest

from recommendation import build_recommendation_prompt


class RecommendationPromptTests(unittest.TestCase):
    def test_build_recommendation_prompt_highlights_respiratory_condition(self):
        profile = {
            "name": "John",
            "age": 45,
            "gender": "Male",
            "occupation": "Engineer",
            "income": 1200000,
            "marital_status": "Married",
            "medical_history": "Severe respiratory disease",
            "existing_policy": "No policy",
        }

        prompt = build_recommendation_prompt(profile, "sample document")

        self.assertIn("severe respiratory disease", prompt.lower())
        self.assertIn("oxygen", prompt.lower())
        self.assertIn("icu", prompt.lower())
        self.assertIn("hospitalization", prompt.lower())

    def test_build_recommendation_prompt_highlights_heart_disease(self):
        profile = {
            "name": "John",
            "age": 45,
            "gender": "Male",
            "occupation": "Engineer",
            "income": 1200000,
            "marital_status": "Married",
            "medical_history": "Mild heart disease",
            "existing_policy": "No policy",
        }

        prompt = build_recommendation_prompt(profile, "sample document")

        self.assertIn("heart-related disease", prompt.lower())
        self.assertIn("cardiac", prompt.lower())
        self.assertIn("hospitalization", prompt.lower())


if __name__ == "__main__":
    unittest.main()

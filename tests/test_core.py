# tests/test_core.py

import unittest
from cyberprompt.core import CyberPromptCore

class TestCyberPromptCore(unittest.TestCase):
    """
    Unit tests for the CyberPromptCore class.
    """

    def setUp(self):
        """
        Set up a new CyberPromptCore instance before each test.
        This method is called automatically by the unittest framework.
        """
        self.core = CyberPromptCore(recursion_depth=2, creativity=0.5)

    def test_initialization(self):
        """
        Test that the CyberPromptCore instance is initialized with the correct
        attributes.
        """
        self.assertEqual(self.core.recursion_depth, 2)
        self.assertEqual(self.core.creativity, 0.5)
        self.assertEqual(self.core.history, [])

    def test_generate_response(self):
        """
        Test the generate_response method to ensure it returns a valid
        response and updates the history.
        """
        prompt = "What is the meaning of life?"
        response = self.core.generate_response(prompt)

        # Test that the response is a string
        self.assertIsInstance(response, str)

        # Test that the response contains the original prompt
        self.assertIn(prompt, response)

        # Test that the response contains the configuration parameters
        self.assertIn("Recursion Depth: 2", response)
        self.assertIn("Creativity: 0.5", response)

    def test_history_tracking(self):
        """
        Test that the interaction history is correctly updated after generating
        a response.
        """
        # Initially, the history should be empty
        self.assertEqual(len(self.core.history), 0)

        prompt1 = "First prompt"
        self.core.generate_response(prompt1)

        # After one response, the history should have one entry
        self.assertEqual(len(self.core.history), 1)
        self.assertEqual(self.core.history[0]['prompt'], prompt1)
        self.assertIn(prompt1, self.core.history[0]['response'])

        prompt2 = "Second prompt"
        self.core.generate_response(prompt2)

        # After a second response, the history should have two entries
        self.assertEqual(len(self.core.history), 2)
        self.assertEqual(self.core.history[1]['prompt'], prompt2)
        self.assertIn(prompt2, self.core.history[1]['response'])


if __name__ == '__main__':
    unittest.main()

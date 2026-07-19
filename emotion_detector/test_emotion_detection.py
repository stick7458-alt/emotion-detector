"""
test_emotion_detection.py

Unit tests for the emotion_detector function. Each test sends a
sample statement expected to trigger a specific dominant emotion,
and asserts that the function returns the correct dominant_emotion.
"""

import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetection(unittest.TestCase):
    """Test suite validating dominant_emotion output for each emotion."""

    def test_emotion_detector(self):
        """Verify emotion_detector returns the expected dominant emotion."""
        result_joy = emotion_detector("I am glad this happened")
        self.assertEqual(result_joy["dominant_emotion"], "joy")

        result_anger = emotion_detector("I am really mad about this")
        self.assertEqual(result_anger["dominant_emotion"], "anger")

        result_disgust = emotion_detector(
            "I feel disgusted just hearing about this"
        )
        self.assertEqual(result_disgust["dominant_emotion"], "disgust")

        result_sadness = emotion_detector("I am so sad about this")
        self.assertEqual(result_sadness["dominant_emotion"], "sadness")

        result_fear = emotion_detector(
            "I am really afraid that this will happen"
        )
        self.assertEqual(result_fear["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()

"""Unit tests for the emotion_detector function."""
import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for emotion_detector."""

    def test_emotion_detector(self):
        """Check the dominant emotion returned for sample statements."""
        cases = {
            'I am glad this happened': 'joy',
            'I am really mad about this': 'anger',
            'I feel disgusted just hearing about this': 'disgust',
            'I am so sad about this': 'sadness',
            'I am really afraid that this will happen': 'fear',
        }
        for statement, expected in cases.items():
            result = emotion_detector(statement)
            self.assertEqual(result['dominant_emotion'], expected)


if __name__ == '__main__':
    unittest.main()

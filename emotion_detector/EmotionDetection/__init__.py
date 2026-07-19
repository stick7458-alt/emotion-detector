"""
EmotionDetection package.

Exposes emotion_detector() so it can be imported as:
    from EmotionDetection import emotion_detector
or
    from EmotionDetection.emotion_detection import emotion_detector
"""

from EmotionDetection.emotion_detection import emotion_detector

__all__ = ["emotion_detector"]

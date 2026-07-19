"""
emotion_detection.py

Contains the core emotion_detector function that sends text to the
Watson NLP embeddable AI 'emotion_aggregated-workflow_lang_en_stock'
model and returns a dictionary of emotion scores plus the dominant
emotion.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Sends text_to_analyze to the Watson NLP emotion prediction service
    and returns a dictionary with anger, disgust, fear, joy, sadness
    scores, and the dominant_emotion.

    If the input text is blank/invalid (server returns HTTP 400),
    every value in the returned dictionary is set to None.
    """
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/"
        "watson.nlp.insights.emotion"
    )
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    input_json = {"raw_document": {"text": text_to_analyze}}

    response = requests.post(url, json=input_json, headers=headers, timeout=10)

    # Task 7: handle blank / invalid input gracefully (status code 400)
    if response.status_code == 400:
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    formatted_response = json.loads(response.text)
    emotion_predictions = formatted_response["emotionPredictions"][0]["emotion"]

    anger = emotion_predictions["anger"]
    disgust = emotion_predictions["disgust"]
    fear = emotion_predictions["fear"]
    joy = emotion_predictions["joy"]
    sadness = emotion_predictions["sadness"]

    # Task 3: format the output
    emotion_scores = {
        "anger": anger,
        "disgust": disgust,
        "fear": fear,
        "joy": joy,
        "sadness": sadness,
    }

    dominant_emotion = max(emotion_scores, key=emotion_scores.get)
    emotion_scores["dominant_emotion"] = dominant_emotion

    return emotion_scores

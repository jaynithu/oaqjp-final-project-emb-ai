import requests
import json

def emotion_detector(text_to_analyze):
    # Handle blank input before making API call
    if not text_to_analyze or text_to_analyze.strip() == "":
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
    
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    response = requests.post(url, headers=headers, json=input_json)
    
    # Check if request was successful (status code 200)
    if response.status_code == 200:
        response_data = response.json()
        emotions = response_data['emotionPredictions'][0]['emotion']
        dominant_emotion = max(emotions, key=emotions.get)
        emotions['dominant_emotion'] = dominant_emotion
        return emotions
    
    # If status code is 400 (or any error), return None values
    else:
        return {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
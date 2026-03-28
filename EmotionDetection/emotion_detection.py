import requests
import json

def emotion_detector(text_to_analyze):
    # Step 1: Define the Watson NLP API endpoint
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Step 2: Define the headers
    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }
    
    # Step 3: Create the input JSON payload
    input_json = {
        "raw_document": {
            "text": text_to_analyze
        }
    }
    
    # Step 4: Make the POST request to Watson API
    response = requests.post(url, headers=headers, json=input_json)
    
    response_data = response.json()
    
    # Extract just the emotion scores
    emotions = response_data['emotionPredictions'][0]['emotion']
        # NEW: Find the dominant emotion (the one with highest score)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # NEW: Add dominant_emotion to the dictionary
    emotions['dominant_emotion'] = dominant_emotion
    
    return emotions
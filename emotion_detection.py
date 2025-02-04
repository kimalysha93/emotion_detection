import requests
import json

def emotion_detector(text_to_analyze):

    # Define the URL
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # payload with input json text to be analyzed
    payload = { "raw_document": { "text": text_to_analyze } }

    # set headers with required model id for the API
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Make a POST request to the API with payload and headers
    response = requests.post(url, json=payload, headers=header)

    # Parse the response from the API
    formatted_response = json.loads(response.text)
    
    # retrieving the text attribute from the response object
    text = formatted_response["emotionPredictions"][0]["emotionMentions"][0]["span"]["text"]

    # returning the text attribute from the response object
    return {'text': text}
  

'''
{'emotionPredictions':
    [{
    'emotion': {'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024},
    
    'target': '',

    'emotionMentions': [{'span': {'begin': 0, 'end': 27, 'text': 'I love this new technology.'}, 'emotion': {'anger': 0.01364663, 'disgust': 0.0017160787, 'fear': 0.008986978, 'joy': 0.9719017, 'sadness': 0.055187024}}]
    }],

    'producerId': {'name': 'Ensemble Aggregated Emotion Workflow',
    
    'version': '0.0.1'}}
'''
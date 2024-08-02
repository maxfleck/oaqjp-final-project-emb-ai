import requests  # Import the requests library to handle HTTP requests
import json # Import the json library... for json lol

# Define a function named emotion_detector that takes a string input (text_to_analyse)
def emotion_detector( text_to_analyse ):
    # URL: 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Headers: {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Input json: { "raw_document": { "text": text_to_analyse } }
    
    # URL of the emotion detector service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    # Set the headers required for the API request
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    # Create a dictionary with the text to be analyzed
    myobj = { "raw_document": { "text": text_to_analyse }}
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=headers)
    # check status code
    if response.status_code == 400:
        # set all keys to None
        emotion = {
                "anger": None, 
                "disgust": None, 
                "fear": None, 
                "joy": None, 
                "sadness": None, 
                "dominant_emotion": None
                }
    else:
        # get emotion from response
        emotion = json.loads( response.text )['emotionPredictions'][0]['emotion']
        # get dominant emotion
        emotion["dominant_emotion"] = max(emotion, key = emotion.get )            
    # Return the response text from the API
    return emotion
import requests  # Import the requests library to handle HTTP requests

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
    myobj = { "raw_document": { "text": text_to_analyse } }
    # Send a POST request to the API with the text and headers
    response = requests.post(url, json = myobj, headers=headers)
    # Return the response text from the API
    return response.text
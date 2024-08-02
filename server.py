''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5000.
'''
#pylint: disable=consider-using-f-string
import json
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def sent_analyzer():
    """
    Define a function named sent_analyzer
    """
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the emotion detector function and store the response
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"]:
        return_string = '''For the given statement, the system response is {}. The
         dominant emotion is <b>{}</b>.'''.format(
                                        json.dumps(response)[1:-1],
                                        response["dominant_emotion"] )
    else:
        return_string = "<b>Invalid text! Please try again!</b>"
    # Return the dict
    return return_string

@app.route("/")
def render_index_page():
    """
    Define a function to render the index page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

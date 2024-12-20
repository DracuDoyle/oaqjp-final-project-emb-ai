"""
Flask application for emotion detection using Watson NLP's Emotion Predict API.
"""


from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route('/')
def index():

    """
    Renders the index page.
    """

    return render_template('index.html')


@app.route('/emotionDetector', methods=['GET'])
def detect_emotion():

    """
    Detects emotion from the provided text.

    Retrieves the text input via a GET request, passes it to the
    emotion detection function, and formats the response accordingly.
    """

    text_to_analyze = request.args.get('textToAnalyze', '')
    result = emotion_detector(text_to_analyze)

    if result['dominant_emotion'] is None:

        response = "Invalid text! Please try again!"

    else:

        response = (
            f"For the given statement, the system response is "
            f"'anger': {result['anger']} "
            f"'disgust': {result['disgust']} "
            f"'fear': {result['fear']} "
            f"'joy': {result['joy']} "
            f"'sadness': {result['sadness']} "
            f"The dominant emotion is {result['dominant_emotion']}."
        )

    return response


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)

from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/emotionDetector')
def emotion_detector_route():
    # Get the text from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    
    # Call the emotion_detector function
    result = emotion_detector(text_to_analyze)
    
    # Check if dominant_emotion is None (error case)
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"
    
    # Extract individual emotions
    anger = result['anger']
    disgust = result['disgust']
    fear = result['fear']
    joy = result['joy']
    sadness = result['sadness']
    dominant_emotion = result['dominant_emotion']
    
    # Format the response string
    response_text = (
        f"For the given statement, the system response is 'anger': {anger}, "
        f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy}, 'sadness': {sadness}. "
        f"The dominant emotion is {dominant_emotion}."
    )
    
    return response_text

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

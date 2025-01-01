"""
Twitch AI Overlay using Ollama API and Flask

This script sets up a Flask server to generate AI responses based on user input
and serve an HTML overlay for displaying the AI responses in a Twitch stream.

The overlay uses JavaScript to fetch the latest AI response every 2 seconds
and display it with a typing effect.

To run, execute this script and navigate to `http://localhost:5000/overlay`
in your browser or use it in Streamlabs.

You can also test the AI response generation by sending a POST request
to `http://localhost:5000/query` with a JSON payload containing the user's input:

    {
        "input": "Hello, world!"
    }

The response will be a JSON object containing the AI response:

    {
        "response": "Hello, human!"
    }
"""

import flask
import ollama
import threading
import time
import json

app = flask.Flask(__name__)

MODEL_NAME = "llama3:latest"

# Global variable to hold the most recent AI response
latest_ai_response = "Waiting for AI response..."

# Function to get AI response from Ollama API
def get_ai_response(user_input: str) -> str:
    global latest_ai_response
    try:
        # Generate AI response from the Ollama API
        # You can modify the prompt to get different AI responses or caracteristics
        prompt = f"""
        You are a fun and interactive Twitch AI assistant named Neuraibu. Your owner is named Perrier. He is a french developer and love Java and thing around Minecraft. 
        Your goal is to talk about random things and have a good conversation with viewers. But don't make long responds (like don't make more than 35 words).
        User: {user_input}
        Neuraibu:
        """
        response = ollama.generate(model=MODEL_NAME, prompt=prompt)

        # Print the entire response for debugging
        print("Raw response from Ollama:", response)

        # Extract the 'response' field instead of 'choices'
        if 'response' in response:
            latest_ai_response = response["response"].strip()  # Store text for streaming
            return latest_ai_response
        else:
            return f"Unexpected response format: {response}"  # Return raw response if 'response' is not found
    except Exception as e:
        return f"Error generating response: {str(e)}"

# Route to handle POST requests and generate responses
@app.route('/query', methods=['POST'])
def query():
    data = flask.request.get_json()  # Get JSON data from the request
    user_message = data.get('input', '')  # Extract the 'input' field from the JSON payload

    if not user_message:
        return flask.jsonify({'error': 'No input provided'}), 400  # Return error if input is missing

    # Get the AI-generated response based on the message
    ai_response = get_ai_response(user_message)

    return flask.jsonify({'response': ai_response})

# Route to serve the HTML overlay (used in Streamlabs or any browser)
@app.route('/overlay', methods=['GET'])
def overlay():
    return flask.render_template('overlay.html')

# Route to get the latest AI response for the overlay
@app.route('/latest_response', methods=['GET'])
def latest_response():
    return flask.jsonify({'response': latest_ai_response})

# Function to run Flask server in the background
def run_flask():
    app.run(host='0.0.0.0', port=5000, use_reloader=False)

# Run the Flask server in a separate thread
if __name__ == '__main__':
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()


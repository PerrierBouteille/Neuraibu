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
        You are a fun and interactive Twitch AI assistant named ChatBot-X. Respond humorously:
        User: {user_input}
        ChatBot-X:
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
    return """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Twitch Overlay</title>
        <style>
          #ai-response {
            position: fixed;
            bottom: 10px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(0, 0, 0, 0.6);
            border-radius: 15px;
            padding: 10px;
            color: white;
            font-size: 24px;
            max-width: 500px;
            border: 2px solid #00ff00;
            opacity: 1;
          }
        </style>
      </head>
      <body>
        <div id="ai-response">Waiting for AI response...</div>

        <script>
          let currentResponse = "";  // Store the current AI response to prevent overwriting
          let isTyping = false;  // To ensure typing doesn't restart if text is already being typed
          let typingTimeout;  // To track the timeout for text disappearance

          // Fetch the AI response every 2 seconds
          setInterval(fetchAIResponse, 2000);

          // Function to fetch the AI response from the server
          function fetchAIResponse() {
              fetch('/latest_response')
                  .then(response => response.json())
                  .then(data => {
                      if (data.response && data.response !== currentResponse) {
                          currentResponse = data.response;  // Update the current response
                          if (!isTyping) {  // If not typing, start typing the new response
                              typeEffect(currentResponse);
                          }
                      }
                  })
                  .catch(error => {
                      console.error('Error fetching AI response:', error);
                  });
          }

          // Function for typing effect
          function typeEffect(text) {
              const element = document.getElementById('ai-response');
              let index = 0;
              element.innerHTML = "";  // Clear previous text
              element.style.opacity = "1";  // Make sure the element is visible
              isTyping = true;  // Mark typing as in progress

              // Function to type the next letter
              function typeNextLetter() {
                  if (index < text.length) {
                      element.innerHTML += text.charAt(index);  // Add next letter
                      index++;
                      setTimeout(typeNextLetter, 100);  // Adjust typing speed here
                  } else {
                      // After typing is done, start a timeout to make text disappear after 10 seconds
                      setTimeout(() => {
                          element.style.opacity = "0";  // Fade out text after it's complete
                          isTyping = false;  // Mark typing as complete
                      }, 10000);  // 10 seconds delay before disappearing
                  }
              }

              typeNextLetter();  // Start the typing effect
          }

        </script>
      </body>
    </html>
    """

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


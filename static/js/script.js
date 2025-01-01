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
            let start = Date.now();
            let timer = setInterval(() => {
                let time = Date.now() - start;
                let opacity = 1 - time / 10000;
                element.style.opacity = opacity.toString();  // Fade out text over 10 seconds
                if (time >= 10000) {
                    clearInterval(timer);
                    isTyping = false;  // Mark typing as complete
                }
            }, 16);  // 16ms to match 60fps
        }
    }

    typeNextLetter();  // Start the typing effect
}
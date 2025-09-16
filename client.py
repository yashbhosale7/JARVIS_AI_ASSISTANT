
import google.generativeai as genai
import os

# Configure the API key
# Make sure you've set up your GEMINI_API_KEY environment variable.
# You can get your API key from Google AI Studio.
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Create the model
generation_config = {
    "temperature": 0.9,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
]

model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest",
                              generation_config=generation_config,
                              safety_settings=safety_settings)

def get_gemini_response(query):
    """Sends a query to the Gemini API and returns the response."""
    try:
        response = model.generate_content(query)
        # Check if the response contains text and return it
        if response and response.text:
            return response.text
        else:
            return "Sorry, I couldn't get a response from Gemini."
    except Exception as e:
        print(f"An error occurred while calling the Gemini API: {e}")
        return "Sorry, I am unable to connect to Gemini at the moment."
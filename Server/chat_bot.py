"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=os.environ["API_KEY"])

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 0.7,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  safety_settings={
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_ONLY_HIGH
        },
  system_instruction="Chat with user input",
)

chat_session = model.start_chat()

def chat_with_gemini(user_input):
  return chat_session.send_message(user_input).text   


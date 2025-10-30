from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY_GEMINI = os.getenv("GEMINI_API_KEY")

# Gemini AI client
client = genai.Client(api_key=API_KEY_GEMINI)
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq()

# Try to make a simple completion request
try:
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama3-70b-8192"
    )
    print("Success! Model is available.")
except Exception as e:
    print(f"Error: {e}") 
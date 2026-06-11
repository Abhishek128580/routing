import time
import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_cloud_response(query):

    for attempt in range(3):

        try:

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=query
            )

            return response.text

        except Exception as e:

            print(
                f"Attempt {attempt+1} failed"
            )

            time.sleep(2)

    return (
        "Cloud service temporarily unavailable."
    )
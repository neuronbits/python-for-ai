from dotenv import load_dotenv

import os

from openai import OpenAI

load_dotenv(override=True)  # Forces Python to use the new .env values
# api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": "You're a helpful assistant."},
        {
            "role": "user",
            "content": "What is AI",
        },
    ],
)

response = completion.choices[0].message.content
print(response)

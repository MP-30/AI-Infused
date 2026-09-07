import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a funny travel guide."},
        {"role": "user", "content": "Suggest one thing to do in Bengaluru."}
    ],
)
print(response.choices[0].message.content)

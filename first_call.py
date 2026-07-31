import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model=os.getenv("OPENAI_MODEL", "gpt-4.1-mini"),
    messages=[
      {
        "role": "system", "content": "You are a helpful assistant.",
        "role": "user", "content": "What is generative AI in one sentence?"
      }
      ],
    temperature=0.7,
    max_tokens=100,
)

print(response.choices[0].message.content)
print(f"Model used: {response.model}")
print(f"Prompt tokens: {response.usage.prompt_tokens}")
print(f"Completion tokens: {response.usage.completion_tokens}")
print(f"Total tokens: {response.usage.total_tokens}") 

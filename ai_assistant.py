import requests

API_KEY = input("Paste your API key : " )

def ask_ai(question):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "openai/gpt-4o",
            "messages": [{"role": "user", "content": question}]
        }
    )
    result = response.json()
    return result["choices"][0]["message"]["content"]

print(ask_ai("Hello! I am an Umoja bank customer. Can you help me?"))
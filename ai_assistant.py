import requests

API_KEY = input("Paste your OpenRouter key : " )

def ask_ai(question):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={
            "model": "openai/gpt-4o",
            "messages": [
                {"role": "system", "content": " You are a helpful assistant for Umoja Bank. " } , {"role" : "user" , "content" : question}
            ]
        }
    )
    result = response.json()
    return result["choices"][0]["message"]["content"]


print("Umoja Bank AI Assistant")
print("Type 'quit' to exit\n")

while True :
    question = input("You: ")
    if question == "quit" :
        print("Goodbye!")
        break
    
    answer = ask_ai(question)
    print("Umoja AI: " + answer + "\n")
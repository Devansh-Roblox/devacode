import requests

def ask_openrouter(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": "Bearer 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",  # 👈 Replace with your API key
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",  # You can change to another free model
            "messages": [
                {"role": "system", "content": "You are a helpful coding assistant. Only answer coding questions related to Python, HTML, CSS, JavaScript, and PHP."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

# Example usage
while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break
    print("Bot:", ask_openrouter(user_input))

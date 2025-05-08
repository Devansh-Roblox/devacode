from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

API_KEY = "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"

def ask_openrouter(prompt):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {"role": "system", "content": "You are a helpful coding assistant. Only help with Python, HTML, CSS, JavaScript, and PHP."},
                {"role": "user", "content": prompt}
            ]
        }
    )
    return response.json()["choices"][0]["message"]["content"]

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json["message"]
    
    if "PHP login form" in user_input:
        answer = ask_openrouter("Write a PHP login form with sessions.")
    else:
        answer = ask_openrouter(user_input)
        
    return jsonify({"response": answer})

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# 🔑 Add your Gemini API key here
GEMINI_API_KEY = "YOUR_GEMINI_API_KEY"

API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.json.get("message")

    # Make AI act like DevOps expert
    user_input = "You are a DevOps expert. " + user_input

    payload = {
        "contents": [{
            "parts": [{"text": user_input}]
        }]
    }

    response = requests.post(API_URL, json=payload)

    try:
        reply = response.json()['candidates'][0]['content']['parts'][0]['text']
    except:
        reply = "Error processing request"

    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)

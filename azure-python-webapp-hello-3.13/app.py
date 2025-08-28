from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from Azure App Service on Python 3.13! 🎉"

@app.get("/health")
def health():
    return jsonify(status="ok")

if __name__ == "__main__":
    # Local dev only; Azure uses gunicorn via startup command
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
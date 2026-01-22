from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# 🔴 TEMPORARY (for testing): paste your REAL API key
import os
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_completion(prompt):
    try:
        response = client.responses.create(
            model="gpt-4.1-mini",
            input=prompt
        )
        return response.output_text
    except Exception as e:
        print("OpenAI Error:", e)
        return "Sorry, I could not generate a response."

@app.route("/", methods=["GET", "POST"])
def query_view():
    if request.method == "POST":
        prompt = request.form.get("prompt")
        reply = get_completion(prompt)
        return jsonify({"response": reply})
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

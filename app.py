import os
import google.generativeai as genai
from flask import Flask, render_template, request

app = Flask(__name__)
# This securely pulls the key from the server's environment
genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route("/", methods=["GET", "POST"])
def index():
    script = ""
    if request.method == "POST":
        topic = request.form["topic"]
        prompt = f"Create a 60-second Reels script for '{topic}'. Output ONLY a Markdown table: | Time | Visual | Text | Voiceover |"
        response = model.generate_content(prompt)
        script = response.text
    return render_template("index.html", script=script)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
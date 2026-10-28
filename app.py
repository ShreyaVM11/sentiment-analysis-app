from flask import Flask, render_template, request, redirect, url_for, session, jsonify
import os
import csv
from datetime import datetime
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from textblob import TextBlob
import webbrowser
import threading
from flask import send_file, make_response

# ------------------ Configuration Import ------------------
from config.db_config import (
    SECRET_KEY,
    ADMIN_USERNAME,
    ADMIN_PASSWORD,
    CSV_FILE
)

# ------------------ Flask Setup ------------------
app = Flask(__name__)
app.secret_key = SECRET_KEY

# ------------------ Ensure VADER Lexicon ------------------
try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

# ------------------ Sentiment Analysis ------------------
def analyze_sentiment(sentence: str):
    vader_score = sia.polarity_scores(sentence)['compound']
    blob_score = TextBlob(sentence).sentiment.polarity

    if vader_score >= 0.05:
        sentiment = "Positive"
    elif vader_score <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"

    return {
        "sentence": sentence,
        "vader_score": vader_score,
        "textblob_score": blob_score,
        "sentiment": sentiment
    }

# ------------------ Save Feedback ------------------
def save_feedback(sentence: str, result: dict):
    file_exists = os.path.isfile(CSV_FILE)
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["Timestamp", "Sentence", "VADER", "TextBlob", "Sentiment"])
        writer.writerow([
            datetime.now().isoformat(),
            sentence,
            result["vader_score"],
            result["textblob_score"],
            result["sentiment"]
        ])

# ------------------ Routes ------------------
@app.route("/")
def feedback_form():
    return render_template("feedback.html")

@app.route("/submit", methods=["POST"])
def submit_feedback():
    sentence = request.form.get("feedback", "").strip()
    if not sentence:
        return render_template("feedback.html", error="Please enter feedback.")

    result = analyze_sentiment(sentence)
    save_feedback(sentence, result)
    return render_template("feedback.html", message="Feedback submitted successfully!")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session["admin"] = True
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error="Invalid username or password")
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.pop("admin", None)
    return redirect(url_for("login"))

# ------------------ Dashboard ------------------
@app.route("/dashboard")
def dashboard():
    if not session.get("admin"):
        return redirect(url_for("login"))

    if not os.path.exists(CSV_FILE):
        return render_template(
            "dashboard.html",
            rows=[],
            pos_perc=0, neg_perc=0, neu_perc=0,
            pos_count=0, neg_count=0, neu_count=0
        )

    rows = []
    with open(CSV_FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader, None)
        for row in reader:
            rows.append(row)

    total = len(rows)
    positive = sum(1 for r in rows if r[-1].strip() == "Positive")
    negative = sum(1 for r in rows if r[-1].strip() == "Negative")
    neutral = sum(1 for r in rows if r[-1].strip() == "Neutral")

    pos_perc = round((positive / total) * 100, 2) if total else 0
    neg_perc = round((negative / total) * 100, 2) if total else 0
    neu_perc = round((neutral / total) * 100, 2) if total else 0

    # 🔹 Pass both percentage and count to template
    return render_template(
        "dashboard.html",
        rows=rows,
        pos_perc=pos_perc, neg_perc=neg_perc, neu_perc=neu_perc,
        pos_count=positive, neg_count=negative, neu_count=neutral
    )

# ------------------ Quick Feedback ------------------
@app.route("/quick_feedback", methods=["POST"])
def quick_feedback():
    data = request.get_json()
    quick = data.get("quick")

    feedback_map = {
        "like": ("Quick like", "Positive", 0.9, 0.9),
        "dislike": ("Quick dislike", "Negative", -0.9, -0.9),
        "angry": ("Angry", "Negative", -0.9, -0.8),
        "sad": ("Sad", "Negative", -0.6, -0.5),
        "neutral": ("Neutral", "Neutral", 0.0, 0.0),
        "happy": ("Happy", "Positive", 0.6, 0.7),
        "excited": ("Excited", "Positive", 0.9, 0.9)
    }

    if quick not in feedback_map:
        return jsonify({"error": "Invalid value"}), 400

    sentence, sentiment, vader_score, textblob_score = feedback_map[quick]
    result = {
        "sentence": sentence,
        "vader_score": vader_score,
        "textblob_score": textblob_score,
        "sentiment": sentiment
    }

    save_feedback(sentence, result)
    return jsonify(result)

def open_browser():
    webbrowser.open("http://127.0.0.1:5000")

if __name__ == "__main__":
    threading.Timer(1.0, open_browser).start()
    app.run(debug=False, port=5000)

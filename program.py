from flask import Flask, render_template
from models.data import surahs
from waitress import serve
import webbrowser
import threading
import os
from datetime import datetime

# -----------------------------
# Flask App Initialization
# -----------------------------
app = Flask(__name__)

# -----------------------------
# Routes
# -----------------------------
@app.route("/")
def home():
    # Pass surahs and current year to template
    return render_template("index.html", surahs=surahs, current_year=datetime.now().year)

@app.route("/surah/<int:surah_id>")
def surah_page(surah_id):
    surah = next((s for s in surahs if s["id"] == surah_id), None)
    if surah:
        return render_template("surah.html", surah=surah, current_year=datetime.now().year)
    return "Surah not found", 404

# -----------------------------
# Utility: Auto-open browser
# -----------------------------
def open_browser(host, port):
    url = f"http://{host}:{port}/"
    webbrowser.open_new(url)

# -----------------------------
# Main Entry Point
# -----------------------------
if __name__ == "__main__":
    # Allow environment variables for flexibility
    host = os.getenv("APP_HOST", "127.0.0.1")
    port = int(os.getenv("APP_PORT", "8080"))

    # Open browser automatically after 1 second
    threading.Timer(1.0, open_browser, args=(host, port)).start()

    # Run production-ready server
    serve(app, host=host, port=port)

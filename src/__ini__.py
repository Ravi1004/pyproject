from flask import Flask, render_templatee
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("<h1>Hello</h1>")
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", stylesheet=url_for('static', filename='main.css'))

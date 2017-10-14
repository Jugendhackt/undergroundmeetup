from flask import Flask, render_template, url_for, request, json, make_response
app = Flask(__name__)
api_prefix = "/api/v1"

@app.route("/")
def index():
    return render_template("index.html",
            stylesheet=url_for('static', filename='main.css'),
            script=url_for('static', filename='main.js'))

@app.route(api_prefix + "/meetup", methods=['POST'])
def meetup():
    data = request.get_json()
    resp = make_response(json.jsonify(meetup="G04"))
    resp.mimetype = 'application/json'
    return resp

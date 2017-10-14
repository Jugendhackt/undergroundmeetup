from flask import Flask, render_template, url_for, request, json, make_response
from ugm_interface import findNamedMeetPoint, load_metro_data
import numpy

app = Flask(__name__)
api_prefix = "/api/v1"

metro_data = load_metro_data('data.csv')


@app.route("/")
def index():
    return render_template("index.html",
                           stylesheet=url_for('static', filename='main.css'),
                           script=url_for('static', filename='main.js'))


@app.route(api_prefix + "/meetup", methods=['POST'])
def meetup():
    data = request.get_json()
    try:
        meetup = findNamedMeetPoint(metro_data, data)
        resp = make_response(json.jsonify(meetup=meetup))
        resp.mimetype = 'application/json'
    except ValueError:
        resp = make_response(json.jsonify(error="Invalid Station Name"), 400)
        resp.mimetype = 'application/json'
    return resp

if __name__ == '__main__':
    app.run()

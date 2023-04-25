"""
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
* @Description: This is the main application file for the flask application
"""
import json

from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS

from Bioprocess import load_json as bio

app = Flask(__name__)
CORS(app)


def start_app(host, port, debug=bool()) -> Flask:
    """
    * This is the main function/config for the application
    * @param {string} host
    * @param {string} port
    * @param {bool} debug
    * @return {Flask} app
    """
    if bool(debug) is True:
        app.run(host=host, port=port, debug=debug)
    else:
        print("Debug mode is disabled")
        app.run(host=host, port=port, debug=False)
    return app


@app.route("/", methods=['GET'])
def html():
    """ Renders the html page """
    return render_template('index.html')


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    """
    * This is the route for the upload page
    * @param {POST} request
    * @param {GET} request
    * @return {JSON} status
    """
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        results(bio(json.loads(data)))
    return redirect(url_for('uploaded', _method='GET'), code=307)


@app.route("/uploaded", methods=['GET', 'POST'])
def uploaded():
    """
    * This is the route for the uploaded page
    """
    return render_template('upload.html')


@app.route("/results", methods=['GET'])
def results(result):
    result_data = json.loads(result)
    for alignment in result_data:
        result_data.append({
            "score": alignment['score'],
            "aligned": alignment['aligned'],
        })
    return render_template('results.html', results=result_data)


# TO debug the application run the following command
# python -m flask --app backend.py  run --debug
start_app(host="0.0.0.0", port=5000)

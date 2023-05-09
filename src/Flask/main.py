'''
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
* @Description: This is the main application file for the flask application
'''
import os
from flask import Flask, render_template, request, redirect, url_for
from flask_cors import CORS
import Bioprocess as Bio

app = Flask(__name__)
CORS(app)


def start_app(host, port, debug=bool()) -> Flask:
    '''
    * This is the main function/config for the application
    * @param {string} host
    * @param {string} port
    * @param {bool} debug
    * @return {Flask} app
    '''
    Bio.qr_code(host, port)
    if bool(debug) is True:
        app.run(host=host, port=port, debug=debug)
    else:
        print("Debug mode is disabled")
        app.run(host=host, port=port, debug=False)
    return app


@app.route("/", methods=['GET'])
def html():
    ''' Renders the html page '''
    return render_template('index.html')


@app.route("/upload", methods=['POST', 'GET'])  # type: ignore
def upload():
    '''
    * This is the route for the upload page
    * @param {POST} request
    * @param {GET} request
    * @return {JSON} status
    '''
    if request.method == 'POST':
        data: str = request.data.decode('utf-8')
        Bio.load_json(data)
        return redirect(url_for('html', _method='GET'))

@app.route("/result", methods=['GET'])
def results():
    '''
    * This is the route for the results page
    '''
    return render_template('results.html')


@app.route("/api/results", methods=['GET'])
def results_api():
    '''
    * This is the route for the results page
    '''
    return redirect(url_for('static', filename='results.txt'))


@app.route("/api/delete", methods=['POST', 'GET'])
def delete():
    '''
    * This is the route for the delete page
    '''
    if os.path.exists("static/results.txt") or os.path.exists("static/qr.png"):
        os.remove("static/results.txt")
        os.remove("static/qr.png")
        
    
    return redirect(url_for('html', _method='GET'))

# TO debug the application run the following command
# python -m flask --app backend.py  run --debug
start_app(host="0.0.0.0", port=5000, debug=True)

"""
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
* @Description: This is the main application file for the flask application
"""
import os
from flask import Flask, make_response, render_template, request, redirect, url_for, Response
from flask_cors import CORS
from modules import Bioprocess as Bio

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


@app.route("/", methods=['GET', 'POST'])
def userpage():
    if request.method == 'POST':
        user = request.form['username']
        resp = make_response(render_template("index.html",userid=user))
        resp.set_cookie('Username', user, samesite='Strict')
        return resp
    return render_template('userpage.html')

# @app.route("<username>/index", methods=['GET'])
# def index(username):
#     """ Renders the index.html page """
#     render_template("index.html",username=username)


@app.route("/upload", methods=['POST', 'GET'])
def upload():
    """
    * This is the route for the upload page
    * @param {POST} request
    * @param {GET} request
    * @return {JSON} status
    """
    USER_COOKIE = usercookie()
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        Bio.load_json(data)
        return render_template('index.html',username=USER_COOKIE)


@app.route("/results", methods=['GET', 'POST'])
def results():
    """
    * This is the route for the results page
    """
    USER_COOKIE = usercookie()
    if request.method == 'POST':
        data = request.data.decode('utf-8')
        Bio.qr_code(data)
    return render_template('results.html',username=USER_COOKIE)


@app.route("/api/results", methods=['GET'])
def results_api():
    """
    * This is the route for the results text file.
    """
    USER_COOKIE = usercookie()

    if request.method == 'GET' and os.path.exists(f"static/results_{USER_COOKIE}.txt"):
        return redirect(url_for('static', filename=f'results_{USER_COOKIE}.txt'))
    else:
        return Response(status=404)


@app.route("/api/delete", methods=['POST'])
def delete():
    """
    * This is the route for the delete page
    """
    USER_COOKIE = usercookie()
    RESULT_PATH = f"static/results_{USER_COOKIE}.txt"
    QR_PATH=f"static/qr_{USER_COOKIE}.png"
    if os.path.exists(RESULT_PATH) or os.path.exists(QR_PATH):
        os.remove(RESULT_PATH)
        os.remove(QR_PATH)
    return render_template('index.html',username=USER_COOKIE)

def usercookie():
    USER_COOKIE = request.cookies.get("Username")
    return USER_COOKIE


""" 
To debug the application run the following command
python main.py or Uncomment the following line
"""
if __name__ == '__main__':
    start_app("localhost", 5000, True)

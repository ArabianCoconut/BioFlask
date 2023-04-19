"""
* @Author: ArabianCoconut
* @Version: 0.0.1 Alpha
* @Description: This is the main application file for the flask application
"""
from flask import Flask, render_template,request

app = Flask(__name__)
FILE_PATH=r'src\Bio\data.json'

def start_app(host,port,debug=bool()):
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
        with open(FILE_PATH, 'w+',encoding='utf-8') as outfile:
            outfile.write(request.data.decode('utf-8'))
            outfile.close()
    return {'status': 'success',
            'message': 'File uploaded successfully'}


# TO debug the application run the following command
# python -m flask --app backend.py  run --debug
start_app(host="0.0.0.0", port=5000)
"""
* This is the main application file for the flask application
"""
from flask import Flask, render_template,request


app = Flask(__name__)
FILE_PATH=r'src\Bio\data.json'

def start_app():
    """
    * This is the main function for the application
    * @return {Flask} app
    """
    app.run(host='0.0.0.0', port=5000, debug=True)
    return app


@app.route("/", methods=['GET'])
def html():
    """ Render the html page """
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


start_app()

from flask import Flask
app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def hello_world():
    return 'Hello, World!'

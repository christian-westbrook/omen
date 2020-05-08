from flask import Flask
from flask_cors import CORS, cross_origin
import extractor.singleExtract

app = Flask(__name__)
cors = CORS(app)
app.config['CORS-HEADERS'] = 'Content-Type'

@app.route('/generate', methods=['GET', 'POST'])
@cross_origin()
def hello_world():
    return 'Hello, World!'

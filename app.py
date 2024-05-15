from flask import Flask
from flask_cors import CORS, cross_origin
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def get_endpoints():
    file = open('./endpoints.json')
    data = json.load(file)
    return data

if __name__ == "__main__":
    app.run()
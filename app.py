# app.py
from flask import Flask
from flask_cors import CORS
from main import random_data_string

app = Flask(__name__)
app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return random_data_string()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)



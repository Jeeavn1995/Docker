from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello Dosto, welcome to DevOps Zero To Hero (Junoon  Batch 9) Welcome Mr Ramjeevan kumar to this batch'

@app.route('/health')
def health():
    return 'Server is up and running'

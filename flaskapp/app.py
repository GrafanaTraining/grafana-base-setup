from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
        return "Hello World!"

@app.route('/hello')
def greetings():
        return "Hello participant!"
@app.route('/welcome')
def welcome():
    return "Welcome to the training!"

if __name__ == '__main__':
        app.run(host='0.0.0.0', port=8000)
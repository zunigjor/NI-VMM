from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


@app.route('/<user>')
def hello_user(user):  # put application's code here
    return f'Hello {user}'


if __name__ == '__main__':
    app.run(host='0.0.0.0:5000')
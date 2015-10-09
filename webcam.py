from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/channels')
def channels():
    return '[{"id":"cantina","url":"http://xpto.com:20000"}]'

if __name__ == '__main__':
    app.run()

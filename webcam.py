from flask import Flask, render_template, Response
from camera import VideoCamera

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen(VideoCamera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/channels/<channel_id>')
def show_channel(channel_id):
    return render_template('channel.html', channel_id=channel_id)


@app.route('/channels')
def channels():
    return '[{"id":"cantina","url":"http://xpto.com:20000"}]'

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

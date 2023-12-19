from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    video_directory = os.path.join(app.static_folder, 'videos')

    files = os.listdir(video_directory)
    files.sort(reverse=True)
    latest_videos = files[:3]
    return render_template('index.html', videos=latest_videos)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


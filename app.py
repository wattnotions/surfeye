from flask import Flask, render_template
import os
from datetime import datetime

app = Flask(__name__)

    
def format_timestamp(filename):
    # Extract the Unix timestamp from the filename (assuming format 'timestamp.mp4')
    unix_timestamp = int(filename.split('.')[0])
    # Convert Unix timestamp to datetime object
    timestamp = datetime.fromtimestamp(unix_timestamp)
    # Format the datetime object into a human-readable form
    return timestamp.strftime('%d %B %Y %H:%M')

@app.route('/')
def index():
    video_directory = os.path.join(app.static_folder, 'videos')
    files = os.listdir(video_directory)
    files.sort(reverse=True)
    latest_videos = files[:3]
    video_timestamps = [format_timestamp(video) for video in latest_videos]
    return render_template('index.html', videos=latest_videos, video_timestamps=video_timestamps)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

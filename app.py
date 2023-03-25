from pathlib import Path

from flask import Flask, render_template, send_from_directory


TRACKS_FOLDER = Path(__file__).parent.resolve() / 'tracks'
app = Flask(__name__)


def get_tracks():
    folder_objects = TRACKS_FOLDER.glob('**/*.*')
    tracks = [
        str(item).split('\\')[-1]
        for item in folder_objects
    ]
    return tracks


@app.route('/tracks/<path:filename>')
def track_files(filename):
    return send_from_directory(TRACKS_FOLDER, filename)


@app.route('/')
def main():
    items = get_tracks()
    return render_template('main.html', items=items)

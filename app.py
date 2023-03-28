from pathlib import Path

from flask import Flask, render_template, send_from_directory


MAIN_FOLDER = Path(__file__).parent.resolve()
app = Flask(__name__)


def get_tracks():
    folder_objects = (MAIN_FOLDER / 'tracks').glob('**/*.*')
    tracks = [
        'tracks//' + str(item).split('\\')[-1]
        for item in folder_objects
    ]
    print(f'tracks: {tracks}')
    return tracks


def get_subfolders_files(tracks_folder: str) -> dict:
    result = {}
    path = Path(tracks_folder)
    if not path.exists():
        return result
    for subfolder in path.iterdir():
        if not subfolder.is_dir():
            continue
        files = []
        for file in subfolder.iterdir():
            if not file.is_file():
                continue
            files.append(file.name)
        result[subfolder.name] = files
    return result


@app.route('/<path:filename>')
def local_files(filename):
    print(f'file request: {filename}')
    return send_from_directory(MAIN_FOLDER, filename)


@app.route('/')
def main():
    items = get_tracks()
    return render_template('main.html', items=items)
 
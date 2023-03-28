from pathlib import Path

from flask import Flask, render_template, send_from_directory


MAIN_FOLDER = Path(__file__).parent.resolve()
app = Flask(__name__)


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


@app.route('/<path:folder>/<path:filename>')
def local_files(filename, folder = None):
    target_folder = MAIN_FOLDER
    file = filename
    if folder:
        target_folder /= folder
    return send_from_directory(target_folder, file)


@app.route('/')
def main():
    items = get_subfolders_files(MAIN_FOLDER / 'tracks')
    return render_template('main.html', items=items)
 
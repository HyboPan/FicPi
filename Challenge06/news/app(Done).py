import os
import json
from flask import Flask, render_template

app = Flask(__name__)

result = {}
directory = os.path.join(os.getcwd(), '../files')
for i in os.listdir(directory):
    file_path = os.path.join(directory, i)
    with open(file_path) as f:
        result[i[:-5]] = json.load(f)

@app.route('/')
def index():
    return render_template('index.html',
        title_list = [i['title'] for i in result.values()])

@app.route('/files/<filename>')
def file(filename):
    f = result.get(filename)
    if not f:
        abort(404)
    return render_template('file.html', file_item = f)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

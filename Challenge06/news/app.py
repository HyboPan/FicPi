import os
import json
from flask import Flask, render_template
 
app = Flask(__name__)
 
 
def get_title_list():  # 读取titile
    for root, dirs, titles in os.walk(r'/home/shiyanlou/files'):
        title = os.path.splitext(titles)[0]
        title_list = []
        title_list.append(title)
    return title_list
 
def read_files():  # 读取文件内容
    for root, dirs, titles in os.walk(r'/home/shiyanlou/files'):
        with open(title, 'r') as file:
            file_item = json.loads(file.read())
        return file_item


@app.route('/')
def index():
    return render_template('index.html', title_list = get_title_list())

@app.route('/files/<filename>')
def file(filename):
    file_item = read_files(filename)
    if username == 'invalid':
        abort(404)
    return render_template('file.html', file_item = file_item)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404


if __name__ == '__main__':
    app.run()

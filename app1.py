1. 404.html # Done

<h1> shiyanlou 404</h1>



2. base.html # 用不上



3. index.html # Done

<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Content</title>
</head>
<body>
    {% for title in title_list %}
        <li>{{ title }}</li>
    {% endfor %}
</body>
</html>


4. file.html # 这个里面的 file_item 要出现在 app.py 里

<!DOCTYPE html>
<html>
<haed>
    <meta charset="utf-8">
    <title>flie</title>
</head>
<body>
    <h1>{{ file_item['title'] }}</h1>
    <p>{{ file_item['created_time'] }}</p>
    <p>{{ file_item['content'] }}</p>
</body>
</html>



5. app.py

import os
import json
from flask impot Flask, render_template

app = Flask(__name__)


def get_title_list():  # 读取titile
    for root, dirs, titles in os.walk(r'/home/shiyanlou/files')
        title = os.path.splitext(titles)[0]
        title_list = []
        title_list.append(title)
    return title_list

def read_files():  # 读取文件内容
    for root, dirs, titles in os.walk(r'/home/shiyanlou/files')
        with open(title, 'r') as file:
            file_item = json.loads(file.read())
    return file_item
   

@app.route('/')
def index():
    return render_template('index.html', title_list = get_title_list()) # tilte_list 在 index.html中用来循环

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

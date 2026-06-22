import os
from flask import Flask, render_template

# 修改這裡：使用 __file__ 來定位檔案所在絕對路徑，避開相對路徑問題
# 將 templates 資料夾明確設為 app.py 同層的 /templates
app = Flask(__name__, 
            template_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates'),
            static_folder=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static'))

@app.route('/')
def index():
    return render_template('index.html')
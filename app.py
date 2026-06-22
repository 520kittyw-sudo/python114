import os
from flask import Flask, render_template

# 核心修正：明確告訴 Flask 去哪裡找 templates
# os.path.dirname(__file__) 會自動抓到 app.py 所在的目錄
base_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(base_dir, 'templates')

app = Flask(__name__, template_folder=template_dir)

@app.route('/')
def index():
    return render_template('index.html')
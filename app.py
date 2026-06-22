import os
from flask import Flask, render_template

# 這裡幫 Flask 指定絕對路徑
app = Flask(__name__, template_folder=os.path.join(os.path.dirname(__file__), 'templates'))

@app.route('/')
def index():
    return render_template('index.html')
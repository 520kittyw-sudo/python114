import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # 這裡會打印出伺服器運行的當前目錄
    print(f"當前工作目錄: {os.getcwd()}")
    # 這裡會打印出 templates 資料夾內的檔案列表
    if os.path.exists('templates'):
        print(f"templates 資料夾內容: {os.listdir('templates')}")
    else:
        print("警告：找不到 templates 資料夾！")
        
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
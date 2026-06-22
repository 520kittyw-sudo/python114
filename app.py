from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# 確保這三個路徑是乾淨的
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/result', methods=['POST'])
def result():
    # 這裡放你的計算邏輯
    player_name = request.form.get('player_name')
    # ... (其餘計算程式碼)
    return render_template('result.html', name=player_name) 

if __name__ == '__main__':
    app.run()
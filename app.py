from flask import Flask, render_template, request, session, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import numpy as np
import os
from scraper import get_market_data

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# 設定絕對路徑確保資料庫存在
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'game.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# 資料庫模型：新增了 nickname 欄位
class GameResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(50))
    choices = db.Column(db.String(100))
    mean = db.Column(db.Float)
    var = db.Column(db.Float)
    personality = db.Column(db.String(200))

with app.app_context():
    db.create_all()

def analyze_game_behavior(choices):
    arr = np.array(choices)
    mean, var = float(np.mean(arr)), float(np.var(arr))
    if mean > 70: p = "大膽的開拓者：你偏好高報酬與極高風險。"
    elif mean < 30: p = "穩健的守成者：你追求絕對的安全。"
    elif var > 600: p = "心跳狂飆的博弈家：你喜歡在極端策略中求勝。"
    else: p = "均衡的操盤手：你在風險與報酬間取得平衡。"
    return round(mean, 2), round(var, 2), p

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
    session['nickname'] = request.form.get('nickname')
    return redirect(url_for('game', round_num=1))

@app.route('/game/<int:round_num>', methods=['GET', 'POST'])
def game(round_num):
    if round_num == 1: session['choices'] = []
    
    if request.method == 'POST':
        choice = float(request.form.get('risk_value'))
        choices = session.get('choices', [])
        choices.append(choice)
        session['choices'] = choices
        return redirect(url_for('game', round_num=round_num + 1)) if round_num < 5 else redirect(url_for('result'))
    
    market_info = get_market_data()
    return render_template(f'round{round_num}.html', market_info=market_info)

@app.route('/result')
def result():
    nickname = session.get('nickname', '玩家')
    choices = session.get('choices', [])
    if not choices: return redirect(url_for('index'))
    
    mean, var, personality = analyze_game_behavior(choices)
    new_res = GameResult(nickname=nickname, choices=",".join(map(str, choices)), mean=mean, var=var, personality=personality)
    db.session.add(new_res)
    db.session.commit()
    
    # 結尾新增訊息
    message = f"親愛的 {nickname} 你好！"
    return render_template('result.html', mean=mean, var=var, personality=personality, nickname=nickname, message=message)

if __name__ == '__main__':
    app.run(debug=True)
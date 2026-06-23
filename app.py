from flask import Flask, render_template, request, session, redirect, url_for
import numpy as np

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def analyze_game_behavior(choices):
    arr = np.array(choices)
    mean = float(np.mean(arr))
    var = float(np.var(arr))
    if mean > 70: personality = "大膽的開拓者：你偏好高報酬與極高風險，天生具有冒險家精神。"
    elif mean < 30: personality = "穩健的守成者：你追求絕對的安全，精於避險，擅長穩扎穩打。"
    elif var > 600: personality = "心跳狂飆的博弈家：你的決策變動大，喜歡在極端策略中尋求勝利。"
    else: personality = "均衡的操盤手：你在風險與報酬間展現了卓越的理性平衡感。"
    return round(mean, 2), round(var, 2), personality

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/game/<int:round_num>', methods=['GET', 'POST'])
def game(round_num):
    if round_num == 1: session['choices'] = []
    if request.method == 'POST':
        choice = float(request.form.get('risk_value'))
        choices = session.get('choices', [])
        choices.append(choice)
        session['choices'] = choices
        if round_num < 5: return redirect(url_for('game', round_num=round_num + 1))
        else: return redirect(url_for('result'))
    return render_template(f'round{round_num}.html')

@app.route('/result')
def result():
    choices = session.get('choices', [])
    if not choices: return redirect(url_for('index'))
    mean, var, personality = analyze_game_behavior(choices)
    return render_template('result.html', mean=mean, var=var, personality=personality)

if __name__ == '__main__':
    app.run(debug=True)
import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# 首頁
@app.route('/')
def index():
    info_data = {
        "title": "幾何人格：山海特質心理賽局網站",
        "member": "黃琦瑤",
        "department": "數學系資訊數學組",
        "description": "本網站結合『動態網頁爬蟲』與『機率統計變異數分析』..."
    }
    return render_template('index.html', info=info_data)

# 遊戲頁面
@app.route('/game')
def game():
    info_data = {"title": "幾何賽局 - 挑戰頁"}
    return render_template('game.html', info=info_data)

# 結果計算頁面
@app.route('/result', methods=['POST'])
def result():
    player_name = request.form.get('player_name')
    # ... (你的數據取得與計算邏輯) ...
    
    # 這裡的變數名稱一定要跟 HTML 裡的一模一樣！
    return render_template('result.html', 
                           name=player_name, 
                           mean=round(mean_val, 2), 
                           var=round(var_val, 2), 
                           conclusion=conclusion)

    mean_val = np.mean(data)
    var_val = np.var(data)
    
    if mean_val < 35:
        conclusion = "海之平穩：你傾向深思熟慮，在動盪中尋求安全感。"
    elif mean_val < 70:
        conclusion = "風之脈動：你能在風險與機遇中找到平衡，策略靈活。"
    else:
        conclusion = "火之狂熱：你是冒險家，敢於在未知中挑戰極限。"
        
    return render_template('result.html', 
                           name=player_name, 
                           mean=round(mean_val, 2), 
                           var=round(var_val, 2), 
                           conclusion=conclusion)

if __name__ == '__main__':
    app.run()
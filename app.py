from flask import Flask, render_template, request
import numpy as np
import os

app = Flask(__name__)

# 確保路徑設定正確
current_dir = os.path.dirname(os.path.abspath(__file__))
template_dir = os.path.join(current_dir, 'templates')

# --- 核心分析模型 ---
def analyze_game_behavior(choices):
    """計算玩家決策特質"""
    arr = np.array(choices)
    mean = np.mean(arr)
    variance = np.var(arr)
    
    if variance < 100:
        personality = "海之平穩：你傾向於深思熟慮，在動盪中尋求安全感。"
    elif variance < 800:
        personality = "山海共鳴：你在保守與冒險間有獨特的平衡感。"
    else:
        personality = "山之巔峰：你是一位冒險家，敢於在極端機率中追求勝利。"
    return round(mean, 2), round(variance, 2), personality

# --- 路由與首頁 ---
@app.route('/')
def index():
    # 這裡保留你原本定義的所有變數，就不會報 'info' is undefined 了
    project_info = {
        "title": "幾何人格：山海特質心理賽局網站",
        "description": "本網站結合『動態網頁爬蟲』與『機率統計變異數分析』...",
        "member": "黃琦瑤",
        "department": "數學系資訊數學組"
    }
    return render_template('index.html', info=project_info)

# --- 遊戲與邏輯 ---
@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        # 確保三個回合數值都能抓到
        try:
            r1 = float(request.form.get('round1', 50))
            r2 = float(request.form.get('round2', 50))
            r3 = float(request.form.get('round3', 50))
            name = request.form.get('player_name', '匿名挑戰者')
            
            mean, var, personality = analyze_game_behavior([r1, r2, r3])
            
            return render_template('result.html', 
                                   name=name, 
                                   mean=mean, 
                                   var=var, 
                                   personality=personality)
        except Exception as e:
            return f"運算錯誤: {str(e)}"
            
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)
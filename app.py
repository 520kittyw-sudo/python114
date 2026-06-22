import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

# --- 必須補上這兩個路由 ---

@app.route('/')
def index():
    # 定義 info 字典，包含 HTML 需要的所有資料
    info_data = {
        "title": "幾何人格：山海特質心理賽局網站",
        "member": "黃琦瑤",
        "department": "數學系資訊數學組",
        "description": "本網站結合『動態網頁爬蟲』與『機率統計變異數分析』..."
    }
    # 將 info 傳遞給模板
    return render_template('index.html', info=info_data)

@app.route('/game')
def game():
    # 當訪問 /game 時，顯示測驗頁面
    return render_template('game.html')

# --- 你原本的結果處理路由 ---

@app.route('/result', methods=['POST'])
def result():
    player_name = request.form.get('player_name')
    
    # 取得三個回合的風險數值
    try:
        data = [
            int(request.form.get('round1')),
            int(request.form.get('round2')),
            int(request.form.get('round3'))
        ]
    except (TypeError, ValueError):
        return "請確保所有選項都已選取！"

    # 使用 NumPy 進行分析
    mean_val = np.mean(data)    # 期望值
    var_val = np.var(data)      # 方差 (Variance)
    
    # 根據數值範圍給予不同的分析結論
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
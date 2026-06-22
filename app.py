import numpy as np
from flask import Flask, render_template, request

app = Flask(__name__)

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
    
    # 根據數值範圍給予不同的分析結論 (修正 Bug)
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
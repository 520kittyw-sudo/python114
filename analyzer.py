import numpy as np

def analyze_game_behavior(choices):
    arr = np.array(choices)
    mean = float(np.mean(arr))
    var = float(np.var(arr))
    
    # 初始化一個預設值，確保變數一定存在
    personality = "尚未分類的觀察者：你的決策模式非常獨特。"
    
    if mean > 70:
        personality = "大膽的開拓者：你偏好高報酬與極高風險，天生具有冒險家精神。"
    elif mean < 30:
        personality = "穩健的守成者：你追求絕對的安全，精於避險，擅長穩扎穩打。"
    elif var > 600:
        personality = "心跳狂飆的博弈家：你的決策變動大，喜歡在極端策略中尋求勝利。"
    else:
        # 當前面都不符合時，這裡會補上預設的分類
        personality = "均衡的操盤手：你在風險與報酬間展現了卓越的理性平衡感。"
        
    return mean, var, personality
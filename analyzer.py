import numpy as np

def analyze_game_behavior(choices):
    """
    choices: 玩家在三回合內選擇的風險籌碼清單，例如 [10, 80, 50]
    10 代表極度保守（海型），80 代表極度冒險（山型）
    """
    choices_array = np.array(choices)
    
    # 數學計算：平均值 (期望決策) 與方差 (決策起伏度)
    mean_value = float(np.mean(choices_array))
    variance_value = float(np.var(choices_array))
    
    # 判定邏輯：
    # 如果方差很大 (每次選擇高低落差極大) 或 平均投入籌碼極高 -> 山型人
    # 如果方差很小 (每次選擇都很穩健、平緩) -> 海型人
    if variance_value > 400 or mean_value > 60:
        personality = "陡峭冒險的『山型人』 (Peak Player)"
    else:
        personality = "平穩柔和的『海型人』 (Wave Player)"
        
    return mean_value, variance_value, personality
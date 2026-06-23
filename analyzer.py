# analyzer.py
import numpy as np

def analyze_game_behavior(choices):
    arr = np.array(choices)
    mean = float(np.mean(arr))
    var = float(np.var(arr))
    # ... 你的分析判斷邏輯 ...
    return mean, var, personality
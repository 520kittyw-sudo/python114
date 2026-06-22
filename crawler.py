import requests
from datetime import datetime
import psycopg2

DATABASE_URL = "postgresql://qi_mo_zhuan_an_user:dUIboiyu0nLjIWSGc4sNvyypOMrelJ8u@dpg-d8r9enfavr4c73e9b01g-a.singapore-postgres.render.com/qi_mo_zhuan_an"

def fetch_and_save_daily_data():
    # 模擬爬取動態財經或氣象開放資料的波動度 (這裡用一個公開的隨機天氣/波動指引 API 示意)
    # 妳也可以用 requests 去抓取某個特定網頁的數字
    try:
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        data = response.json()
        # 拿取動態變化的數字尾數來當作今天的數學隨機波動率 (Volatility)
        price = data['bpi']['USD']['rate_float']
        volatility = round((price % 100) / 100, 2)  # 讓數值落在 0 到 1 之間
    except Exception as e:
        print(f"爬蟲抓取失敗，啟動備用數學隨機值: {e}")
        import random
        volatility = round(random.uniform(0.1, 0.9), 2)

    today = datetime.now().strftime("%Y-%m-%d")
    
    # 寫入 Render PostgreSQL
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    try:
        cur.execute(
            "INSERT INTO market_data (date, volatility_value) VALUES (%s, %s) ON CONFLICT (date) DO UPDATE SET volatility_value = EXCLUDED.volatility_value;",
            (today, volatility)
        )
        conn.commit()
        print(f"今日爬蟲數據已儲存！日期：{today}，波動度設定為：{volatility}")
    except Exception as e:
        print("資料庫寫入錯誤:", e)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    fetch_and_save_daily_data()
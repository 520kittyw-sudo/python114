import os
import psycopg2

# 請把引號內的網址換成妳在 Render 申請的 External Database URL
DATABASE_URL = "postgresql://qi_mo_zhuan_an_user:dUIboiyu0nLjIWSGc4sNvyypOMrelJ8u@dpg-d8r9enfavr4c73e9b01g-a.singapore-postgres.render.com/qi_mo_zhuan_an"

def init_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    
    # 1. 儲存爬蟲數據的表格
    cur.execute('''
        CREATE TABLE IF NOT EXISTS market_data (
            id SERIAL PRIMARY KEY,
            date TEXT UNIQUE,
            volatility_value REAL
        );
    ''')
    
    # 2. 儲存玩家決策與分析結果的表格
    cur.execute('''
        CREATE TABLE IF NOT EXISTS game_results (
            id SERIAL PRIMARY KEY,
            player_name TEXT,
            score REAL,
            variance_value REAL,
            personality_type TEXT
        );
    ''')
    
    conn.commit()
    cur.close()
    conn.close()
    print("資料庫資料表初始化成功！")

if __name__ == "__main__":
    init_db()
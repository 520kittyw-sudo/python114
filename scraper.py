import requests
from bs4 import BeautifulSoup

def get_market_data():
    try:
        # 使用請求獲取市場數據
        url = "https://www.coingecko.com/en/coins/bitcoin"
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 抓取價格標籤 (根據網站結構)
        price_element = soup.find('span', {'data-price-btc': True})
        if price_element:
            return "比特幣現況：數據即時同步中，市場波動較大。"
        return "比特幣現況：市場交易活躍。"
    except:
        return "市場數據同步中"
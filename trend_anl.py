import requests
import json
from datetime import datetime, timedelta

# 네이버 API 키
CLIENT_ID = 'InYeM2RvrwIDjdft0Vx5'
CLIENT_SECRET = 'egJhtRdxZE'

# 트렌드 분석용 데이터 파일
DATA_FILE = 'trend_data.json'

# 네이버 API로 상품 검색 함수
def get_trending_keywords(query):
    url = f'https://openapi.naver.com/v1/search/shop.json?query={query}&display=10'
    headers = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        trending_keywords = [item['title'] for item in data['items']]
        return trending_keywords
    else:
        print("Error:", response.status_code)
        return None

# 트렌드 데이터 저장 함수
def save_trend_data(query, keywords):
    date_str = datetime.now().strftime('%Y-%m-%d')
    try:
        with open(DATA_FILE, 'r') as f:
            trend_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        trend_data = {}

    # 날짜별로 데이터를 저장
    if query not in trend_data:
        trend_data[query] = {}
    trend_data[query][date_str] = keywords

    # 파일에 저장
    with open(DATA_FILE, 'w') as f:
        json.dump(trend_data, f, indent=4)

# 데이터 비교 및 트렌드 출력 함수
def display_trends(query):
    try:
        with open(DATA_FILE, 'r') as f:
            trend_data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        print("데이터 파일이 없습니다. 먼저 트렌드 데이터를 수집하세요.")
        return

    if query not in trend_data:
        print(f"{query}에 대한 데이터가 없습니다.")
        return

    # 최근 날짜 데이터와 이전 날짜 데이터 비교
    dates = sorted(trend_data[query].keys())
    latest_keywords = trend_data[query][dates[-1]]
    prev_keywords = trend_data[query][dates[-2]] if len(dates) > 1 else []

    print(f"최신 트렌드 ({dates[-1]}):")
    for i, keyword in enumerate(latest_keywords, 1):
        trend_info = f"{i}. {keyword}"
        if keyword not in prev_keywords:
            trend_info += " (New)"
        print(trend_info)

    # 전날 대비 새로 추가된 키워드 출력
    if prev_keywords:
        new_trends = set(latest_keywords) - set(prev_keywords)
        print("\n새롭게 떠오른 키워드:")
        for keyword in new_trends:
            print(f"- {keyword}")

if __name__ == "__main__":
    query = input("분석할 검색어를 입력하세요: ")
    keywords = get_trending_keywords(query)
    if keywords:
        save_trend_data(query, keywords)
        display_trends(query)
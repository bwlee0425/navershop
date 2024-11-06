import requests
from datetime import datetime, timedelta

# 네이버 API 키
CLIENT_ID = 'O_PLGQP5uShA2wpukSCL'
CLIENT_SECRET = 'C4Oq_EmUzW'

# API 요청 URL
API_URL = "https://openapi.naver.com/v1/datalab/search"

def get_trend_data(start_date, end_date, time_unit, keyword_groups, device=None, ages=None, gender=None):
    headers = {
        "X-Naver-Client-Id": CLIENT_ID,
        "X-Naver-Client-Secret": CLIENT_SECRET,
        "Content-Type": "application/json"
    }

    # 요청 body 설정
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "timeUnit": time_unit,
        "keywordGroups": keyword_groups
    }

    if device:
        body["device"] = device
    if ages:
        body["ages"] = ages
    if gender:
        body["gender"] = gender

    # POST 요청
    response = requests.post(API_URL, headers=headers, json=body)

    # 응답 처리
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"Error Code: {response.status_code}", "details": response.json()}

def get_recent_trend_data(query):
    today = datetime.today()
    six_months_ago = (today - timedelta(days=6*30)).strftime('%Y-%m-%d')
    one_week_ago = (today - timedelta(days=7)).strftime('%Y-%m-%d')
    yesterday = (today - timedelta(days=1)).strftime('%Y-%m-%d')
    
    keyword_groups = [{"groupName": query, "keywords": [query]}]

    # 최근 6개월 데이터 (월 단위)
    six_month_data = get_trend_data(six_months_ago, yesterday, "month", keyword_groups)
    
    # 최근 1주 데이터 (주 단위)
    one_week_data = get_trend_data(one_week_ago, yesterday, "week", keyword_groups)
    
    # 어제 데이터 (일 단위)
    yesterday_data = get_trend_data(yesterday, yesterday, "date", keyword_groups)
    
    return {
        "six_month_data": six_month_data,
        "one_week_data": one_week_data,
        "yesterday_data": yesterday_data
    }

def format_trend_results(results):
    formatted_results = []
    if results and 'results' in results:
        for result in results['results']:
            title = result['title']
            keywords = ', '.join(result['keywords'])
            data_points = []
            for data in result['data']:
                data_points.append({
                    "날짜": data['period'],
                    "검색량 비율": f"{data['ratio']:.2f}"
                })
            formatted_results.append({
                "주제어": title,
                "키워드": keywords,
                "데이터": data_points
            })
    else:
        formatted_results.append({"message": "트렌드 분석 결과가 없습니다."})
    return formatted_results
import requests

# 네이버 API 키 입력
CLIENT_ID = 'InYeM2RvrwIDjdft0Vx5'
CLIENT_SECRET = 'egJhtRdxZE'

def search_products(query):
    url = f'https://openapi.naver.com/v1/search/shop.json?query={query}'
    headers = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        return response.json()  # JSON 형식으로 데이터 반환
    else:
        return {"error": f"Error: {response.status_code}"}

def format_products(products):
    results = []
    if products and 'items' in products:
        for item in products['items']:
            results.append({
                "상품명": item['title'],
                "가격": f"{item['lprice']}원",
                "이미지 URL": item['image']  # 이미지 URL 추가
            })
    else:
        results.append({"message": "검색 결과가 없습니다."})
    return results
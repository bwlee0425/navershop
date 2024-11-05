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
        print(f"Error: {response.status_code}")
        return None

def display_products(products):
    if products:
        for item in products['items']:
            print(f"상품명: {item['title']}, 가격: {item['lprice']}원")

if __name__ == "__main__":
    query = input("검색할 상품명을 입력하세요: ")
    products = search_products(query)
    display_products(products)
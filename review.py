import requests

CLIENT_ID = 'InYeM2RvrwIDjdft0Vx5'
CLIENT_SECRET = 'egJhtRdxZE'

def get_product_reviews(product_id):
    url = f'https://openapi.naver.com/v1/review.json?product_id={product_id}'
    headers = {
        'X-Naver-Client-Id': CLIENT_ID,
        'X-Naver-Client-Secret': CLIENT_SECRET
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        reviews = response.json()
        return reviews['items']
    else:
        print("리뷰 검색 오류:", response.status_code)
        return None

def display_reviews(reviews):
    if reviews:
        for review in reviews:
            print(f"리뷰: {review['content']}, 평점: {review['rating']}")

if __name__ == "__main__":
    product_id = input("상품 ID를 입력하세요: ")
    reviews = get_product_reviews(product_id)
    display_reviews(reviews)
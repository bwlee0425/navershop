# main.py
import ns  # ns.py 파일을 임포트합니다.

if __name__ == "__main__":
    query = input("검색할 상품명을 입력하세요: ")
    products = ns.search_products(query)  # ns.py의 search_products 함수를 호출
    ns.display_products(products)  # ns.py의 display_products 함수를 호출하여 결과 출력
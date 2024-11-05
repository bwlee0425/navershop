import subprocess

def main():
    query = input("검색할 상품명을 입력하세요: ")

    # search_item.py 실행
    print("상품 검색 중...")
    subprocess.run(['python', 'search_item.py', query])  # search_item.py를 실행하고 검색어 전달

    # trend_anl.py 실행
    print("트렌드 분석 중...")
    subprocess.run(['python', 'trend_anl.py', query])  # trend_anl.py를 실행하고 검색어 전달

if __name__ == "__main__":
    main()
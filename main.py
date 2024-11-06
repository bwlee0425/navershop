# main.py
import streamlit as st
import search_item
import trend_anl
from datetime import datetime

def main():
    st.title("쇼핑 검색 및 트렌드 분석")
    query = st.text_input("검색할 상품명을 입력하세요:")

    if st.button("검색 및 트렌드 분석 실행"):
        if query:
            # 상품 검색 실행
            st.write("상품 검색 중...")
            search_results = search_item.search_products(query)
            formatted_products = search_item.format_products(search_results)
            
            if "error" in search_results:
                st.error(search_results["error"])
            else:
                for product in formatted_products:
                    st.write(f"상품명: {product['상품명']}")
                    st.write(f"가격: {product['가격']}")
                    if "이미지 URL" in product:
                        st.image(product["이미지 URL"], width=150)
                    st.write("---")

            # 트렌드 분석 실행
            st.write("트렌드 분석 중...")
            trend_data = trend_anl.get_recent_trend_data(query)

            # 최근 6개월 데이터 출력
            st.subheader("최근 6개월 데이터")
            six_month_trends = trend_anl.format_trend_results(trend_data["six_month_data"])
            for trend in six_month_trends:
                st.write(f"주제어: {trend['주제어']}")
                st.write(f"키워드: {trend['키워드']}")
                for data in trend['데이터']:
                    st.write(f"날짜: {data['날짜']}, 검색량 비율: {data['검색량 비율']}")
                st.write("---")

            # 최근 1주 데이터 출력
            st.subheader("최근 1주 데이터")
            one_week_trends = trend_anl.format_trend_results(trend_data["one_week_data"])
            for trend in one_week_trends:
                st.write(f"주제어: {trend['주제어']}")
                st.write(f"키워드: {trend['키워드']}")
                for data in trend['데이터']:
                    st.write(f"날짜: {data['날짜']}, 검색량 비율: {data['검색량 비율']}")
                st.write("---")

            # 어제의 데이터 출력
            st.subheader("어제 데이터")
            yesterday_trends = trend_anl.format_trend_results(trend_data["yesterday_data"])
            for trend in yesterday_trends:
                st.write(f"주제어: {trend['주제어']}")
                st.write(f"키워드: {trend['키워드']}")
                for data in trend['데이터']:
                    st.write(f"날짜: {data['날짜']}, 검색량 비율: {data['검색량 비율']}")
                st.write("---")
        else:
            st.warning("상품명을 입력해주세요.")

if __name__ == "__main__":
    main()
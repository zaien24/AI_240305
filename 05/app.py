import streamlit as st
import requests

st.title("면접 질의서 작성 서비스")

generate_ad_slogan_url = "http://localhost:8000/create_ad_slogan"

product_name = st.text_input("나의 History (성장배경/학교생활 등)")
details = st.text_input("나의 KOLON (회사 및 직무 지원 동기)")
options = st.text_input("나의 One&Only (구체적 사례를 통한 자신만의 차별화된 경쟁력)")

if st.button("질의 생성"):
    try:
        response= requests.post(generate_ad_slogan_url,
                    json={"product_name": product_name,
                            "details": details,
                            "tone_and_manner": ', '.join(options)})
        ad_slogan = response.json()['ad_slogan']
        st.success(ad_slogan)
    except:
        st.error("예상치 못한 에러가 발생했습니다")
    

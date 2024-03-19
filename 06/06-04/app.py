import streamlit as st
import requests

summarize_url = "http://localhost:8000/summarize"

def summarize(text):
    response = requests.post(summarize_url, json={"text": text})
    summary = response.json()["summary"]
    return summary

st.title("요약 서비스")
tab1, tab2 = st.tabs(["실시간", "파일 업로드"])

with tab1:
    input_text = st.text_area("여기에 텍스트를 입력하세요", height=300)
    if st.button("요약"):
        if input_text:
            try:
                summary = summarize(input_text)
                st.success(summary)
            except:
                st.error("요청 오류가 발생했습니다")
        else:
            st.warning("텍스트를 입력하세요")

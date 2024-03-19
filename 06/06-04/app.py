import streamlit as st
import requests
import pandas as pd

summarize_url = "http://localhost:8000/summarize"

def summarize(text):
    response = requests.post(summarize_url, json={"text": text})
    summary = response.json()["summary"]
    return summary

def summarize_df(df):
    news_summaries : []
    for news_origin in df['뉴스원문']:
        summary = summarize(news_origin)
        news_summaries.append(summary)
    df['뉴스요약'] - news_summaries
    
    return df
    

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

with tab2:
    uploaded_file = st.file_uploader("Choose a file")

    if uploaded_file:
        st.success("업로드 성공!")
        
        progress_bar = st.progress(0, text="progress")
        
        df = pd.read_excel(uploaded_file)
        
        st.dataframe(df)
        
        new_df = summarize_df(df)
        
        st.dataframe(new_df)
        
        



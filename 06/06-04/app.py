import streamlit as st
import requests
import pandas as pd
import os
import io

summarize_url = "http://localhost:8000/summarize"

def summarize(text):
    response = requests.post(summarize_url, json={"text": text})
    summary = response.json()["summary"]
    return summary

def summarize_df(df):
    global progress_bar
    
    total = len(df)
    news_summaries = []
    
    for i, news_origin in enumerate(df['뉴스원문'], start=1):
        summary = summarize(news_origin)
        news_summaries.append(summary)
        
        progress_bar.progress(i/total, text="progress")
        
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
        
        df = summarize_df(df)
        st.dataframe(df)
        
        file_base_name = os.path.splitext(os.path.basename(uploaded_file.name))[0]
        st.download_button(
            label="Download",
            data=to_excel(df),
            file_name=f"{file_base_name}__summarized.xlsx"
        )
        
        



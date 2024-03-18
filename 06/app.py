import openai
import streamlit as st

openai.api_key = "<YOUR_OPENAI_API_KEY>"

def translate_text_using_text_davinci(text, src_lang, trg_lang):
    response = openai.Completion.create(engine="text-davinci-003", # 175B 
                                        prompt=f"Translate the following {src_lang} text to {trg_lang}: {text}",
                                        max_tokens=200,
                                        n=1,
                                        temperature=1)
    translated_text = response.choices[0].text.strip()
    return translated_text

def translate_text_using_chatgpt(text, src_lang, trg_lang):
    system_instruction = f"assistant는 번역앱으로서 동작한다. {src_lang}을 {trg_lang}으로 적절하게 번역하고 번역된 텍스트만 출력한다."

    messages = [{"role": "system", "content": system_instruction},
                {"role": "user", "content": text}]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages) 
    translated_text = response['choices'][0]['message']['content']
    return translated_text

text = st.text_area("번역할 텍스트를 입력하세요", "")
src_lang = st.selectbox("원본 언어", ["영어", "한국어", "일본어"])
trg_lang = st.selectbox("목표 언어", ["영어", "한국어", "일본어"], index=1)

if st.button("번역"):
    # 번역 함수를 만들어서 (text, src_lang, trg_lang) -> translated_text
    translated_text = translate_text_using_chatgpt(text, src_lang, trg_lang)
    st.success(translated_text)
    
    
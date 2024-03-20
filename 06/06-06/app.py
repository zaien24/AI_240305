import streamlit as st
from streamlit_chat import message
from audiorecorder import audiorecorder


if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    # [{"role": "user", "content": "blahblahblah"},
    #  {"role": "assistant", "content": "blahblahblah"}, ...]

host_url = "http://localhost:8000"
chat_url = f"{host_url}/chat"
transcribe_url = f"{host_url}/transcribe"

def stt(audio_bytes):
    audio_file = io.BytesIO(audio_bytes)
    files = {"audio_file": ("audio.wav", audio_file, "audio/wav")}
    response = requests.post(transcribe_url, files=files)
    text = response.json()['text']
    return text

def chat(text):
    user_turn = {"role": "user", "content": text}
    messages = st.session_state['messages']
    resp = requests.post(chat_url, json={"messages": messages + [user_turn]})
    assistant_turn = resp.json()
    
    st.session_state['messages'].append(user_turn)
    st.session_state['messages'].append(assistant_turn)


st.title("챗봇 서비스")

row1 = st.container()
row2 = st.container()


with row2:
    # input_text = st.text_input("You")
    # if input_text:
    #     chat(input_text)
    
    audio = audiorecorder("Click to record", "Recording...")
    if len(audio) > 0:
        audio_bytes = audio.tobytes()
        st.audio(audio_bytes)

    text = stt(audio_bytes)
    chat(text)

with row1:
    for i, msg_obj in enumerate(st.session_state['messages']):
            msg = msg_obj['content']
            is_user = False
            if i % 2 == 0:
                is_user = True

            message(msg, is_user=is_user, key=f"chat_{i}")   
        
        
        
        
        
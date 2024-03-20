import streamlit as st
from streamlit_chat import message

if 'messages' not in st.session_state:
    st.session_state['messages'] = []
    # [{"role": "user", "content": "blahblahblah"},
    #  {"role": "assistant", "content": "blahblahblah"}, ...]

chat_url = "http://localhost:8000/chat"

st.title("챗봇 서비스")

for i, msg_obj in enumerate(st.session_state['messages']):
        msg = msg_obj['content']
        is_user = False
        if i % 2 == 0:
            is_user = True

        message(msg, is_user=is_user)   
        
        
        
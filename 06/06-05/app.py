import streamlit as st
from streamlit_chat import message

message("this is assistant")
message("this is user", is_user=True)
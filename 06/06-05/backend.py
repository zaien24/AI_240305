from fastapi import FastAPI
from pydantic import BaseModel
import openai

openai.api_key = "<YOUR_OPENAI_API_KEY>"

def chat(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn # {"role": "assistant", "content": "blahblahblah"}

app = FastAPI()

class Turn(BaseModel):
    role: str
    content: str

class Messages(BaseModel):
    messages: List[Turn]  # [{"role": "user", "content": "blahblahblah"}, {"role": "assistant", "content": "blahblahblah"}, ...]
    
@app.post("/chat")
def post_chat(messages: Messages):
    assistant_turn = chat(messages=messages['messages'])
    return assistant_turn

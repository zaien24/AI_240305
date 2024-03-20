import openai

openai.api_key = "<YOUR_OPENAI_API_KEY>"

def chat(messages):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    resp_dict = response.to_dict_recursive()
    assistant_turn = resp_dict['choices'][0]['message']
    return assistant_turn # {"role": "assistant", "content": "blahblahblah"}

messages = [{"role": "user", "content": "너는 누구야"}]

print(chat(messages=messages))
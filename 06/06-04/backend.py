import openai

openai.api_key = "<YOUR_OPENAI_API_KEY>"

def summarize(text):
    system_instruction = "assistant는 user의 입력을 bullet point로 3줄 요약해준다."

    messages = [{"role": "system", "content": system_instruction},
                {"role": "user", "content": text} 
                ]

    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    result = response['choices'][0]['message']['content']
    return result

text = """
신동빈 롯데그룹 회장의 장남인 신유열 전무가 지난해 연말 인사에서 롯데지주 미래성장실을 이끌게 되면서 롯데지주 이사회 내 집행위원회에도 합류한 것으로 확인됐다. 집행위원회는 주로 자회사의 자금 조달을 위한 지급보증이나 제도 도입 등의 안건을 결정하는 기구다. 신 전무가 지난달 사내이사로 선임된 롯데바이오로직스와 더불어 롯데지주의 이사회에서도 입지를 넓히면서 회사 내부 경영을 아우르는 대내외 영향력을 확보했단 평가다.



"""

print(summarize(text))
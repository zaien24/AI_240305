from openai import OpenAI
client = OpenAI(
    api_key="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",
)

chat_completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)
import os
import openai

openai.api_key = "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"

response = openai.Completion.create(model="text-davinci-003",
                                     prompt="Say this is a test",
                                     temperature=0,
                                     max_tokens=7)
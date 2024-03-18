import openai

openai.api_key = "<YOUR_OPENAI_API_KEY>"


class SloganGenerator:
    def __init__(self, engine='gpt-3.5-turbo'):
        self.engine = engine
        self.infer_type = self._get_infer_type_by_engine(engine) # or completion
        
    def _get_infer_type_by_engine(self, engine):
        if engine.startswith("text-"):
            return 'completion'
        elif engine.startswith("gpt-"):
            return 'chat'
        
        raise Exception(f"Unknown engine type: {engine}")
    
    def _infer_using_completion(self, prompt):
        response = openai.Completion.create(engine=self.engine,
                                            prompt=prompt,
                                            max_tokens=200,
                                            n=1)
        result = response.choices[0].text.strip()
        return result
    
    def generate(self, product_name, details, tone_and_manner):
        prompt = f"제품 이름: {product_name}\n주요 내용: {details}\n광고 문구의 스타일: {tone_and_manner} 위 내용을 참고하여 마케팅 문구를 만들어라."
        if self.infer_type == 'completion':
            result = self._infer_using_completion(prompt=prompt)
    
        return result
    
slogan_generator = SloganGenerator("gpt-3.5-turbo")
result = slogan_generator.generate(product_name="나이키 신발", details="예쁘고 편안합니다", tone_and_manner="과정")
print(result)
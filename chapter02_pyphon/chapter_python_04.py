"""
모듈과 패키지
모듈: 하나의 파이썬 파일, 이 파일에 들어있는 다른 함수나, 클래스, 변수들을 가져와서 사용할 수가 있습니다.
패키지: 모듈들을 묶어놓은 폴더
"""

# import overwatch as ow
# from overwatch import test_function 

# overwatch.test_function()

# ow.test_function()

# test_function()

# print(ow.get_hp_by_character("genji"))
# print(ow.hp_by_character)

# from game.user import User

# user = User(username="python", rank="gold")
# user.print_info()

from game.user as u 

user = u.User(username="python", rank="gold")
user.print_info()

    """예외 처리
    """
    
    try:
        print(1/0)
    
    except:
        print("error occur!")
        
    print("here here")        



    try:
        print(1/0)
    
    except Exception as e:
        print(f"error occur!, {e}")
        
    print("here here")        


"""
표준 라이브러리
"""
import json
import glob
import datetime

a = {"genji": 200, "doomfist": 450}

with open("./hp_by_character.json", "wt") as f:
    json.dump(a, f)
    
    
"""
외부 라이브러리

pandas, requests, tqdm
"""    

a = {"name": ["genji", "para", "doomfist"],
     "hp": ["200", "200", "450"] }

a_df = pd.DataFrame(a)

print(a_df)

a_df.to_excel("./overwatch.xlsx")



"""
가상환경
여러 프로젝트에 사용되는 라이브러리들이 다를 수 있고, 같더라고 그 버전이 다를 수 있습니다.

"""



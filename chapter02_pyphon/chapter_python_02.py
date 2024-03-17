# if, for, while
import random
target = random.randint(1,5)


# true
condition = 2 > 1
print(condition)
print(type(condition))

if 2 > 1 :
    print("here")
    

n = 2

if n == 10:
    print("top")        
elif n == 5:    
    print("middle")    
else:
    print("bottom")
    
guess = int(input("숫자를 입력하세요"))    


# for 문
for i in range(10):
    print("안녕")    
    
print(list(range(10)))    


for i in [0,1,2,3,4,5,6,7,8,9]:
    print("안녕")
    
    
import random
target = random.randint(1,10)    


while True:
    guess = int(input("숫자를 입력하세요"))
    if guess == target:
        print("정답 입니다.")
        break
    elif guess < target:
        print("target은 좀 더 큰 숫자입니다")
    elif guess > traget:
        print("target은 좀 더 작은 숫자입니다")
        
        

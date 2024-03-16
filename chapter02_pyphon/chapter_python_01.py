# 자료형과 변수 
# int, float, str, list, tuple, set, dict
# comment, 주석

print(1)

#a = "오늘"
#b = input("오늘 날씨는 얼마야?")

#print(f"{a}의 날씨는 {b}도입니다.")
#print("{a}의 날씨는 {b}도입니다.".format(a=a, b=b))


# list
#idx 0 1 2 3
a = [1,2,3,4]

print(a)

# indexing, slicing
print(a[2])

# 2,3
print(a[1:3])
# 2,3,4
print(a[1:])
# 1,2
print(a[:-2])  

# tuple
a = ["오늘", "내일", "모래"]
b = ("오늘", "내일", "모래")

print(a)
a[1] = "XX"
print(a)

print(b)
b[1] = "XX"
print(b)

# set 
a = {1,2,3,1,2}
a = set([1,2,3,1,2])

printa(a)
a.add(10)
print(a) 

#list
a = [1,2,3,1,2]

print(a)
a.append(10)
print(a)
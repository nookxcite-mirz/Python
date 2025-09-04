#프로그램  핵심 개념 in Python : 추상화/제어문

#Comment
print('Goodbye world!') #Comment

buger_price = 4990
print(buger_price*3) #Comment

# 함수 만들기.
def hello(name):
    print("Hello!")
    print(name)
    print("Welcome to Code!")

hello("Chris")

def add(a,b):
    return a+b

print(add(3,5))

print(2**3)     #2의 거듭제곱 3
print(4+7)
print(4.0+7.0)
print(4+7.0)    #소수형 으로 나옴
print(4/2)      #나누기는 모두 소수형

# 옵셔널 파라미터
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))

myself("코드잇", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("코드잇", 1)         # 옵셔널 파라미터를 제공하지 않는 경우

def myName(name):
    print("내 이름은 {}".format(name))

myName( "Cherry ")

#상수는 대문자로 사용하여 코드 구분을 한다.
PI = 3.14   #원주율  '파이'

#while 조건부분:
#    수행 부분

#while 조건부분:
#    if 조건부분:
#		break
#	if 조건부분:
#		continue

#if 조건부분:
#	수행 부분
#else:
#	수행 부분

#if 조건부분 or 조건부분:
#	수행 부분
#elif 조건부분:
#	수행 부분
#else:
#	수행부분




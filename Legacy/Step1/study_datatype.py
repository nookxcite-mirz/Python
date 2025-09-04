# 프로그래밍 기초 in Python > Chapter2 프로그램 핵심 개념 in Python
# 자료형

# 연산자
# +(덧셈), -(뺄셈), *(곱셈), /(나눗셈), %(나머지), **(거듭제곱), //(버림 나눗셈:floor division)
# 나눗셈은 모두 소수형 으로 결고값 반환.

print(round(3.141526535))       # 반올림, 자릿수
print(round(3.141526535, 2))

#문자열 '문자열' == "문자열" 동일한 기능

print("문자열"+'문자열')
print("문자열"*3)
print("I'm a boy'")
print("I\'m \"excityed\" to learn study")

# 형변환
# python 자료형은 정수,소수, 문자열 로 이루어짐.
print(int(3.8))             # 잘림
print(float(3))
print(int("2")+int("5"))
print(float("2.3")+float("5.2"))
print(str(2) + str(3.5))
age = 18
print("제 나이는 " + str(age) + "살 입니다.")

year = 2021
month = 2
day = 1
print("Today is "+ str(year) + ":" + str(month) + ":" + str(day))
print("Today is {}:{}:{}".format(year, month, day))
tomorrow = "tomorrow is {}:{}:{}"
print(tomorrow.format(year, month, day+1))
print("Today is {2}:{1}:{0}".format(year, month, day))

num_1=1
num_2=3
print("{0}/{1}={2:.0f}".format(num_1, num_2, num_1/num_2))  # 정수
print("{0}/{1}={2:.2f}".format(num_1, num_2, num_1/num_2))  # 소수점 2째자리 반올림
print("{}/{}={:.4f}".format(num_1, num_2, num_1/num_2))  # 소수점 2째자리 반올림

name= "홍길동"
age = 32
print("제이름은 %s이고, %d살 입니다." % (name, age))          # %포멧 사용, c++(옛 방식)
print("제이름은 {}이고, {}살 입니다.".format(name, age))     # foramt 메소드
print(f"제이름은 {name}이고, {age}살 입니다.")                # f-string 방식

# 불 대수 (진리값)
# AND OR NOT
print(True)
print(False)

print(not True)
print(not False)

print(True and True)
print(True and False)
print(False and True)
print(False and False)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# type 자료형
def hello():
    print("hello world!")

print(type(3))
print(type(3.0))
print(type("3"))
print(type(True))
print(type(hello))      #사용자 함수 타입
print(type(print))      #내장함수 타입

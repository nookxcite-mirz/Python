def fibonacci(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(8):
    print(fibonacci(i))

# 실행 > Python 1.2.4.fibonacci.py

# 복소수
print(1.2 + 4.2j + 2.3 + 4.1j) 
[1,2,3]    # list
(1,2,3)    # tuple
range(10)  # range
{'one' , 'two' , 'three'} # set
{'one':1 , 'two':2 , 'three':3 } # dict

# 리스트와 튜플이 차이, 리스트는 요소 추가 가능, 튜플는 요소 변경 불가

# 조건문
a = 10
if 10 < a < 20:
    print('a is between 10 and 20')
else:    
    print('a is not between 10 and 20')
    
# 반복문
for i in range(10):
    print(i, end=" ")
print("")
for i in range(3,9):
    print(i, end=" ")
print("")
for i, e in enumerate([5,3,7]): # 열거혈으로 출력
    print(i, e, end=" ")
print("")

data = []
for i in range(10):
    data.append(i)
print(data)

data = [i for i in range(10) if i%2 ==0]        # 리스트 내포문 if
data = [i if i%2==0 else 0 for i in range(10)]  # 리스트 내포문 if...else
print(data)

# 반복문 while
i = 0
while i < 10:
    print(i, end=" ")
    i += 1

# 함수
def functionName(param1, param2):
    print(param1, param2)
    return param1 + param2
print (functionName(1,2))

# 함수 인자는 가변형과 불변형으로 나뉘며,
# 불변형은 숫자, 문자열, 튜플등으로 값에 의한 전달이 되고, 가변형 list, dic, set등은 참조에 의한 전달 된다.
# Scope 가 없어 if, for등에 선언된 변수도 접근 가능, 변경 불가능
# 전역 변수와 지역변수는 이름이 같아도 다르게 처리됨 (global x 처럼 전역변수로 선언가능)

# Class
class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age

user = User('이재성', 20)
print(user.name)
print(user.age)
print(user.getName())
print(user.getAge())

# 상속
class Student(User):
    def __init__(self, name, age, major):
        super().__init__(name, age)
        self.major = major
    def getMajor(self):
        return self.major





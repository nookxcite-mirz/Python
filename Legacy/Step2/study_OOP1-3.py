# 객체 지향 프로그래밍 : Topic1 - 객체 지향 프로그램 이란?
# chapter3 - 미리 알아야할 것들

# -------------------------------------------------------
# 순수 객체 지향 언어
# -------------------------------------------------------

print(type(1))
print(type(1.0))
print(type("1"))
print(type(()))     # tuple - 유한 순서 목록 (시퀀스)
print(type([]))
print(type({}))

def print_hello():
    pass

print(type(print_hello))

class User:
    pass

user1 = User()
print(type(User))
print(type(user1))

# 가변 vs 불변 Type
# - 가변 타입 : list, dict
mutable_obj = [1,2,3]
mutable_obj[0] = 4
print(mutable_obj)

# - 불변 타입 : bool, int, float, str, tuple
immutable_obj = (1,2,3)     # 튜플은 불변타입 객체임
#immutable_obj[0]  = 4       # error
immutable_obj = (5,6,7,8)   # 새로 정의는 가능 (변경은 불가능)


# -------------------------------------------------------
# 유요한 함수들
# -------------------------------------------------------

# - max, min 함수
print(max(2, 5))             # => 5
print(max(2, 7, 5))          # => 7
print(min(2, 5))             # => 2
print(min(2, 7, 5, 11, 6))   # => 2

# - sum 함수
int_list = [1, 2, 3, 4, 5]
int_tuple = (4, 3, 6, 1, 2)
int_dict = {1: "one", 2: "two", 3: "three"}

print(sum(int_list))    # => 15
print(sum(int_tuple))   # => 16
print(sum(int_dict))    # => 6    key들의 합을 return 한다.

# - 불린(Boolean) 값에 따라 다른 값을 리턴하는 구문 : ternary expression
def func_normal():
    condition = True
    if condition:
        condition_string = "nice"
    else:
        condition_string = "not nice"
    print(condition_string)  # => nice

def func_ternary():
    condition = True
    condition_string = "nice" if condition else "not nice"      # condition 조건을 중심으로 좌/우로 배치됨.
    print(condition_string)  # => nice

# - list comprehension : 새로운 리스트를 만드는 간편한 방법
def func_list():
    int_list = [1, 2, 3, 4, 5, 6]
    squares = []
    for x in int_list:
        squares.append(x ** 2)
    print(squares)  # [1, 4, 9, 16, 25, 36]

#> [] 안에 원하는 값을 리턴하는 식 (x**2) 뒤에 for문을 써줍니다 (for x in int_list).
def func_listcomp():
    int_list = [1, 2, 3, 4, 5, 6]
    squares = [x ** 2 for x in int_list]
    print(squares)  # [1, 4, 9, 16, 25, 36]

# - zfill 메소드
print("1".zfill(6))            # 000001
print("333".zfill(2))          # 333
print("a".zfill(8))            # 0000000a
print("ab".zfill(8))           # 000000ab


# -------------------------------------------------------
# 모듈
# -------------------------------------------------------
from [모듈의 이름] import [불러올 변수/함수/클래스 이름]

#ex> from calculator import sum, difference, product, square        > 필요한 부분만
#ex> from calculator import *                                       > 모두


# - randint 함수와 uniform 함수
from random import randint
# 1 <= N <= 20를 만족하는 랜덤한 정수(난수) N을 리턴한다.
x = randint(1, 20)
print(x)

from random import uniform
# 0 <= N <= 1을 만족하는 랜덤한 소수(난수) N을 리턴한다.
x = uniform(0, 1)
print(x)
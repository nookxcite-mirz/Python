# 객체 지향 프로그래밍 : Topic1 - 객체 지향 프로그램 이란?
# chapter2 - 객체를 만드는법

### https://wikidocs.net/book/1   ### 점프 투 파이쎤 e-book
### 파이보 (https://pybo.kr)       ### 파이썬 봇  Q&A

# 객체란 : 속성 + 행동
# 객체지향적인 설계 : 모델링

# 객체 지향 프로그래밍의 4가지
# - Chapter 1: 추상화(Abstraction)
# - Chapter 2: 캡슐화(Encapsulation)
# - Chapter 3: 상속(Inheritance)
# - Chapter 4: 다형성(Polymorphism)

# 견고한 객체 지향 프로그래밍: SOLID 원칙
# - Chapter 1: 단일 책임 원칙 (Single Responsibility Principle)
# - Chapter 2: 개방 폐쇄 원칙 (Open-closed Principle)
# - Chapter 3: 리스코프 치환 원칙 (Liskov Substitution Principle)
# - Chapter 4: 인터페이스 분리 원칙 (Interface Segregation Principle)
# - Chapter 5: 의존 관계 역전 원칙 (Dependency Inversion Principle)

# 객체의 틀 : Class, 만들어진 객체 : Instance

class User:
    pass        # 아무내용 없음

user1 = User()
user2 = User()
user3 = User()

# ---------------------------------------------------------------
# 변수
# ---------------------------------------------------------------

# 인스턴스 변수 name, email, password
user1.name = "김대위"
user1.email = "captain@gmail.com"
user1.password = "1234"
print(user1.email)

user2.name = "나상사"
user2.email = "sangsa@gmail.com"
user2.password = "1234"
print(user2.password)

user3.name = "다람쥐"
user3.email = "squrrel@gmail.com"
user3.password = "1234"
print(user3.name)


# 클래스 변수  (static member value)
class UserMV:
    count = 0       # 클래스 변수 생성 - 인스턴스 객체 갯수 파악

    # 생성시 호출되는 함수
    def __init__(self, name, email, password):
        # 특수메소드(생성시 자동 호출됨)
        self.name = name
        self.email = email
        self.password = password
        UserMV.count += 1

userMV1 = UserMV("A", "A@none.kr", "1234")
userMV2 = UserMV("B", "B@none.kr", "1234")
userMV3 = UserMV("C", "C@none.kr", "1234")

userMV2.count = 10      # 인스턴스 변수 생성 (변경 필요시, UserMV.count = 10 으로 사용해야 함.)

print(UserMV.count)
print(userMV1.count)
print(userMV2.count)
print(userMV3.count)



# ---------------------------------------------------------------
# 메소드
# ---------------------------------------------------------------

# 메소드(함수) 종류 - 인스턴스 메소드 : 첫번째 파라미터는 self로 사용함 (암묵적 규약)
class UserInst:
    def initialize(self, in_name, in_email, in_password):
        # 인스턴스 변수 초기화
        self.name = in_name
        self.email = in_email
        self.password = in_password
        print(f"{self.name} {self.email} {self.password}")

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def login(self, in_email, in_password):
        # 로그인 시도
        if self.email == in_email and self.password == in_password :
            print("로그인 성공")
        else:
            print("로그인 실패")

    def  check_name(self, name):
        # 파라미터로 받는 name이 유저의 이름과 같은지 판단
        return self.name == name

user5 = UserInst()
user5.name = "오징어"
user5.email = "ojinga@gmail.com"
user5.password = "1234"

UserInst.say_hello(user1)   # 클래스 메소드 호출
UserInst.say_hello(user2)
UserInst.say_hello(user3)
user5.say_hello()           # 인스턴스 메소드의 특징 (첫번째 파라미터에 자신을(self) 자동으로 넣어줌)
UserInst.login( user1, "captain@gmail.com", "1234")
user5.login( "ojinga@gmail.com", "123" )
print( user5.check_name("오징어"))

# 생성, 초기화 > 속성값 모두 설정됨.
user6 = UserInst()
user6.initialize("Young", "young@codeit.kr", "123456")

# __init__ 특수함수 사용
class UserInit:
    def __init__(self, name, email, password):          # 생성시 호출되는 함수 - 기본으로 정의함.
        # 특수메소드(생성시 자동 호출됨)
        self.name = name
        self.email = email
        self.password = password

user7 = UserInit("Taeho", "Taeho@codeit.kr", "123456")
print( user7.name )


# instagam following, follower
class UserInsta:
    # 인스턴스 변수 설정
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트

    # 팔로우
    def follow(self, another_user):
        # 코드를 입력하세요
        if another_user.name not in self.following_list:
            self.following_list.append(another_user.name)
        if self.name not in another_user.followers_list:
            another_user.followers_list.append(self.name)

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        # 코드를 입력하세요
        return len(self.following_list)

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        # 코드를 입력하세요
        return len(self.followers_list)

    # print 함수 호출시 자동으로 호출됨
    def __str__(self):
        return "사용자:{}, 이메일:{}, 비전:{} type:{}".format(self.name, self.email, self.password, type(self))

# instagam 예제
# ---------------------------------------------------------------
# instagam - 유저들 생성
userinsta1 = UserInsta("Young", "young@codeit.kr", "123456")
userinsta2 = UserInsta("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
userinsta3 = UserInsta("Taeho", "taeho@codeit.kr", "123abc")
userinsta4 = UserInsta("Lisa", "lisa@codeit.kr", "abc123")

# instagam - 유저마다 서로 관심 있는 유저를 팔로우
userinsta1.follow(userinsta2)
userinsta1.follow(userinsta3)
userinsta2.follow(userinsta1)
userinsta2.follow(userinsta3)
userinsta2.follow(userinsta4)
userinsta4.follow(userinsta1)

# instagam - 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(userinsta1.name, userinsta1.num_followers(), userinsta1.num_following())
print(userinsta2.name, userinsta2.num_followers(), userinsta2.num_following())
print(userinsta3.name, userinsta3.num_followers(), userinsta3.num_following())
print(userinsta4.name, userinsta4.num_followers(), userinsta4.num_following())

print(user1)
print(userinsta1)


# 메소드(함수) 종류 - 클래스 메소드

class UserCM:       # classMethos
    count = 0

    # 생성시 호출되는 함수
    def __init__(self, name, email, password):
        # 특수메소드(생성시 자동 호출됨)
        self.name = name
        self.email = email
        self.password = password
        UserCM.count += 1

    def say_hello(self):
        # 인사 메세지 출력 메소드
        print("안녕하세요! 저는 {}입니다!".format(self.name))

    def __str__(self):
        return "사용자:{}, 이메일:{}, 비전:{} type:{}".format(self.name, self.email, self.password, type(self))

    # 인스턴스 변수를 접근 할수 없다. 인스턴스가 없더라도 호출될 수 있다.
    @classmethod
    def number_of_user(cls):            # 첫번째 파라미터에 class로 자동 전달 (파이썬 규약)
        print("총 유저 수는 : {}입니다".format(cls.count))

    @classmethod
    def from_string(cls, string_params):
        parameter_list = string_params.split(",")     # split 메소드를 사용해서 쉼표(,)를 기준으로 문자열을 리스트로 분리한다
        return cls(parameter_list[0], parameter_list[1], parameter_list[2])

    @classmethod
    def from_list(cls, list_params):
        return cls(list_params[0], list_params[1], list_params[2])

    # 메소드(함수) 종류 - 정적 메소드, cls, self 가 없는 독립적인 함수.
    @staticmethod
    def is_valid_email(email_address):
        return "@" in email_address

userCm1 = UserCM("Young", "young@codeit.kr", "123456")
userCm2 = UserCM("Yoonsoo", "yoonsoo@codeit.kr", "abcdef")
userCm3 = UserCM("Taeho", "taeho@codeit.kr", "123abc")

# 클래스 메소드 사용.
UserCM.number_of_user()
userCm1.number_of_user()

younghoon = UserCM.from_string("강영훈,younghoon@codeit.kr,123456")
yoonsoo   = UserCM.from_list(["이윤수", "yoonsoo@codeit.kr", "abcdef"])

print(younghoon.name, younghoon.email, younghoon.password)
print(yoonsoo.name, yoonsoo.email, yoonsoo.password)



# ---------------------------------------------------------------
# 데코레이터
# ---------------------------------------------------------------

# 데코레이터 함수
def deco_print_to(original):
    def wrapper():
        print("함수 시작")       # 꾸밈 추가
        original()
        print("함수 끝")         # 꾸밈 추가
    return wrapper              # 함수 리턴

def print_hello1():
    print("안녕하세요!")

@deco_print_to                  # 데코레이터 적용 (새로운 기능 추가)
def print_hello2():
    print("안녕하세요!")

deco_print_to(print_hello1)()     # add_print_to(print_hello) == wrapper >>> wrapper()
print_hello1 = deco_print_to(print_hello1)
print_hello1()                   # 함수 재정의 호출

print_hello2()

# 객체 지향 프로그래밍 : topic2 객체 지향 프로그래밍의 4개의 기둥

""" -------------------------------------------------------------------
# - chapter1: 추상화
#   : 필수적인 정보(사용에 꼭 필요한 부분)를 제외한 세부사항을 숨기는 처리
"""

"""
문서화 문자열 (DocString).
"""

class BankAccount:
    """ 은행 계좌 """
    interest = 0.02

help(BankAccount)
help(list)

# 파이썬은 동적 type 언어이며 java, c++, c# 등은 정적 type 언어.
# 동적 type 언어의 문제 parameter등의 type이 무엇인지 몰라 어떤 값을 넣어야 할지 모호함.

# 	<python 3.5 이상부터 지원됨>
#	typehinting 사용시 적용된 타입과 다른 값을 넣을 경우 run에는 문제가 없으나, warning에 노출됨.
#	변수 > interest: float = 0.02
#	리턴 > def aaa(self, amout: float ) -> None:

""" -------------------------------------------------------------------
- chapter2: 캡슐화
    : 클래스 내부의 속성을 외부로부터 숨길 수 있다
        - 일부 구현 내용에 대한 외부 직접 액세스 차단 (멤버 변수 및 함수에 "__" 붙여서 외부 접근 금지 시킴 : private, protected)
        - 속성과 그것을 사용하는 행동을 하나로 묶는 것
"""
class Citizen:
    """주민 클래스"""
    drinking_age = 19 # 음주 가능 나이

    def __init__(self, name, age, resident_id):
        """이름, 나이, 주민등록번호"""
        self.name = name
        self.set_age(age)
        self.__resident_id = resident_id    # 액세스 접근 금지 private

    def authenticate(self, id_field):
        """본인이 맞는지 확인하는 메소드"""
        return self.__resident_id == id_field

    def can_drink(self):
        """음주 가능 나이인지 확인하는 메소드"""
        return self._age >= Citizen.drinking_age

    def __str__(self):
        """주민 정보를 문자열로 리턴하는 메소드"""
        return self.name + "씨는 " + str(self._age) + "살입니다!"

    def get_age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self._age

    def set_age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다")
            self._age = 0
        else:
            self._age = value

    @property           # property 데코레이션을 사용한 캡슐화.
    def age(self):
        """숨겨 놓은 인스턴스 변수 __age의 값을 받아오는 메소드"""
        return self._age

    @age.setter
    def age(self, value):
        """숨겨 놓은 인스턴스 변수 __age의 값을 설정하는 메소드"""
        if value < 0:
            print("나이는 0보다 작을 수 없습니다. 기본 값 0으로 나이를 설정하겠습니다")
            self._age = 0
        else:
            self._age = value

"""
파이썬에서는 변수나 메소드 이름 앞에 밑줄 2개(__)가 있더라도 이름 뒤에도 밑줄 2개(__)가 있으면 일반 변수나 메소드처럼 클래스 밖에서도 접근할 수 있습니다.
 메소드 이름 앞 뒤에 밑줄 2개가 있으면 파이썬이 정한 특수한 상황에서 자동으로 실행되는 "특수 메소드"를 나타낸다고 배웠습니다."""

# 시민 인스턴스 생성
young = Citizen("younghoon kang", 15, "87654321") # (1) Citizen 클래스로 young이라는 인스턴스를 하나 생성
print(dir(young))                                 # (2) dir 라는 함수를 사용하면 인스턴스가 갖고 있는 모든 변수와 메소드를 볼 수 있음

print(young.age)    # getter
young.age = 30      # setter
print(young.age)    # getter

"""
result > ['_Citizen__age', '_Citizen__resident_id', '__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'authenticate', 'can_drink', 'drinking_age', 'get_age', 'name', 'set_age']
  변수나 메소드 이름 앞에 밑줄 두 개(__)를 쓰면, 파이썬은 그 앞에 추가적으로 "_클래스 이름" 을 덧붙여서 이름을 바꿔버림 > 맹글링
  사실 파이썬은 언어 차원에서 캡슐화를 지원하지 않습니다. 캡슐화처럼 보이긴 하지만 알고보면 완벽한 캡슐화는 아닙니다.
  개발자들끼리의 암묵적인 규약으로 변수 및 함수 앞에 _ 하나를 붙이면 private 라고 생각하면 된다. 
  """

class CreditCard:
    MAX_PAYMENT_LIMIT = 30000000

    # 모든 인스턴스 변수를 _를 통해서 외부 접근을 막는다
    def __init__(self, name, password, payment_limit):
        self.name = name
        self._password = password
        self._payment_limit = payment_limit

    @property
    def password(self):
        return "비밀 번호는 볼 수 없습니다"

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def payment_limit(self):
        return self._payment_limit

    @payment_limit.setter
    def payment_limit(self, new_payment_limit):
        if new_payment_limit >= 0 and new_payment_limit <= CreditCard.MAX_PAYMENT_LIMIT:
            self._payment_limit = new_payment_limit
        else:
            print("카드 한도는 0원 ~ 3천만 원 사이로 설정해주세요!")

card = CreditCard("강영훈", "123", 100000)

print(card.name)
print(card.password)
print(card.payment_limit)

card.name = "성태호"
card.password = "1234"
card.payment_limit = -10

print(card.name)
print(card.password)
print(card.payment_limit)


""" -------------------------------------------------------------------
- chapter3: 상속
"""






""" -------------------------------------------------------------------
- chapter4: 다형성
"""

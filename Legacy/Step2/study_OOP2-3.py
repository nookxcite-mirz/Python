"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic2 객체 지향 프로그래밍의 4개의 기둥
- chapter3 : 상속
"""

# buildtins.object : 최상위 부모

class Employee:
    """직원 클래스"""
    raise_percentage = 1.03
    company_name = "코드잇 버거"

    def __init__(self, name, wage):
        """인스턴스 변수 설정"""
        self.name = name
        self.wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self.wage *= Employee.raise_percentage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    pass

class Manager(Employee):
    pass

class DeliveryMan(Employee):
    """배달원 클래스"""
    raise_percentage = 1.05

    def __init__(self, name, wage, on_standby=True):
        super().__init__(name, wage)
        self.on_standby = on_standby

    def raise_pay(self):
        """시급을 인상한다"""
        self.wage *= self.raise_percentage

    def deliver(self, address):
        """배달원이 대기 중이면 주어진 주소로 배달을 보내고 아니면 메시지를 출력한다"""
        if self.on_standby:
            print(address + "로 배달 나갑니다!")
            self.on_standby = False
        else:
            print("이미 배달하러 나갔습니다!")

    def back(self):
        """배달원 복귀를 처리한다"""
        self.on_standby = True

    def __str__(self):
        return DeliveryMan.company_name + " 배달원: " + self.name


young = Cashier("홍길동", 88900)

# Method resolution oder: 상속 관계 보여줌.
help(young)

# 상속 관계를 보여줌. (Method Resolution Order:메소드 검색 순서) : 오버라이딩 지원.
# 	- mro : 클래스가 상속받은 부모 클래스들의 순서가 담긴 리스트 리턴
print(Cashier.mro())

"""isinstance 함수
isinstance 함수는 어떤 인스턴스가 주어진 클래스의 인스턴스인지를 알려줍니다. isinstance 함수의
	1. 첫 번째 파라미터에는 검사할 인스턴스의 이름
	2. 두 번째 파라미터에는 기준 클래스의 이름 """

print(isinstance(young, Cashier))  # 출력: True
print(isinstance(young, DeliveryMan))  # 출력: False
print(isinstance(young, Employee))  # 출력: True

""" issubclass 함수
issubclass 함수는 한 클래스가 다른 클래스의 자식 클래스인지를 알려주는 함수입니다.
	1. 첫 번째 파라미터로 검사할 클래스의 이름
	2. 두 번째 파라미터에는 기준이 되는 부모 클래스의 이름"""

print(issubclass(Cashier, Employee))  # 출력: True
print(issubclass(Cashier, object))  # 출력: True
print(issubclass(Manager, Employee))  # 출력: True
print(issubclass(Employee, list))  # 출력: False


# 다중 상속
#	- 다중 상속일 경우, 다중 부터가 같은 함수를 가지고 있을 경우, 어떤 함수가 호출될지 모호하다.
#	- mro() 로 어떤 함수가 호출될지 확인은 가능하다.

class Engineer:
    def __init__(self, favorite_language):
        self.favorite_language = favorite_language

    def program(self):
        print("{}으로 프로그래밍 합니다".format(self.favorite_language))


class TennisPlayer:
    def __init__(self, tennis_level):
        self.tennis_level = tennis_level

    def play_tennis(self):
        print("{} 반에서 테니스를 칩니다.".format(self.tennis_level))


class EngineerTennisPlayer(Engineer, TennisPlayer):
    def __init__(self, favorite_language, tennis_level):
        Engineer.__init__(favorite_language);
        TennisPlayer.__init__(tennis_level);

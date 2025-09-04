"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic3 견고한 객체 지향 프로그래밍
- chapter2 : 개방 폐쇄 원칙 (Open-Closed Principle)

    - 클래스는 확장에는 열려있어야 하며, 수정에는 닫혀있어야 한다. (기존 코드 수정 없이도 확장이 가능하도록 개발)
    - 추상 클래스(abstract class)를 사용을 통해 인터페이스등을 제공한다.
"""


"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic3 견고한 객체 지향 프로그래밍
- chapter3 : 리스코프 치환 원칙 (Liskov Substitution Principle)

    - 부모 클래스의 인스턴스를 사용하는 위치에 자식 클래스의 인스턴스를 사용해도 원래 의도대로 동작해야 한다.
    - isinstance(자식 클래스 인스턴스, 부모클래스 인스턴스) => True
    - 보모 클래스의 행동 규약을 자식 클래스가 어기면 안된다.
        type1. 자식이 부모의 변수의 타입및 함수 파라미터, 리턴값을 변경하여 오버라이딩 하면 안됨
        type2. 자식이 부모의 의도와 다르게 함수를 오버라이딩 하면 안됨
"""

# Type1 ----------------------------------------------------------------------------
class Employee:
    """직원 클래스"""
    company_name = "코드잇 버거"
    raise_percentage = 1.03

    def __init__(self, name, wage):
        self.name = name
        self._wage = wage

    def raise_pay(self):
        """직원 시급을 인상하는 메소드"""
        self._wage *= self.raise_percentage

    @property
    def wage(self):
        return self._wage

    def __str__(self):
        """직원 정보를 문자열로 리턴하는 메소드"""
        return Employee.company_name + " 직원: " + self.name


class Cashier(Employee):
    """리스코프 치환 원칙을 지키지 않는 계산대 직원 클래스"""
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def raise_pay(self, raise_amount):          # < error1. 부모 함수의 오버라이딩시 파라미터를 변경해 버럼.
        """직원 시급을 인상하는 메소드"""
        self.wage += self.raise_amount

    @property
    def wage(self):
        return "시급 정보를 알려줄 수 없습니다"      # < error1. 부모 함수의 오버라이딩시 리턴를 변경해 버럼.


class Cashier2(Employee):
    """계산대 직원 클래스"""
    raise_percentage = 1.05
    burger_price = 4000

    def __init__(self, name, wage, number_sold=0):
        super().__init__(name, wage)
        self.number_sold = number_sold

    def take_order(self, money_received):
        """손님이 낸 돈을 받아 주문 처리를 하고 거스름돈을 리턴한다"""
        if Cashier.burger_price > money_received:
            print("돈이 충분하지 않습니다. 돈을 다시 계산해서 주세요!")
            return money_received
        else:
            self.number_sold += 1
            change = money_received - Cashier.burger_price
            return change

    def __str__(self):
        return Cashier.company_name + " 계산대 직원: " + self.name


# Type2 ----------------------------------------------------------------------------
class Rectangle:
    """직사각형 클래스"""

    def __init__(self, width, height):
        """세로와 가로"""
        self.width = width
        self.height = height

    def area(self):
        """넓이 계산 메소드"""
        return self.width * self.height

    @property
    def width(self):
        """가로 변수 getter 메소드"""
        return self._width

    @width.setter
    def width(self, value):
        """가로 변수 setter 메소드"""
        self._width = value if value > 0 else 1

    @property
    def height(self):
        """세로 변수 getter 메소드"""
        return self._height

    @height.setter
    def height(self, value):
        """세로 변수 setter 메소드"""
        self._height = value if value > 0 else 1

# 정사각형은 직사각형의 행동 규약을 지킬 수 없으므로 상속을 하면 안됨. class Square(Rectangle): > class Square:
class Square:
    def __init__(self, side):
        self._side = side

    def area(self):
        """넓이 계산 메소드"""
        return self._side * self._side

    @property
    def side(self):
        """가로 변수 getter 메소드"""
        return self._side

    @side.setter
    def side(self, value):
        """"가로 변수 setter 메소드"""
        self._side = value if value > 0 else 1

rect_1 = Rectangle(4, 6)
rect_1.width = 3
rect_1.height = 7
print(rect_1.area())

squr_2 = Square(2)
squr_2.side = 7
print(squr_2.area())

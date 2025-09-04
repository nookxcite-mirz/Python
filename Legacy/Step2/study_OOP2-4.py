"""
------------------------------------------------------------------
- 객체 지향 프로그래밍 : topic2 객체 지향 프로그래밍의 4개의 기둥
- chapter4 : 다형성
	: 하나의 변수가 여러가지 type을 가질수 있는 특징, 추상클래스 지원
"""

from math import pi, sqrt
from abc import ABC, abstractmethod  # ABC (Abstract Base Class)


# 다형성의 성립위 위한 추상 클래스 지원. isinstance() 사용
class Shape(ABC):
    """도형 클래스"""
    @abstractmethod
    def area(self) -> float:
        """도형의 넓이를 리턴한다. 자식 클래스가 알아서 오버라이딩 하세요."""
        print("도형의 넓이 계산 중!")   # ---------------- 추가된 코드

    @abstractmethod
    def perimeter(self) -> float:
        """도형의 둘레를 리턴한다. 자식 클래스가 알아서 오버라이딩 하세요."""
        pass

    def larger_than(self, shape):
        """해당 인스턴스의 넓이가 파라미터 인스턴스의 넓이보다 큰지를 불린으로 나타낸다"""
        return self.area() > shape.area()

    def __str__(self):
        return "추상 클래스라고 해서 모든 메소드가 추상 메소드일 필요는 없습니다!"

    """getter 메소드이자 추상 메소드"""
    @property
    @abstractmethod
    def x(self):
        """도형의 x 좌표 getter 메소드"""
        return self._x

    """getter 메소드이자 추상 메소드"""
    @property
    @abstractmethod
    def y(self):
        """도형의 y 좌표 getter 메소드"""
        return self._y

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @y.setter
    def x(self, value):
        """_x setter 메소드"""
        self._y = value


class EquilateralTriangle(Shape):
    """정삼각형 클래스"""
    def __init__(self, x, y, side):
        self._x = x
        self._y = y
        self.side = side

    def area(self):
        """정삼각형의 넓이를 리턴한다"""
        return sqrt(3) * self.side * self.side / 4

    def perimeter(self):
        """정삼각형의 둘레를 리턴한다"""
        return 3 * self.side

    @property
    def x(self):
        """_x getter 메소드"""
        return self._x

    @x.setter
    def x(self, value):
        """_x setter 메소드"""
        self._x = value

    @property
    def y(self):
        """_y getter 메소드"""
        return self._y

    @y.setter
    def y(self, value):
        """_y setter 메소드"""
        self._y = value

##  제곱 a^n  > a ** n,  math.pow(a,n)
##  루트 a루트 > a ** 0.5, math.sqrt(a)

class RightTriangle(Shape):
    """직각삼각형 클래스"""
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직각삼각형의 넓이를 리턴한다"""
        return self.width * self.height / 2

    def perimeter(self):
        """직각삼각형의 둘레를 리턴한다"""
        return self.width + self.height + sqrt(self.width**2 + self.height **2)

    def __str__(self):
        """직각삼각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직각삼각형".format(self.width, self.height)

class Rectangle(Shape):
    """직사각형 클래스"""

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """직사각형의 넓이를 리턴한다"""
        super().area()  # ---------------- 부모의 메소드를 가져다 씀
        return self.width * self.height

    def perimeter(self):
        """직사각형의 둘레를 리턴한다"""
        return 2 * self.width + 2 * self.height

    def __str__(self):
        """직사각형의 정보를 문자열로 리턴한다"""
        return "밑변 {}, 높이 {}인 직사각형".format(self.width, self.height)

class Circle(Shape):
    """원 클래스"""

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """원의 넓이를 리턴한다"""
        super().area()  # ---------------- 부모의 메소드를 가져다 씀
        return pi * self.radius * self.radius

    def perimeter(self):
        """원의 둘레를 리턴한다"""
        return 2 * pi * self.radius

    def __str__(self):
        """원의 정보를 문자열로 리턴한다"""
        return "반지름 {}인 원".format(self.radius)


class Cylinder:
    """원통 클래스"""
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def __str__(self):
        """원통의 정보를 문자열로 리턴하는 메소드"""
        return "밑면 반지름 {}, 높이 {}인 원기둥".format(self.radius, self.height)


class Paint:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    def add_shape(self, shape: Shape):
        """그림판에 도형을 추가한다"""
        if isinstance(shape, Shape):  # 인스턴스 타입 확인
            self.shapes.append(shape)
        else:
            print("넓이, 둘래 메소드가 없습니다")

    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        return sum([shape.area() for shape in self.shapes])

    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        # sum : 리스트의 합을 구한다
        # [shape.perimeter() for shape in self.shapes] : 각 요소의.perimeter()를 후출하여, 리스트를 생성한다.
        return sum([shape.perimeter() for shape in self.shapes])

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다."""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str

# 테스트 코드
right_triangle_1 = RightTriangle(3, 4)
right_triangle_2 = RightTriangle(5, 12)
right_triangle_3 = RightTriangle(6, 8)

paint_program = Paint()

paint_program.add_shape(right_triangle_1)
paint_program.add_shape(right_triangle_2)
paint_program.add_shape(right_triangle_3)

print(paint_program.total_area_of_shapes())
print(paint_program.total_perimeter_of_shapes())


"""---------------------------------------------------------------------
추상 다중 상속

정리하자면 이 세 가지를 기억하셔야 합니다:

추상 클래스 다중 상속은 일반적으로 많이 사용한다.
다중 상속받는 부모 추상 클래스들이 추상 메소드로만 이뤄져 있으면 아무 문제 없이 다중 상속받을 수 있다.
다중 상속받는 부모 추상 클래스들 간에 이름이 겹치는 일반 메소드가 있으면 일반 클래스를 다중 상속받을 때와 동일한 문제가 생길 수 있다.
"""


class Message(ABC):
    @abstractmethod
    def print_message(self) -> None:
        pass

    @abstractmethod
    def send(self, destination: str) -> None:  # ----- 중복되는 추상 메소드
        pass

    def __str__(self):  # ----- 중복되는 일반 메소드
        return "Message 클래스의 인스턴스"

class Sendable(ABC):
    @abstractmethod
    def send(self, destination: str) -> None:   # ----- 중복되는 추상 메소드
        pass

    def __str__(self):  # ----- 중복되는 일반 메소드
        return "Sendable 클래스의 인스턴스"

class Email(Message, Sendable):
    def __init__(self, content, user_email):
        self.content = content
        self.user_email = user_email

    def print_message(self):
        print("이메일 내용입니다:\n{}".format(self.content))

    def send(self, destination):
        print("이메일을 주소 {}에서 {}로 보냅니다!".format(self.user_email, destination))

# 이메일 인스턴스를 생성한다.
email = Email("안녕? 오랜만이야 잘 지내니?", "young@codeit.kr")
# 메시지 내용 출력
email.print_message()
# 메시지 전송
email.send("captain@codeit.kr")


"""---------------------------------------------------------------------
함수/메소드 다형성
    - 옵셔널 파라미터 : 뒤쪽에 사용한다.
        def new_print(value_1, value_2=None, value_3=None ):
            print( "{} {} {}",  value_1, value_2, value_3 )
    - 파라미터 이름 명시 : 함수 호출시 파라미터 이름 명시적으로 표시
        new_print(value_1="홍길동", value_2="30" ):
    - 개수가 확정되지 않은 파라미터 : 마지막 파라미터 이름 앞에 * (튜플에 담아서 전달)
"""
def msg_print1(msg, *numbers):
    print(msg)
    return sum(numbers)

def msg_print2(*numbers, msg):
    print(msg)
    return sum(numbers)

print(msg_print1("test1", 1,3,5))
print(msg_print1("test1", 1))
print(msg_print1("test1", 1,3,5,9,11))

print(msg_print2(1,3,5,9,11, msg="test1"))



"""---------------------------------------------------------------------
파이썬 EAFP 코딩 스타일

LBYL Style : Look Before You Leap (어떤 작업 수행전에 확인 해보고 진행함: 돌다리도 두드리고 건너라.)
EAFP Style : Easier to Ask for Forgiveness Than Permission (일단 먼저 빨리 실행하고, 문제가 생기면 처리한다:허락보다 용서가 쉽다.)
"""

class PaintEAFP:
    """그림판 프로그램 클래스"""
    def __init__(self):
        self.shapes = []

    # EAFP
    def add_shape(self, shape: Shape):
        """그림판에 도형 인스턴스 shape을 추가한다. 단, shape은 추상 클래스 Shape의 인스턴스여야 한다."""
        self.shapes.append(shape)

    # EAFP
    def total_area_of_shapes(self):
        """그림판에 있는 모든 도형의 넓이의 합을 구한다"""
        total_area = 0
        for shape in self.shapes:
            try:
                total_area +=  shape.area()
            except (AttributeError, TypeError):
                print("그림판에 area 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}가 있습니다.".format(shape))
        return total_area

    # EAFP
    def total_perimeter_of_shapes(self):
        """그림판에 있는 모든 도형의 둘레의 합을 구한다"""
        # sum : 리스트의 합을 구한다
        # [shape.perimeter() for shape in self.shapes] : 각 요소의.perimeter()를 후출하여, 리스트를 생성한다.
        # return sum([shape.perimeter() for shape in self.shapes])
        total_perimeter = 0
        for shape in self.shapes:
            try:
                total_perimeter += shape.perimeter()
            except (AttributeError, TypeError):
                print("그림판에 perimeter 메소드가 없거나 잘못 정의되어 있는 인스턴스 {}가 있습니다.".format(shape))
        return total_perimeter

    def __str__(self):
        """그림판에 있는 각 도형들의 정보를 출력한다."""
        res_str = "그림판 안에 있는 도형들:\n\n"
        for shape in self.shapes:
            res_str += str(shape) + "\n"
        return res_str

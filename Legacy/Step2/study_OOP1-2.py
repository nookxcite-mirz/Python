# 객체 지향 프로그래밍 : Topic1 - 객체 지향 프로그램 이란?
# chapter4 - 객체 만들기 연습

### 메뉴 만들기
class MenuItem:
    # 음식 메뉴를 나타내는 클래스
    def __init__(self, name, price):
        # 코드를 쓰세요
        self.name = name
        self.price = price

    def __str__(self):
        # 코드를 쓰세요
        return "{} 가격: {}".format(self.name, self.price)

# 메뉴 인스턴스 생성
burger = MenuItem("햄버거", 4000)
coke = MenuItem("콜라", 1500)
fries = MenuItem("후렌치 후라이", 1500)

# 메뉴 인스턴스 출력
print(burger)
print(coke)
print(fries)


### 속성 없는 계산기
class SimpleCalculator:
    # 계산기 클래스
    @staticmethod
    def add(first_number, second_number):
        # 파라미터로 받는 두 숫자의 합을 리턴한다
        return first_number+second_number

    @staticmethod
    def subtract(first_number, second_number):
        # 첫 번째 파라미터에서 두 번째 파라미터를 뺀 값을 리턴한다
        return first_number - second_number

    @staticmethod
    def multiply(first_number, second_number):
        # 파라미터로 받는 두 숫자의 곱을 리턴한다
        return first_number * second_number

    @staticmethod
    def divide(first_number, second_number):
        # 첫 번째 파라미터를 두 번째 파라미터로 나눈 값을 리턴한다
        return first_number / second_number


# 계산기 인스턴스 생성
calculator = SimpleCalculator()

# 계산기 연산 호출
print(calculator.add(4, 5))
print(calculator.subtract(4, 5))
print(calculator.multiply(4, 5))
print(calculator.divide(4, 5))



### 블로그 유저 만들기
class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 작성 날짜와 내용을 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글의 정보를 문자열로 리턴하는 메소드
        return "작성 날짜: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저 클래스
    def __init__(self, name):
        """
        블로그 유저는 속성으로 이름, 게시글들을 갖는다
        posts는 빈 배열로 초기화한다
        """
        self.name = name
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.posts:
            print(post)

    def __str__(self):
        # 간단한 인사와 이름을 문자열로 리턴
        return "안녕하세요 {}입니다.\n".format(self.name)

# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호")

# 블로그 유저 인스턴스 출력(인사, 이름)
print(blog_user_1)

# 블로그 유저 게시글 2개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()
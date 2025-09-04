# 객체 지향 프로그래밍 : Topic1 - 객체 지향 프로그램 이란?
# chapter5 - 객체 지향 프로그래밍 직접 해보기

class Counter:
    """
    시계 클래스의 시,분,초를 각각 나타내는데 사용될 카운터 클래스
    """
    limit = 0
    value = 0

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최댓값), value(현재까지 카운트한 값)을 설정한다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초깃값 0으로 설정한다.
        """
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 설정한다.
        아닐 경우 value에 0을 설정한다.
        """
        # self.value = new_value if 0 <= new_value < self.limit else 0
        if 0 <= new_value < self.limit:
            self.value = new_value
        else:
            self.value = 0

    def tick(self):
        """
        value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        return False

    def __str__(self):
        """
        value를 최소 두 자릿수 이상의 문자열로 리턴한다.
        일단 str 함수로 숫자형 변수인 value를 문자열로 변환하고 zfill 메소드를 호출한다.
        """
        return str(self.value).zfill(2)

class Clock:
    """
    시계 클래스
    """
    HOURS = 24      # 시 최댓값
    MINUTES = 60    # 분 최댓값
    SECONDS = 60    # 초 최댓값

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 인스턴스 3개(hour, minute, second)를 정의한다.
        현재 시간을 파라미터 hour시, minute분, second초로 지정한다.
        """
        self.hourCnt = Counter(HOURS)
        self.minCnt = Counter(MINUTES)
        self.secCnt = Counter(SECONDS)

        self.hourCnt.set(hour)
        self.minCnt.set(minute)
        self.secCnt.set(second)

    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        self.hourCnt.set(hour)
        self.minCnt.set(minute)
        self.secCnt.set(second)

    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가시킬 때, 분 또는 시가 바뀌어야하는 경우도 처리한다.
        """
        if self.secCnt.tick() == True:
            if self.minCnt.tick() == True:
                self.hourCnt.tick()

    def __str__(self):
        """
        현재 시간을 시:분:초 형식으로 리턴한다. 시, 분, 초는 두 자리 형식이다.
        예시: "03:11:02"
        """
        return "{}:{}:{}".format(self.hourCnt, self.minCnt, self.secCnt)
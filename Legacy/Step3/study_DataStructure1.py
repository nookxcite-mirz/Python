# 지료구조
# Topic1 : 기본 자료구조

#-----------------------------------------------
# - Chapter1 : 자료 구조란?
#-----------------------------------------------
import time

test_list = [x for x in range(0,1000001)]	    # - 선형 자료구조
test_set  = set([x for x in range(0,1000001)])	# - 이진 자료구조

t_0 = time.time()
print( 1000000 in test_list)
t_1 = time.time()
print("리스트 검색 시간: {}".format(t_1 - t_0))

t_0 = time.time()
print( 1000000 in test_set)
t_1 = time.time()
print("세트 검색 시간: {}".format(t_1 - t_0))

# id 함수를 이용하면 저장한 데이터의 메모리 주소를 정수로 표현한 값을 알아낼 수 있습니다.
list1 = [1, 2]
print(id(list1))


#-----------------------------------------------
# - Chapter3 : 배열
#-----------------------------------------------
list = [1, 2, "데이터", 5, True] # > 파이썬은 레퍼런스로 생성되므로, 여러 타입을 담을수 있다.
"""
배열 접근 	: O(1)
배열 탐색 	: O(n)
추가 연산 	: O(n:공간 없음), O(1:공간 있음) 
(append)  시간 복잡도 분할 상환 분석(Amortized Analysis) 사용시 O(1) 쪽에 가까움.
삽입 연산	: O(2n+1:공간 없음), O(n+1:공간 있음-이동) 
(insert)	
"""


# -----------------------------------------------
# - Chapter4 : 링크드리스트
# -----------------------------------------------
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """링크드  리스트 클래스"""

    def __init__(self):
        self.head = None  # 링크드 리스트의 가장 앞 노드
        self.tail = None  # 링크드 리스트의 가장 뒤 노드

    def append(self, data):
        """링크드 리스트 추가 연산 메소드"""
        new_node = Node(data)

        # 링크드 리스트가 비어 있으면 새로운 노드가 링크드 리스트의 처음이자 마지막 노드다
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # 링크드 리스트가 비어 있지 않으면
        else:
            self.tail.next = new_node  # 가장 마지막 노드 뒤에 새로운 노드를 추가하고
            self.tail = new_node  # 마지막 노드를 추가한 노드로 바꿔준다

    def __str__(self):
        """링크드 리스트를 문자열로 표현해서 리턴하는 메소드"""
        res_str = "|"

        # 링크드  리스트 안에 모든 노드를 돌기 위한 변수. 일단 가장 앞 노드로 정의한다.
        iterator = self.head

        # 링크드  리스트 끝까지 돈다
        while iterator is not None:
            # 각 노드의 데이터를 리턴하는 문자열에 더해준다
            res_str += f" {iterator.data} |"
            iterator = iterator.next  # 다음 노드로 넘어간다

        return res_str


# 새로운 링크드 리스트 생성
linked_list = LinkedList()

# 링크드 리스트에 데이터 추가
linked_list.append(2)
linked_list.append(3)
linked_list.append(5)
linked_list.append(7)
linked_list.append(11)

# 링크드 리스트 출력
print(linked_list)

# -----------------------------------------------
# - Chapter5 : 해시 테이블
# -----------------------------------------------
"""
Direct Access Table  
	> Key값을 배열화 하여 적용 O(1)접근, Key 메모리 낭비.

Hach Table (해시 테이블) 
	> 고정된 배열을 만들고, 특정 키값을 원하는 범위(고정 배열 크기)의 자연수로 바꿔주는 해쉬함수 사용
	> 해쉬함수와 DirectAcessTable 사용하여 구현.

hash 함수의 한계
	> 파이썬 hash 함수는 언어 자체적으로는 불변 타입 자료형에만 사용할 수 있습니다.
		대표적인 불변 타입 자료형은: 불린형 정수형 소수형 튜플 문자열	

해시 테이블 충돌 해결을 위한 방법 
	> Chaining 개념.
		: 해시 테이블 충돌 발생시 링크드 리스트로 데이터 연결하여 해결한다.
	> Open Addressing 개념.
		> 충돌 발생시 비어있는 Key 배열에 저장.
			1. 선형 탐사(Linear Probing) 
			2. 제곱 탐사(Quadric Probing)
"""

# -----------------------------------------------
# - Chapter6 : 추상 자료형
# -----------------------------------------------
"""
- Abstract Data Type

리스트 (동적 배열)
	연산	            예시	                            시간 복잡도
    접근          	list_1[0], list_1[0] = 5	    O(1)
    추가	            list_1.append(2)	            O(1) (분할 상환)
    맨 뒤 삭제	    list_1.pop()	                O(1) (분할 상환)
    길이 확인	    len(list_1)	                    O(1)
    삽입	            list_1.insert(3, "성태호")	    O(n)
    삭제	            del list_1[0], list_1.pop(3)	O(n)
    탐색	            "이재하" in list_1	            O(n)

deque (더블리 링크드 리스트)
    연산	            예시	                            시간 복잡도
    맨 앞 삭제	    deque_1.popleft()	            O(1)
    맨 앞 삽입	    deque_1.appendleft("김신의")	    O(1)
    맨 뒤 삭제	    deque_1.pop()	                O(1)
    맨 뒤 삽입	    deque_1.append("이규식")	        O(1)
    길이 확인	    len(deque_1)	                O(1)
    
딕셔너리 (해시 테이블)
    연산	            예시	                            시간 복잡도
    탐색	            dict_1["성태호"]	                O(1) (평균)
    삽입	            dict_1["강영훈"] = 100	        O(1) (평균)
    삭제	            del dict_1["강영훈"], dict_1.pop("강영훈")	O(1) (평균)
    길이 확인	    len(dict_1)                 	O(1)

세트 (해시 테이블)
    연산	            예시	                            시간 복잡도
    탐색	            "최지웅" in set_1	            O(1) (평균)
    삽입	            set_1.add("손동욱")	            O(1) (평균)
    삭제	            set_1.remove("김현승")
                    set_1.pop("김현승")	            O(1) (평균)
    길이 확인	    len(set_1)                      O(1)


큐 (queue)       : FIFO - deque(양방향 큐)
스텍 (stack)     : LIFO - deque, list.
딕셔너리 (map)    : 해쉬 테이블
세트 (set:집합)   : 해쉬 테이블(key만 저장), 순서에 상관 없이 중복되지 않은 데이터를 저장 할수 있는 자료형
	
"""
from collections import deque
#Queue로 사용.
queue = deque()
deque.append("태호")
deque.append("현승")
deque.append("지웅")
deque.append("동욱")
deque.append("신의")
print(queue)
print(queue[0])
print(queue.popleft())  # 삭제 리턴.
print(queue.popleft())
print(queue)

#Stack으로 사용.
stack = deque()
stack.append("T")
stack.append("a")
stack.append("e")
stack.append("h")
stack.append("o")
print(stack[-1])        # 맨끝 데이터 접근
print(stack.pop())      # 맨끝 데이터 삭제
print(stack.pop())      # 맨끝 데이터 삭제
print(stack)

#Dictionary
grades = {}
grades["현승"] = 80
grades["태호"] = 60
grades["지웅"] = 90
grades["동욱"] = 70
grades["신의"] = 96
print(grades)

print(grades["태호"]) # 접근
grades["태호"] = 100  # 변경
grades.pop("태호")    # 삭제
grades.pop("지웅")
print(grades)

#Set
finished_class = set()
finished_class.add("자료 구조")
finished_class.add("알고리즘")
finished_class.add("프로그램 기초")
finished_class.add("인터렉티브 웹")
finished_class.add("데이터 사이언스")
print(finished_class)   # 순서 없이 출력됨
print("자료 구조" in finished_class)    # 탐색
finished_class.remove("자료 구조")      # 삭제
print(finished_class)


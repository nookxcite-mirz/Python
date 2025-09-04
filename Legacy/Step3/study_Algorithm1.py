"""
알고리즘 정석
    Topic1      : 좋은 알고리즘 이란.

[정렬 알고리즘]
Selection Sort
Insertion Sort
Bubble Sort
Shell Sort
Heap Sort
Merge Sort		: Divide and Conquer (반으로 잘개 쪼개 합치는 과정으로 처리)
Quick Sort		: Divide and Conquer (파티션:Pivot을 중심으로 좌/우 소팅), 파티션 Pivot을 어떻게 잡을 것인가?
Quick3 Sort

시간과 공간
 > 최적화 > 시간(처리 속도) > 공간(메모리)

시간 복잡도 (Time Complexity)
 - 데이터가 많아질때 얼마나 시간이 더 걸리는가?.

 거듭제곱 : Exponentiation
 로그   : Logarithms > 밑수가 2인 경우 Lg로 씀.
     Lg(8) = 3 <>  2^3 = 8

- Big-O Notation (점근 표기법)
  소요시간 		Big-O
  20n + 40		O(n)
  2n^2 + 8n		O(n^2)
  20lgn + 60	O(lgn)

- 리스트		O(1)	O(n)	O(n^2)
   100		1초		1초		1초
   200		1초		2초		4초
   1000		1초		10초		100초
   10000	1초		100초	10000초

 선형 탐색 -> 반복문 > O(n)
 이진 탐색 -> 반복문 > O(lg n)


[List Operations]
Operation		    Code							Average Case
인덱싱				my_list[index]					O(1)
정렬				    my_list.sort()					O(n lgn)
				    sorted(my_list)					O(n lgn)
뒤집기				my_list.reverse()				O(n)
탐색				    element in my_list				O(n)
끝에 요소 추가		my_list.append(element)			O(1)
중간에 요소 추가		my_list.insert(index, element)	O(n)
삭제				    del my_list[index]				O(n)
최솟값, 최댓값 찾기	min(my_list)					O(n)
				    max(my_list)					O(n)
길이 구하기			len(my_list)					O(1)
슬라이싱			       my_list[a:b]					O(b-a)

[Dictionary Operations]
Operation		    Code							Average Case
값 찾기			    my_dict[key]					O(1)
값 넣어주기/덮어쓰기	my_dict[key] = value			O(1)
값 삭제			    del my_list[key]				O(1)

O(1)		: 상수
O(lg{n})	: n의 역거듭제곱
O(n)		: 반복문
O(n lg{n})	: O(n)와 O(lg{n})가 겹져진 반복문
O(n^2)		: 2중 반복문
O(n^3)		: 3중 반복문
O(n^4)		: 4중 반복문
O(2^n)
O(n!)
"""


"""
알고리즘 정석
    Topic2      : 재귀 함수.
    Chapter1    :

"""


"""
알고리즘 정석
    Topic3      : 알고리즘 패러다임.
    Chapter1    :

"""


"""
알고리즘 정석
    Topic4      : 문제 해결 능력 기르기
    Chapter1    :

"""

## 프로그래밍 기초 in Python > Chapter3 프로그램과 데이터 in Python
# 리스트 & for

# list
numbers = [2,3,4,5,6,7]
names = ["철수","영희","태호","영훈"]

# 인덱싱
i = numbers[0] + numbers[2]
i = numbers[-6]  #range -6~-1, 0~5

# 집합
numbers[0:4]		#0번째부터 4개
numbers[2:]		    #2번째부터 마지막
new_list = numbers[:3]

print(type(names))

# list 함수
len(numbers)
numbers.append(9)
del numbers[3]
print(numbers)

numbers.insert(4, 37)	#4번째에 37추가
names.index("영희")		#return 1
names.remove("영희")
print(names)

# list 정렬
numbers = [19,13,2,5,3,11,7,17]
new_list1 = sorted(numbers)
new_list2 = sorted(numbers, reverse=True)
numbers.sort()
numbers.sort(reverse=True)
print(numbers)

print( 7 in numbers )		# contain
print( 7 not in numbers )	# not contain

# for
# for firstElement in list:
# for firstElement in range(start, stop): 		# start 부터 stop-1 까지
# for firstElement in range(stop): 				# 0 부터 stop-1 까지
# for firstElement in range(start, stop, step): 	# start 부터 stop-1 까지, step 간격으로
# range list내용을 for문이 돌면서 사용후 버림 처리됨 메모리 효율.

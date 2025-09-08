# 리스트 ----------------------------------------------------------------
# 리스트 조작
a = [1,"hellow",2,3,[4,5,6]]
print(a[4][1])
print(a[1][1])

print(a[0:3])
print(a[0::2])

a[1] = "world"
print(a)
del a[1]  
print(a)
del a[3:]
print(a)

# 요소 추가 삭제
a.append(7)
print(a)
a.insert(1,10)
print(a)
a.remove(10)
print(a)

# 리스트 순서
a = [1,2,3,4,5]
print(a)
a.reverse()
print(a)

# 리스트 복제
b = a
print(b)
b[0] = 10
print(a)
print(b)

# 리스트 정렬  
a = [5,3,7,1,2]
a.sort()    
print(a)
b = a.pop()
print(b)
print(a)
c = a.pop(0)
print(a)

# 추가
a.append([4,5])
print(a)
a.extend([6,7])
print(a)


# 튜플 ---------------------------------------------------------------- 잠긴 리스트
# Mutable (변경가능: 리스트, 딕셔너리, 집합), Immutable (변경불가: 튜플, 정수, 실수, 문자열)
t1 = (1,2,3,4,5)
t2 = 3,4,5,6,7
print(type(t1), type(t2))
t3 = t1 + t2
print(t3)


# 딕셔너리 ----------------------------------------------------------------
# 딕셔너리 조작
a = {1:"hellow",2:2,3:3,4:[4,5,6]}
print(a[4][1])
print(a[1][1])

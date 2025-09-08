"""
주석 멀티 라인
"""
# Terminal 에 "Python" 이라고 쓰면 REFL 창이 실행됨 파이선 코딩 종료시는 exit(), quit() 등으로 끝남
# Terminal 에 "Python xxx.py" 이라고 쓰면 파일을 실행함

print("Hello World")
print("Welcome to Python")

"""
GPT 나 Gemini에서 디버깅시 ``` 내용 ``` 로 물어볼 경우 빠르게 코드를 수정해 둔다.
"""

# 자료형
a = 1
b = 3.14
c = 4.5e10  #지수 4.5 * 10
d = True
e = "Life is short \n You need Python"
e1 = 'Life is "short"'
e2 = "Life is \"short\""
f = "1234567890"

# 연산자 +, -, *, /, **(제곱^), %(나머지), //(몫)
# 문자열의 이스케이프 코드는 따라 확인 필요.
print(a, type(a))
print(b, type(b))
print(c, type(c))
print(d, type(d))
print(e, e1, e2)
print(f*3)          # 문자열 반복
print(len(f*3))
print(e[3], e[-1], e[0:4], e[16:], e[::2])

# 문자열 슬라이싱 [이상:미만:간격], 문자열은 변경 불가.
data = "20250904Python Start"
print(data[:8])
print(data[8:])

# %s, %c, %d, %f, %i, %o, %x, %X 등의 슬라이싱 자료형 지원
msgInt = "I eat %d apples." % 3
msgStr  = "I eat %s apples." % "five"
msgMulti = "I eat %d(%s) apples." % (5, "five")
print(msgInt, msgStr)
print(msgMulti)

# 공백 채우기
a = "%-10s Jane.\n" % 'hi'
b = "%10s Jane.\n" % 'hi'
print(a,b)

# .format() 사용
msg1 = "I eat {0} apples. for {1} days".format(5, 3)
msg2 = "I eat {num} apples. for {day} days".format(num=5, day=3)
print(msg1, msg2)

# 정렬
a = "{0:<10}".format("hi")
b = "{0:>10}".format("hi")
c = "{0:^10}".format("hi")
d = "{0:*^10}".format("hi")
print(a)
print(b)
print(c)
print(d)

# 최신 문자열 사용 format을 f로 변경
name  = '홍길도'
age   = 20
a = f'이름: {name}, 나이: {age}'
print(a)

# 문자열 lstrip, rstrip, strip, replace, split, join 편집
a = ", ".join('abcd')
print(a)
a = ", ".join(['a', 'b', 'c', 'd'])
print(a)

import math, time

def get_prime(n):
    if n <= 1:
        return []
    prime = [2]
    #제곱근 까지 제한
    limit = int(math.sqrt(n))
    #홀수 리스트 작성
    data = [i+1 for i in range(2,n,2)]

    while limit >= data[0]:
        prime.append(data[0])
        #나누어 떨어지지 않은 수만 꺼냄
        data = [j for j in data if j % data[0] != 0]
    return prime + data

start = time.time()
get_prime(10000)    # 시간초과
end = time.time()       
print( f"{end - start:.5f} sec with Func")

# pip install sympy - sympy 모듈 설치.

from sympy import sieve
from sympy import isprime

start = time.time()
prime = [i for i in sieve.primerange(1, 100000)] 
end = time.time()       
print( f"{end - start:.5f} sec with Simpy")
isprime(101) #소수 인지 판정

# 피보나치 수열 > 황금비 수열
# 재귀 함수
def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
# 메모리를 통해, 한번실행 후 부터는 빠르게 연산
# 파이썬의 재귀 호출 제한은 일반적으로 1000회, 더 깊어지면 maximum recursion depth exceeded 발생.
fibmem = {1:1, 2:1}
def fib2(n):
    if n in fibmem:
        return fibmem[n]
    fibmem[n] = fib2(n-2) + fib2(n-1)
    return fibmem[n]

start = time.time()
fib2(100)
end = time.time()   
print( f"{end - start:.5f} sec fib2")

start = time.time()
fib2(100)
end = time.time()   
print( f"{end - start:.5f} sec fib2")
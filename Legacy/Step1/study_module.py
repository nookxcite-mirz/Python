# 프로그래밍 기초 in Python > Chapter4 파이썬 응용하기

# 모듈 : 기능이 정리된 python 파일

import study_module_calc                # 모듈 include
import study_module_calc as calc        # 모듈 이름 변경

from study_module_calc import add, multiply     # 지정 함수만 불러옴
from study_module_calc import *                 # 모든 함수 불러 오기

print( study_module_calc.add(2, 5))
print( study_module_calc.multiply(2, 5))
print( calc.subtract(2, 5))
print( calc.divide(2, 5))

print( add(2, 5) )
print( multiply(2, 5) )

# 스탠다드 라이브러리 (standard library)
import math     # 수학 모듈
print(math.pi)
print(math.log10(100))

import random   # 난수 모듈
print(random.random())
print(random.randint(1,20))     # 정수 랜덤
print(random.uniform(1,20))     # 실수 랜덤

import datetime # 시간 모듈
day = datetime.datetime(2021, 2, 1)
print(day)

today = datetime.datetime.now()
print(today)

timeoffset = today - day        # timedelta
print(timeoffset)

timeadd = datetime.timedelta(days=3, hours=3)
print( today + timeadd)

print(today.strftime("%A, %B %dth %Y"))
# 포맷 코드
# %a	요일 (짧은 버전)	                Mon
# %A	요일 (풀 버전)	                Monday
# %w	요일 (숫자 버전, 0~6, 0이 일요일)	5
# %d	일 (01~31)	                    23
# %b	월 (짧은 버전)	                Nov
# %B	월 (풀 버전)	                    November
# %m	월 (숫자 버전, 01~12)	            10
# %y	연도 (짧은 버전)	                16
# %Y	연도 (풀 버전)	                2016
# %H	시간 (00~23)	                    14
# %I	시간 (00~12)	                    10
# %p	AM/PM	                        AM
# %M	분 (00~59)	                    34
# %S	초 (00~59)	                    12
# %f	마이크로초 (000000~999999)	    413215
# %Z	표준시간대	                    PST
# %j	1년 중 며칠째인지 (001~366)	    162
# %U	1년 중 몇 주째인지 (00~53, 일요일이 한 주의 시작이라고 가정)	35
# %W	1년 중 몇 주째인지 (00~53, 월요일이 한 주의 시작이라고 가정)	35

import os       # operation sys
print( os.getlogin() )
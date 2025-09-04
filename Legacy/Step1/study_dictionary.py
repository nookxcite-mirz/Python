# 프로그래밍 기초 in Python > Chapter3 프로그램과 데이터 in Python
# 사전 & 데이터

# key-value pair (키값-쌍)

my_dic = { 5: 29, 2: 4, 3: 9 }
print(my_dic[3])
print(type(my_dic))

my_dic[9] = 81  # append
print(my_dic)

my_family = { "father":"smith", "mother":"charolina" , "children":"bob" }
print(my_family)
print("smith" in my_family.values())

for value in my_family.values():
    print(value)

for key in my_family.keys():
    value = my_family[key]
    print(key, value)

for key, value in my_family.items():
    print(key, value)


# 파이선의 데이터 처리
x = [2,3,5,7,11]
y = x           # 참조
z = list(x)     # 복사
y[2] = 4
print(x)
print(y)    # 둘다 같은 결과임 Reference 로 처리됨 (alias:가명)
print(z)

# 리스트 & 문자열
alphabet_list =['A','B','C','D','E','F','G','H','I','J']
print(alphabet_list[0:5])   # 리스트 슬라이싱
print(alphabet_list[4:])
print(alphabet_list[:4])

list_1=[1,2,3,4]
list_2=[5,6,7,8]
listtotal = list_1+list_2
print(len(listtotal))
listtotal[1] = 11
print(listtotal)

for alpha in alphabet_list:
    print(alpha)

alphabet_str = "ABCDEFGHIJ"
print(alphabet_str[0:5])
print(alphabet_str[4:])
print(alphabet_str[:4])
print(len(alphabet_str))
#alphabet_str[1] = "C"  # 문자열 수정불가.

for alpha in alphabet_str:
    print(alpha)

# mutable(수정가능) immutable(수정 불가능) > 문자열은 인덱싱 참조로 변경이 불가능 함.

# 자릿수 합 계산
def sum_digit(num):
    total = 0
    for i in str(num):
        total += int(i)
    return total

calc_result = 0

for calc in range(1001):
    calc_result += sum_digit(calc)

print(calc_result)

# 주민번호 가리기
def mask_security_number(security_number):
    # 코드를 입력하세요.
    templist = list(security_number)
    for i in range(len(templist) -4, len(templist)):
        templist[i] = "*"
    return ''.join(templist)

def mask_security_number_easy(security_number):
    # 코드를 입력하세요.
    return security_number[:-4] + "****"        # 배열 참조 -index

print(mask_security_number("880720-1234567"))
print(mask_security_number("8807201234567"))
print(mask_security_number("930124-7654321"))
print(mask_security_number_easy("9301247654321"))
print(mask_security_number_easy("761214-2357111"))
print(mask_security_number_easy("7612142357111"))

units = ["cm", "m", "yard"]
units_to_string = ", ".join(units)              # 문자열 합치기 (join)
print(type(units_to_string))
print(units_to_string)


# 팰린드룸 > 기러기, 토마토
def is_palindrome(word):
    for left in range(len(word) // 2):
        right = len(word) - left - 1
        if word[left] != word[right]:
            return False
    return True

def is_palindrome_easy(word):
    print(word[::-1])
    return word == word[::-1]

# 테스트
print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome_easy("kayak"))
print(is_palindrome_easy("hello"))
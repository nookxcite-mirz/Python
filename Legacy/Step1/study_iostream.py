## 프로그래밍 기초 in Python > Chapter4 파이쎤 응용
# 파일 읽고/쓰기

# input > 문자열을 받는다.
#name = input("이름을 입력하세요 : ")
#print(name)

# file i/o
with open('Data/data.txt', 'r') as fr:     # data.txt 파일 읽기
    print(type(fr))
    for line in fr:
        print(line.strip())               # 화이트 스페이스 제거 .strip()

# 화이트 스페이스 공백문자 \n,\t," "

#stip
my_string1 ="1. 2. 3. 4. 5. 6"
print(my_string1.split(". "))
my_string2 ="   1 \n2 \t\t 3 \n 4  5    6 \n"
my_numbers = my_string2.split()          # 파라미터 없을 경우, 화이트 스페이스 제거
print(my_numbers)

# 'w' 덮어쓰기, 'a' 추가하기
with open("Data/new_data.txt", 'w') as fw:
    fw.write("Hellow world!\n")
    fw.write("My name is Hong")


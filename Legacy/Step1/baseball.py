# 프로그래밍 기초 in Python > Chapter4 파이썬 응용하기
# 야구 프로젝트

from random import randint

# 정렬되지 않은 3 랜덤 수 반환
def generate_numbers():
    gen_nums = []
    while len(gen_nums) < 3:
        randnum = randint(1, 9)
        if randnum not in gen_nums:
            gen_nums.append(randnum)
    print("0과 9 사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")
    return gen_nums

# print(generate_numbers())

# 유저로 부터 숫자 3개를 입력받는 함수
def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    new_guess = []
    # 코드를 작성하세요.
    while len(new_guess) < 3:
        try:
            in_num = int(input("{}번째 숫자를 입력하세요: ".format(len(new_guess) + 1)))
        except:
            print("숫자를 넣어주세요. 다시 입력하세요.")
            continue
        if in_num < 0 or in_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
        elif in_num not in new_guess:
            new_guess.append(in_num)
        else:
            print("중복되는 숫자 입니다. 다시 입력하세요.")
    return new_guess

# print(take_guess())

# 스트라이크 수와 볼 수를 알려 주는 get_score 함수를 작성
def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    # 코드를 작성하세요.
    for i in range(len(guess)):
        if guess[i] == solution[i]:     # 스트라익
            strike_count += 1
        if guess[i] in solution and guess[i] != solution[i]:    # 솔루션에 포함되어 있고 같은 위치가 아니면
            ball_count += 1
    #for i in range(len(guess)):
    #   for j in range(len(solution)):
    #       if i != j and guess[i] == solution[j]:              # 볼
    #           ball_count += 1
    return strike_count, ball_count

# 테스트
#> s_1, b_1 = get_score([2, 7, 4], [2, 4, 7])
#> print(s_1, b_1)

#> s_2, b_2 = get_score([7, 2, 4], [2, 4, 7])
#> print(s_2, b_2)

#> s_3, b_3 = get_score([0, 4, 7], [2, 4, 7])
#> print(s_3, b_3)

#> s_4, b_4 = get_score([2, 4, 7], [2, 4, 7])
#> print(s_4, b_4)

# 여기서부터 게임 시작!
ANSWER = generate_numbers()
tries = 0
print(ANSWER)

# 코드를 작성하세요.
while True:
    user_input = take_guess()
    tries += 1
    s, b = get_score(user_input, ANSWER)
    print ( "Strike:{}, Ball:{}".format( s, b ) )
    if user_input == ANSWER:
        break

print("축하합니다. {}번 만에 숫자 3개의 값과 위치를 모두 맞추셨습니다.".format(tries))


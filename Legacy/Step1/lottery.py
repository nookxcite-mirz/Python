# 프로그래밍 기초 in Python > Chapter4 파이썬 응용하기
# 로또 시뮬레이터

from  random import randint

# 정렬되지 않은 6개 랜덤 수 반환
def generate_numbers(n):
    gen_nums = []
    while len(gen_nums) < n:
        randnum = randint(1, 45)
        if randnum not in gen_nums:
            gen_nums.append(randnum)
    return gen_nums

#> my_nums = generate_numbers(6)
#> print("나의 번호 > " + str( my_nums ) )

# 앞 6개는 정렬 마지막은 2등 번호
def draw_winning_numbers():
    gen_nums = generate_numbers(7)
    win_nums = gen_nums[0:len(gen_nums)-1]
    win_nums.sort()
    win_nums.append(gen_nums[len(gen_nums)-1])
    return win_nums

def draw_winning_numbers_easy():
    winning_numbers = generate_numbers(7)
    return sorted(winning_numbers[:6]) + winning_numbers[6:]

#> win_nums = draw_winning_numbers()
#> print("담청 번호 > " + str(win_nums))

# list 비교 후 겹치는 갯수 반환
def count_matching_numbers(numbers, winning_numbers):
    count = 0
    for x in numbers:
        for y in winning_numbers:
            if x == y :
                count +=1
                break
    return count

def count_matching_numbers_easy(list_1, list_2):
    same_numbers = list(set(list_1).intersection(list_2))
    return len(same_numbers)

#> print("겹치는 수 > " + str(count_matching_numbers(my_nums,win_nums)))

# 당첨금 체크
def check(numbers, winning_numbers):
    count = count_matching_numbers(numbers, winning_numbers[:6])
    bonus_count = count_matching_numbers(numbers, winning_numbers[6:])
    result = 0
    if count == 6:
        return 1000000000
    elif count == 5:
        if bonus_count == 1:
            return 50000000
        else:
            return 1000000
    elif count == 4:
        return 50000
    elif count == 3:
        return 5000
    else:
        return 0

#> print( check([2, 4, 11, 14, 25, 40], [4, 12, 14, 28, 40, 41, 6] ))
#> print( check([2, 4, 11, 14, 25, 40], [2, 4, 10, 11, 14, 40, 25] ))

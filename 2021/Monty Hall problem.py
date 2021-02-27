import random
import math
import time

print("\nMonty Hall problem\n")

mode = 1 # (횟수입력모드 : 1 / 자동연산모드 : 2)

if mode == 1:
    while True:
        number_range = input("시행횟수를 입력하세요. : ")
        if number_range.isdigit() == True:
            if int(number_range) == 0:
                number_range = math.inf
            else:
                number_range = int(number_range)
            print()
            break
        else:
            print("\n올바른 숫자를 입력하세요.")
else:
    number_range = math.inf

win_count, fail_count = 0, 0
plag = 1
while plag <= number_range:
    variable_list = [0, 0, 0]

    prize = random.randint(1, 3)
    variable_list[prize - 1] = 1

    select = random.randint(1, 3)
    while True:
        open = random.randint(1, 3)
        if variable_list[open - 1] != 1:
            if select != open:
                break

    re_select = 6 - select - open
    if variable_list[re_select - 1] == 1:
        win_count += 1
    else:
        fail_count += 1

    print(f"{plag}회차 (성공횟수: {win_count} | {round((win_count / (win_count + fail_count)) * 100, 3)}% | 실패횟수: {fail_count})")
    # time.sleep(0.1)
    plag += 1
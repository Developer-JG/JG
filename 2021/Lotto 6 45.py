import random

print("\n a lottery ticket project")
print("\n" * 1)

run_mod = 1 # (자동모드 : 1 / 수동(반자동)모드 : 2)
print_mod = 2 # (모두출력 : 1 / 결과만출력 : 2)
stop = 0

count = 0

one, two, three, four, five = 0, 0, 0, 0, 0


# 반복실행
while run_mod == 1 or run_mod == 2:
    count = count + 1
    plus_number = 0


    # 번호 추첨
    while True:
        standard, lotto_1, lotto_2, lotto_3, lotto_4, lotto_5 = [], [], [], [], [], []
        lotto_list = [standard, lotto_1, lotto_2, lotto_3, lotto_4, lotto_5]


        # 번호 선택
        for i in range(0, 6):
            lotto = random.sample(range(1, 46), 6)
            lotto_list[i] = lotto
            lotto_list[i].sort()
            if i == 0:
                while True:
                    plus_number = random.randint(1, 46)
                    plag = 0
                    for j in (0, 4):
                        if lotto_list[i][j] == plus_number:
                            plag = plag + 1
                    if plag == 0:
                        break


        # 중복 번호 확인
        plag, plag_1 = 0, 0

        for i in range(1, 6):
            for j in range(1, 6):
                for k in range(0, 6):
                    if lotto_list[j][k] in lotto_list[i]:
                        plag = plag + 1
                    if plag == 6:
                        plag_1 = plag_1 + 1
                plag = 0
        if plag_1 == 5:
            break


    # 번호 출력
    if print_mod == 1:
        print("{0:-^30}".format(" 선택 번호 "))
        for i in range(1, 6):
            print(lotto_list[i])
        print("\n" * 2)
        print("{0:-^30}".format(" 선출 번호 "))
        print(lotto_list[0])

        if run_mod == 1:
            print(" : ")
        elif run_mod == 2:
            input(" : ")

        print("\n" * 3)


    # 일치 확인
    for i in range(1, 6):
        plag = 0
        for j in range(0, 5):
            if lotto_list[i][j] in lotto_list[0]:
                plag = plag + 1
        if plag == 6:
            one = one + 1
            print(f"{count}회차 {one}번쨰 1등 당첨 ({round(one  / (count * 5), 10)})")
            input()
        elif plag == 5:
            if plus_number in lotto_list[i]:
                two = two + 1
                print(f"{count}회차 {two}번쨰 2등 당첨 ({round(two  / (count * 5), 10)})")
                input()
            else:
                three = three + 1
                print(f"{count}회차 {three}번쨰 3등 당첨 ({round(three  / (count * 5), 10)})")
                input()
        elif plag == 4:
            four = four + 1
            print(f"{count}회차 {four}번쨰 4등 당첨 ({round(four  /(count * 5), 10)})")
            # input()
        elif plag == 3:
            five = five + 1
            print(f"{count}회차 {five}번쨰 5등 당첨 ({round(five  / (count * 5), 10)})")
            # input()

    if stop == count:
        break

else:
    print("실행중에 문제가 생겨 시작하지 못했습니다.\n모드를 확인하여 다시 시작하여주시기 바랍니다.\n\n")
    while True:
        input("Restart")
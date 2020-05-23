from random import randint

print("Rock Scissors Paper game project")

print("\n가위바위보를 시작합니다")
input()
while True:
    p_rsp = input("가위(q), 바위(w), 보(e) : ")
    if p_rsp == "q":
        p_rsp = 1
    elif p_rsp == "w":
        p_rsp = 2
    elif p_rsp == "e":
        p_rsp = 3
    else:
        print("올바른 문자를 입력하세요\n")
        p_rsp = 0

    if p_rsp != 0:
        c_rsp = randint(1,3)

        if c_rsp == 3 and p_rsp == 1:
            p_rsp = 4
        if c_rsp == 1 and p_rsp == 3:
            c_rsp = 4

        if p_rsp - c_rsp == -1:
            win = 2
        elif p_rsp - c_rsp == 0:
            win = 0
        elif p_rsp - c_rsp == 1:
            win = 1

        if p_rsp == 1 or p_rsp == 4:
            p_rsp = "가위"
        elif p_rsp == 2:
            p_rsp = "바위"
        elif p_rsp == 3:
            p_rsp = "보"

        if c_rsp == 1 or c_rsp == 4:
            c_rsp = "가위"
        elif c_rsp == 2:
            c_rsp = "바위"
        elif c_rsp == 3:
            c_rsp = "보"

        if win == 0:
            win = "무승부"
        elif win == 1:
            win = "승리"
        elif win == 2:
            win = "패배"

        print("\n{0:=^25}".format("결과"))
        print("플레이어 = {0}".format(p_rsp))
        print("com_1 = {0}".format(c_rsp))
        print("승패여부 = {0}".format(win))
        input()

from random import randint
from time import sleep

print("\n청소구역 배정 프로그램\n")

class division:
    def __init__(self, name, max, now, list):
        self.name = name
        self.max = max
        self.now = now
        self.list = []

div_1 = division("칠판 닦기", 2, 0, [])
div_2 = division("교탁,사물함 닦기", 2, 0, [])
div_3 = division("창문턱,거울 닦기", 1, 0, [])
div_4 = division("쓸기", 3, 0, [])
div_5 = division("줄 맞추기", 3, 0, [])
div_6 = division("교실 닦기", 3, 0, [])
div_7 = division("복도 쓸고 닦기", 1, 0, [])
div_8 = division("분리수거", 2, 0, [])
div_9 = division("환경도우미", 2, 0, [])
div_10 = division("교목실", 5, 0, [])

div_list = [div_1, div_2, div_3, div_4, div_5, \
            div_6, div_7, div_8, div_9, div_10]


def main():
    input("시작하려면 아무키나 누르세요.")
    print("\n")

    sleep(0.5)

    while True:
        st_num = input("시작 번호를 입력하십시오. : ")
        if st_num.isdigit():
            st_num = int(st_num)
            if st_num >= 1:
                break
            else:
                print("1보다 큰 숫자를 입력하십시오\n")
        else:
            print("유효한 숫자를 입력하십시오\n")

    print()

    while True:
        ed_num = input("마지막 번호를 입력하십시오. : ")
        if ed_num.isdigit():
            ed_num = int(ed_num)
            if ed_num > st_num:
                break
            else:
                print("시작번호보다 큰 숫자를 입력하십시오\n")
        else:
            print("유효한 숫자를 입력하십시오\n")

    print()

    all_list = []
    i = st_num - 1
    while i != ed_num:
        i += 1
        all_list.append(i)

    except_list = []

    while True:
        ex_num = input("제외할 번호를 입력하십시오. : ")
        if ex_num != "":
            if ex_num.isdigit():
                if st_num <= int(ex_num) <= ed_num:
                    try:
                        all_list.remove(int(ex_num))
                        except_list.append(ex_num)
                    except:
                        print("이미 제외된 숫자입니다.\n")
                else:
                    print("숫자가 범위안에 있지 않습니다.\n")
        else:
            break

    print("\n\n")
    print("인식된 모든 번호 : ")
    print(all_list)
    print("제외된 모든 번호 : ")
    print(except_list)
    print()

    ter_num = 0
    for i in range(len(div_list)):
        ter_num += div_list[i].max - div_list[i].now

    print("배치 가능한 자리 개수 : {0} / {1}".format(ter_num, len(all_list)))

    if ter_num > len(all_list):
        print("(* 누락된 자리가 생길 수 있습니다.)")
    elif ter_num < len(all_list):
        print("(* 누락된 인원이 생길 수 있습니다.)")
    print("\n")

    plag = input("시작하려면 엔터")
    if plag == 'stop':
        main()

    sleep(2)

    print("\n" * 15)
    print("청소구역 역할분배를 시작합니다.")
    print("\n\n")

    while True:
        num = randint(0, len(all_list))
        num = all_list[num - 1]
        i = randint(0, len(div_list) - 1)

        if div_list[i].max > div_list[i].now:
            div_list[i].list.append(num)
            div_list[i].now += 1
            all_list.remove(num)

        if len(all_list) == 0:
            break

    i = 0
    while i < len(div_list):
        sleep(0.4)
        print("{0}({1} / {2})".format(div_list[i].name, div_list[i].now, div_list[i].max))
        print()
        print(div_list[i].list)
        print("\n")
        i += 1

    re = input("다시 시작하려면 'restrat'를 입력하십시오")
    if re == "restrart":
        main()

if __name__ == "__main__":
    main()

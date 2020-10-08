# import 정의

from random import randint
import time
import datetime


# 이름 불러오기 모듈

name = 0

try:
    import name_file
    name = 1
except:
    name = 0


# 저장위치

storage_location = '/Users/hwang_jeonggyu/Desktop/'


# 연산 방법

operator_method = '1'


# 소개

print("\n청소구역 배정 프로그램 (V.2)\n")


# 부서 정의

class division:
    def __init__(self, name, max, now, list):
        self.name = name
        self.max = max
        self.now = now
        self.list = []

div_0 = division("(제외 인원)", 0, 0, [])
div_1 = division("칠판 닦기", 2, 0, [])
div_2 = division("교탁,사물함 닦기", 2, 0, [])
div_3 = division("창문턱,거울 닦기", 1, 0, [])
div_4 = division("쓸기", 3, 0, [])
div_5 = division("줄 맞추기", 3, 0, [])
div_6 = division("교실 닦기", 3, 0, [])
div_7 = division("복도 쓸고 닦기", 1, 0, [])
div_8 = division("분리수거", 2, 0, [])
div_9 = division("환경도우미", 1, 0, [])
div_10 = division("교목실", 5, 0, [])

div_list = [div_0, div_1, div_2, div_3, div_4, div_5, div_6, div_7, div_8, div_9, div_10]


# 메인

def main():
    input("시작하려면 아무키나 누르세요.")
    print("\n")

    # 시작번호 입력

    while True:
        st_num = input("시작 번호를 입력하십시오. : ")
        if st_num.isdigit():
            st_num = int(st_num)
            if st_num >= 1:
                break
            else:
                print("0보다 큰 숫자를 입력하십시오\n")
        else:
            print("유효한 자연수를 입력하십시오\n")


    # 마지막 번호 입력

    while True:
        ed_num = input("\n마지막 번호를 입력하십시오. : ")
        if ed_num.isdigit():
            ed_num = int(ed_num)
            if ed_num > st_num:
                break
            else:
                print("시작번호보다 큰 숫자를 입력하십시오")
        elif ed_num == '-':
            while True:
                st_num = input("\n시작 번호를 입력하십시오. : ")
                if st_num.isdigit():
                    st_num = int(st_num)
                    if st_num >= 1:
                        break
                    else:
                        print("0보다 큰 숫자를 입력하십시오")
                else:
                    print("유효한 자연수를 입력하십시오")
        else:
            print("유효한 자연수를 입력하십시오")

    print()


    # 시작 - 마지막 리스트 제작

    all_list = []
    i = st_num - 1
    while i != ed_num:
        i += 1
        all_list.append(i)


    # 특수명령 정리

    except_list = []

    while True:
        print()
        print("제외(q) / 추가(w) / 이동(e) / 인식된 숫자 보기 (r) /  건너뛰기(enter)")
        sel = input(": ")
        print()


        # 원소 제외

        if sel == "q":

            while True:
                ex_num = input("제외할 번호를 입력하십시오. : ")
                if ex_num != "":
                    if ex_num.isdigit():
                        if st_num <= int(ex_num) <= ed_num:
                            try:
                                all_list.remove(int(ex_num))
                                except_list.append(int(ex_num))
                                print("\n성공적으로 제외되었습니다.\n\n")
                            except:
                                print("이미 제외된 숫자입니다.\n")
                        else:
                            print("숫자가 범위안에 있지 않습니다.\n")
                    else:
                        print("유효한 자연수를 입력하십시오.\n")
                else:
                    break


        # 원소 추가

        elif sel == "w":

            while True:
                pu_num = input("추가할 번호를 입력하십시오. : ")
                if pu_num != "":
                    if pu_num.isdigit():
                        if int(pu_num) not in all_list:
                            all_list.append(int(pu_num))
                            try:
                                except_list.remove(int(ex_num))
                            except:
                                pass
                            print("\n성공적으로 추가되었습니다.\n\n")
                        else:
                            print("이미 추가된 숫자입니다.\n")
                    else:
                        print("유효한 자연수를 입력하십시오.\n")
                else:
                    break


        # 특정부서로 연결

        elif sel == "e":

            while True:
                print()
                num = 0
                for i in div_list:
                    print("{0}. {1} {2}/{3} {4}".format(num, i.name, i.now, i.max, i.list))
                    num += 1
                print()
                in_num = input("특정부서에 넣을 번호를 입력하십시오. : ")
                if in_num != '':
                    if in_num.isdigit():


                        # 원소 이동

                        if int(in_num) in all_list:
                            in_div = input("해당번호를 넣을 부서를 선택하십시오. : ")
                            if in_div.isdigit():
                                in_div = int(in_div)
                                if int(in_div) in range(len(div_list)):
                                    all_list.remove(int(in_num))
                                    div_list[in_div].list.append(int(in_num))
                                    div_list[in_div].now += 1
                                    print("\n성공적으로 추가되었습니다.\n\n")
                                else:
                                    print("유효한 부서 번호를 입력하십시오.\n")
                            else:
                                print("유효한 자연수를 입력하십시오.\n")


                        # 원소 제거

                        else:
                            out = input ("이미 이동되었거나 숫자가 범위 안에 있지 않습니다.\n특정부서에서 제외하시겠습니까? : ")
                            if out ==  "yes" or out ==  "y":
                                print()
                                out_div = input("해당번호를 제외할 부서를 선택하십시오. : ")
                                if out_div.isdigit():
                                    out_div = int(out_div)
                                    if int(out_div) in range(len(div_list)):
                                        if int(in_num) in div_list[out_div].list:
                                            all_list.append(int(in_num))
                                            div_list[out_div].list.remove(int(in_num))
                                            div_list[out_div].now -= 1
                                            print("\n성공적으로 제되었습니다.\n\n")
                                        else:
                                            print("해당 부서에 특정 숫자가 없습니다.\n")
                                    else:
                                        print("유효한 부서 번호를 입력하십시오.\n")
                                else:
                                    print("유효한 자연수를 입력하십시오.\n")
                            else:
                                print()
                    else:
                        print("유효한 자연수를 입력하십시오.\n")
                else:
                    break


        # 리스트 미리보기

        elif sel == "r":
            print("\n인식된 모든 번호 : ")
            print(all_list)
            input("\n(되돌아가려면 엔터)")


        # 브레이크 (1)

        elif sel == "y":
            break


        # 브레이크 (2)

        elif sel == "enter" or sel == "":
            nex = input("이대로 진행하시겠습니까? : ")
            if nex == "y" or nex == "yes":
                break
            print()


        # 예외설정

        else:
            print()


    # 출력방법 선택

    print()

    while True:
        output_method = input("출력 방법을 선택하십시오. : ")
        if output_method == 'name' or output_method == 'number':
            if output_method == 'name' and name == 0:
                print("\n'name_file'을 찾지 못하였습니다.")
                output_method = 'number'
            break
        else:
            print("유효한 출력 방법을 입력해주십시오.\n")


    # 리스트 확인

    print("\n\n")
    print("인식된 모든 번호 : ")
    print(all_list)
    print("제외된 모든 번호 : ")
    print(except_list)
    print()


    # 총 자리 확인

    ter_num = 0
    for i in range(len(div_list)):
        ter_num += div_list[i].max - div_list[i].now


    # 누락 확인

    print("배치 가능한 자리 개수 : {0} / {1}".format(ter_num, len(all_list)))

    if ter_num > len(all_list):
        print("(* 누락된 자리가 생길 수 있습니다.)")
    elif ter_num < len(all_list):
        print("(* 누락된 인원이 생길 수 있습니다.)")
    print("\n")


    input("(시작하려면 엔터)")


    print("\n"*30)
    print("청소구역 역할분배를 시작합니다.\n")


    # 파일 포멧

    nowdate = datetime.datetime.now()
    save_file = open(storage_location + nowdate.strftime("%y%m%d_%H%M%S") + '.txt', 'w')
    save_file.write(nowdate.strftime("%Y-%m-%d %H:%M:%S.%f") + "\n\n")
    save_file.write("시작번호 : {0} / 마지막번호 : {1}".format(st_num, ed_num) + "\n\n")
    save_file.write("인식된 모든 번호 : {0}".format(all_list) + "\n")
    save_file.write("제외된 모든 번호 : {0}".format(except_list) + "\n\n")
    save_file.write("출력방법 : {0}".format(output_method) + "\n\n\n")

    start = time.time()

    # 분배

    save_file.write("연산방법 : {0}".format(operator_method) + "\n\n\n")

    if operator_method == '1':

        while True:
            plo = 0
            plo_list = []
            i = randint(1, len(div_list) - 1)

            while div_list[i].now != 0:
                i = randint(1, len(div_list) - 1)

            while plo != int(div_list[i].max):

                if len(all_list) == 0:
                    break

                num = randint(0, len(all_list))
                num -= 1
                num = all_list[num]
                div_list[i].now += 1
                plo_list.append(num)
                all_list.remove(num)
                plo += 1
                ter_num -= 1

            div_list[i].list = plo_list

            if len(all_list) == 0 or ter_num == 0:
                break

    elif operator_method == '2':

        while True:
            print()
            num = randint(0, len(all_list))
            num = all_list[num - 1]
            i = randint(1, len(div_list) - 1)

            if div_list[i].max > div_list[i].now:
                div_list[i].list.append(num)
                div_list[i].now += 1
                all_list.remove(num)
                ter_num -= 1

            if len(all_list) == 0 or ter_num == 0:
                break

    for i in range(len(div_list)):
        div_list[i].list.sort


    show_time = time.time() - start


    # 출력

    i = 0
    for i in range(len(div_list)):
        if div_list[i].now > 0:
            print("{0} ({1} / {2})".format(div_list[i].name, div_list[i].now, div_list[i].max))
            save_file.write("{0} ({1} / {2})".format(div_list[i].name, div_list[i].now, div_list[i].max) + "\n")
            div_list[i].list.sort()

            if output_method == 'name':
                for j in div_list[i].list:
                    print(name_file.name(j), end=' ')
                    save_file.write(str(name_file.name(j)) + " ")
                print("\n")
                save_file.write("\n\n")

            elif output_method == 'number':
                print(div_list[i].list)
                save_file.write("{0}".format(div_list[i].list))
                print()
                save_file.write("\n\n")


    # 경과시간 표시

    print("time : {0}\n".format(show_time))


    # 파일 저장

    save_file.close()

    print("성공적으로 파일이 저장되었습니다. (" + nowdate.strftime("%y%m%d_%H%M%S") + ".txt" + ")")
    print("저장위치 : " + storage_location)

if __name__ == "__main__":
    main()

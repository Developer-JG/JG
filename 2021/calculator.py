print("\ncalculator_project")


def factoriacl(number):
    result = 1
    for i in range(1 , number + 1):
        result *= i
    return result

def main():
    while True:
        all_sequence = 1
        number_sequence = 0
        operator_sequence = 0
        parentheses_count = 0
        open_parentheses_count = 0
        number_list = []
        operator_list = []
        list = []

        while True:
            print("\n" * 2)

            if len(list) > 0:
                for i in range(len(list)):
                    i = list[i]
                    if i == "a" or i == "b" or i == "c" or i == "d" or i == "e" or i == "f" or i == "g" or i == "h":
                        if i == "a" :
                            print('+', end=' ')
                        elif i == "b" :
                            print('-', end=' ')
                        elif i == "c" :
                            print('*', end=' ')
                        elif i == "d" :
                            print('/', end=' ')
                        elif i == "e" :
                            print('**', end=' ')
                        elif i == "f" :
                            print('//', end=' ')
                        elif i == "g" :
                            print('%', end=' ')
                        elif i == "h" :
                            print('!', end=' ')
                    else:
                        print(i, end=' ')
            else:
                print()
            print()

            if all_sequence % 2 == 0:
                operator_area_sequence = (all_sequence / 2) + operator_sequence
                print(f"\n{round(operator_area_sequence)} 번째 연산자를 입력하세요.")
            else:
                number_area_sequence = ((all_sequence + 1) / 2) + number_sequence
                print(f"\n{round(number_area_sequence)} 번째 숫자를 입력하세요.")

            ans = input("= ")
            print("\n" * 1)

            if ans != "=" and ans != "(" and ans != ")" and ans != "b":
                plag = 0
                operator_separation = "-"
                number_separation = 0
                if all_sequence % 2 == 0:
                    if ans == "+" or ans == "더하기" or ans == "addition":
                        operator_separation = "a"
                    elif ans == "-" or ans == "빼기" or ans == "subtraction":
                        operator_separation = "b"
                    elif ans == "*" or ans == "x" or ans == "곱하기" or ans == "multiplication":
                        operator_separation = "c"
                    elif ans == "/" or ans == "나누기" or ans == "division":
                        operator_separation = "d"
                    elif ans == "**" or ans == "^" or ans == "제곱" or ans == "square":
                        operator_separation = "e"
                    elif ans == "//" or ans == "몫" or ans == "quota":
                        operator_separation = "f"
                    elif ans == "%" or ans == "나머지" or ans == "remainder":
                        operator_separation = "g"
                    elif ans == "!" or ans == "팩토리얼" or ans == "계승" or ans == "factorial":
                        operator_separation = "h"
                        all_sequence += 1
                        number_sequence += 1
                    else:
                        plag = 1
                else:
                    if ans.isdigit() == True:
                        number_separation = int(ans)
                    elif ans.isdigit() == False:
                        plag = 1

                try:
                    if operator_separation != "-":
                        operator_list.append(operator_separation)
                        list.append(operator_separation)
                    elif number_separation != 0:
                        number_list.append(number_separation)
                        list.append(number_separation)
                except:
                    plag = 1

                if plag == 0:
                    all_sequence += 1
                elif plag == 1:
                    if all_sequence % 2 == 0:
                        print("올바른 연산자를 입력하세요.")
                    else:
                        print("올바른 숫자를 입력하세요.")

            elif ans == "b":
                del list[-1]
                if all_sequence % 2 == 0:
                    del number_list[-1]
                else:
                    del operator_list[-1]
                all_sequence -= 1

            elif ans == "(":
                if all_sequence % 2 == 0:
                    print("연산자 뒤에 여는 괄호를 입력하여 주십시오")
                else:
                    parentheses_count += 1
                    open_parentheses_count += 1
                    list.append(ans)

            elif ans == ")":
                if all_sequence % 2 != 0:
                    print("숫자 뒤에 닫는 괄호를 입력하여 주십시오.")
                else:
                    if parentheses_count > 0:
                        parentheses_count -= 1
                        list.append(ans)
                    else:
                        print("여는 괄호를 먼저 입력하여 주십시오.")

            elif ans == "=":
                if all_sequence % 2 != 0:
                    print("숫자 뒤에 등호를 입력하여 주십시오.")
                else:
                    if parentheses_count == 0:
                        break
                    else:
                        print("괄호를 모두 닫아 완전한 식을 입력하여 주십시오.")

        # 팩토리얼
        delete_count = 0
        for i in range(len(list)):
            i -= delete_count
            if list[i] == "h":
                del list[i]
                list[i - 1] = factoriacl(int(list[i - 1]))
                delete_count += 1

        # 괄호
        while open_parentheses_count != 0:
            open_parentheses_list = []
            close_parentheses_list = []
            for i in range(len(list)):
                j = list[i]
                if j == "(":
                    open_parentheses_list.append(i)
                elif j == ")":
                    close_parentheses_list.append(i)

            close_parentheses_list.sort()
            open_parentheses_list.sort(reverse = True)
            parentheses_list = []
            delete_count = 0
            for i in range(len(open_parentheses_list)):
                for j in range(len(list)):
                    j -= delete_count
                    if open_parentheses_list[i] <= j <= (close_parentheses_list[i] - delete_count):
                        parentheses_list.append(list[j])
                        del list[j]
                        delete_count += 1
                del parentheses_list[0]
                del parentheses_list[-1]

                delete_count = 0
                for i in range(len(parentheses_list)):
                    i -= delete_count
                    try:
                        if parentheses_list[i] == "g" or parentheses_list[i] == "f":
                            if parentheses_list[i] == "g":
                                result = int(parentheses_list[i - 1]) % int(parentheses_list[i + 1])
                            elif parentheses_list[i] == "f":
                                result = int(parentheses_list[i - 1]) // int(parentheses_list[i + 1])
                            parentheses_list[i - 1] = result
                            del parentheses_list[i]
                            del parentheses_list[i + 1]
                    except:
                        pass

                delete_count = 0
                for i in range(len(parentheses_list)):
                    i -= delete_count
                    try:
                        if parentheses_list[i] == "e":
                            result = int(parentheses_list[i - 1]) ** int(parentheses_list[i + 1])
                            parentheses_list[i - 1] = result
                            del parentheses_list[i]
                            del parentheses_list[i + 1]
                    except:
                        pass

                delete_count = 0
                for i in range(len(parentheses_list)):
                    i -= delete_count
                    try:
                        if parentheses_list[i] == "d" or parentheses_list[i] == "c":
                            if parentheses_list[i] == "d":
                                result = int(parentheses_list[i - 1]) / int(parentheses_list[i + 1])
                            elif parentheses_list[i] == "c":
                                result = int(parentheses_list[i - 1]) * int(parentheses_list[i + 1])
                            parentheses_list[i - 1] = result
                            del parentheses_list[i]
                            del parentheses_list[i + 1]
                    except:
                        pass

                delete_count = 0
                for i in range(len(parentheses_list)):
                    i -= delete_count
                    try:
                        if parentheses_list[i] == "b" or parentheses_list[i] == "a":
                            if parentheses_list[i] == "b":
                                result = int(parentheses_list[i - 1]) - int(parentheses_list[i + 1])
                            elif parentheses_list[i] == "a":
                                result = int(parentheses_list[i - 1]) + int(parentheses_list[i + 1])
                            parentheses_list[i - 1] = result
                            del parentheses_list[i]
                            del parentheses_list[i + 1]
                    except:
                        pass

            open_parentheses_count -= 1

        # 계산
        delete_count = 0
        for i in range(len(list)):
            i -= delete_count
            try:
                if list[i] == "g" or list[i] == "f":
                    if list[i] == "g":
                        result = int(list[i - 1]) % int(list[i + 1])
                    elif list[i] == "f":
                        result = int(list[i - 1]) // int(list[i + 1])
                    list[i - 1] = result
                    del list[i]
                    del list[i + 1]
            except:
                pass

        delete_count = 0
        for i in range(len(list)):
            i -= delete_count
            try:
                if list[i] == "e":
                    result = int(list[i - 1]) ** int(list[i + 1])
                    list[i - 1] = result
                    del list[i]
                    del list[i + 1]
            except:
                pass

        delete_count = 0
        for i in range(len(list)):
            i -= delete_count
            try:
                if list[i] == "d" or list[i] == "c":
                    if list[i] == "d":
                        result = int(list[i - 1]) / int(list[i + 1])
                    elif list[i] == "c":
                        result = int(list[i - 1]) * int(list[i + 1])
                    list[i - 1] = result
                    del list[i]
                    del list[i + 1]
            except:
                pass

        delete_count = 0
        for i in range(len(list)):
            i -= delete_count
            try:
                if list[i] == "b" or list[i] == "a":
                    if list[i] == "b":
                        result = int(list[i - 1]) - int(list[i + 1])
                    elif list[i] == "a":
                        result = int(list[i - 1]) + int(list[i + 1])
                    list[i - 1] = result
                    del list[i]
                    del list[i + 1]
            except:
                pass

        print(f"= {list[0]}", end= ' ')


if __name__ == "__main__":
    main()
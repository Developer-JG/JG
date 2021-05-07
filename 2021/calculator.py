print("\ncalculator_project\n")


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
        while True:
            if all_sequence % 2 == 0:
                operator_area_sequence = (all_sequence / 2) + operator_sequence
                print(f"{round(operator_area_sequence)} 번째 연산자를 입력하세요.")
            else:
                number_area_sequence = ((all_sequence + 1) / 2) + number_sequence
                print(f"{round(number_area_sequence)} 번째 숫자를 입력하세요.")

            ans = input("= ")

            if ans != "=":
                plag = 0
                operator_separation = 0
                if all_sequence % 2 == 0:
                    if ans == "+" or ans == "더하기" or ans == "addition":
                        operator_separation = 1
                    elif ans == "-" or ans == "빼기" or ans == "subtraction":
                        operator_separation = 2
                    elif ans == "*" or ans == "x" or ans == "곱하기" or ans == "multiplication":
                        operator_separation = 3
                    elif ans == "/" or ans == "나누기" or ans == "division":
                        operator_separation = 4
                    elif ans == "**" or ans == "^" or ans == "제곱" or ans == "square":
                        operator_separation = 5
                    elif ans == "//" or ans == "몫" or ans == "quota":
                        operator_separation = 6
                    elif ans == "%" or ans == "나머지" or ans == "remainder":
                        operator_separation = 7
                    elif ans == "!" or ans == "팩토리얼" or ans == "계승" or ans == "factorial":
                        operator_separation = 8
                    else:
                        plagplag = 1
                else:
                    if ans.isdigit() == True:
                        pass
                    elif ans.isdigit() == False:
                        plag = 1


                if plag == 0:
                    all_sequence += 1
                elif plag == 1:
                    if all_sequence % 2 == 0:
                        print("올바른 연산자를 입력하세요.")
                    else:
                        print("올바른 숫자를 입력하세요.")
            elif ans == "=":


if __name__ == "__main__":
    main()
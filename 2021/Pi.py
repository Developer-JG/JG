print("Pi project")


def factoriacl(number):
    result = 1
    for i in range(1 , number + 1):
        result *= i
    return result


def prime_number(number):
    if number != 1:
        for i in range(2,number):
            if number % i == 0:
                return False
    else:
        return False
    return True


def Franciscus_Vieta(value, p_count):
    count = 0
    try:
        while True:
            count += 1
            if value == 0:
                value_1 = ((2 ** (1 / 2)) / 2)
                value_2 = (2 ** (1 / 2))
                value += value_1
            else:
                value_1 = (((2 + value_2) ** (1 / 2)) / 2)
                value_2 = ((2 + value_2) ** (1 / 2))
                value *= value_1
            if count % p_count == 0:
                print(value_1)
                print("{0}회 시행 : {1:.256g}".format(count ,2 / value))
                input()
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def John_Wallis(value, p_count):
    count = 0
    n = 1
    try:
        while True:
            count += 1
            if value == 0:
                value += ((2 * n) / ((2 * n) - 1)) * ((2 * n) / ((2 * n) + 1))
            else:
                value *= ((2 * n) / ((2 * n) - 1)) * ((2 * n) / ((2 * n) + 1))
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,value * 2))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def James_Gregory_and_Leibniz(value, p_count):
    count = 0
    n = 0
    try:
        while True:
            count += 1
            value += ((-1) ** n) / ((2 * n) + 1)
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,value * 4))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def John_Machin(value, p_count):
    count = 0
    n = 1
    try:
        while True:
            count += 1
            value += (((4 * ((-1) ** (n - 1))) / ((2 * n) - 1)) * ((1 / 5) ** ((2 * n) - 1))) - \
                     (((-1) ** (n - 1)) / ((2 * n) - 1) * (1 / 239))
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,value * 4))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_1(value, p_count):
    count = 0
    n = 1
    try:
        while True:
            count += 1
            value += 1 / (n ** 2)
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,(value * 6) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_2(value, p_count):
    count = 0
    n = 0
    try:
        while True:
            count += 1
            value += 1 / ((1 + 2 * n) ** 2)
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,(value * 8) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_3(value, p_count):
    count = 0
    n = 1
    try:
        while True:
            count += 1
            value += (((-1) ** (n + 1)) / (n ** 2))
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,(value * 12) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Euler_prim(value, p_count):
    count = 0
    n = 2
    try:
        while True:
            if prime_number(n) == True:
                count += 1
                if  value == 0:
                    value += ((n ** 2) / ((n ** 2) - 1))
                else:
                    value *= ((n ** 2) / ((n ** 2) - 1))
                if count % p_count == 0:
                    print("{0}회 시행 : {1:.256g}".format(count ,(value * 6) ** (1 / 2)))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def Ramanujan(value, p_count):
    count = 0
    n = 0
    try:
        while True:
            count += 1
            value_1 = factoriacl(4 * n) / factoriacl(n)
            value_2 = ((26390 * n) + 1103) / (396 ** (4 * n))
            value_0 = value_1 * value_2
            value += value_0
            if count % p_count == 0:
                print("{0}회 시행 : {1:.256g}".format(count ,((2 * (2 ** (1 / 2))) / (99 ** 2) * value) ** -1))
            n += 1
    except:
        input("program is stoped")
        print("\n" * 2)
        main()


def main():
    count = 1
    value = 0
    while True:
        sel = input(" : ")

        if sel == 'Franciscus_Vieta':
            Franciscus_Vieta(value, count)
        elif sel == 'John_Wallis':
            John_Wallis(value, count)
        elif sel == 'James_Gregory_and_Leibniz':
            James_Gregory_and_Leibniz(value, count)
        elif sel == 'John_Machin':
            John_Machin(value, count)
        elif sel == 'Euler_1':
            Euler_1(value, count)
        if sel == 'Euler_2':
            Euler_2(value, count)
        elif sel == 'Euler_3':
            Euler_3(value, count)
        elif sel == 'Euler_prim':
            Euler_prim(value, count)
        elif sel == 'Ramanujan':
            Ramanujan(value, count)


if __name__ == "__main__":
    main()
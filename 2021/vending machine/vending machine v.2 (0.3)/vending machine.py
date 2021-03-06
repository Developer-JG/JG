from random import randint

print("vending machine project\n")

class player:
    def __init__(self, money_50000, money_10000, money_5000, money_1000, money_500, money_100, money_50, money_10, inventory):
        self.money = {"50,000" : money_50000, "10,000" : money_10000, "5,000" : money_5000, "1,000" : money_1000,
                      "500" : money_500, "100" : money_100, "50" : money_50, "10" : money_10}
        self.inventory = []

class machine:
    def __init__(self, money_50000, money_10000, money_5000, money_1000, money_500, money_100, money_50, money_10):
        self.money = {"50,000": money_50000, "10,000": money_10000, "5,000": money_5000, "1,000": money_1000,
                      "500": money_500, "100": money_100, "50": money_50, "10": money_10}

class menu:
    def __init__(self, name, price, m_count, p_count):
        self.name = name
        self.price = price
        self.m_count = m_count
        self.p_count = p_count

menu_1 = menu("코카콜라", 1000, randint(10, 20), 0)
menu_2 = menu("스프라이트", 1000, randint(10, 20), 0)
menu_3 = menu("환타_오렌지", 1000, randint(10, 20), 0)
menu_4 = menu("밀크소다_암바사", 1000, randint(10, 20), 0)
menu_5 = menu("코레타", 1800, randint(10, 20), 0)
menu_6 = menu("피워에이드", 1500, randint(10, 20), 0)
menu_7 = menu("선키스트_자몽", 1500, randint(10, 20), 0)
menu_8 = menu("코코팜", 1000, randint(10, 20), 0)
menu_9 = menu("미닛메이드_사과", 900, randint(10, 20), 0)
menu_10 = menu("코코팜_포도", 1000, randint(10, 20), 0)
menu_11 = menu("조지아_카페라떼", 1000, randint(10, 20), 0)
menu_12 = menu("조지아_맥스", 1000, randint(10, 20), 0)
menu_13 = menu("조지아_오리지널", 700, randint(10, 20), 0)
menu_14 = menu("벌꿀유자", 900, randint(10, 20), 0)
menu_15 = menu("삼다수", 1000, randint(10, 20), 0)
menu_16 = menu("큰집식혜", 1000, randint(10, 20), 0)

menu_list = [menu_1, menu_2, menu_3, menu_4, menu_5, menu_6, menu_7, menu_8,
             menu_9, menu_10, menu_11, menu_12, menu_13, menu_14, menu_15, menu_16]

def buy():
    print("-")

def vending_machine():
    plag = 0
    n = 3

    print("\n" * 2)

    while True:

        print("{0:=^25}".format(" 자판기 (" + str(plag + 1) + " 페이지) "))

        j = plag * n
        for i in range(plag * (n - 1), plag * (n - 1) + n):
            j = j + 1
            try:
                print(f"{j}. {menu_list[plag + i].name} : {menu_list[plag + i].price}")
            except:
                print()

        print("\n이전 페이지 : q / 다음 페이지 : w / [음료를 구매하려면 번호 입력]")

        answer = input(": ")
        if answer == "q":
            if 1 == plag + 1:
                plag = (len(menu_list)//n)
            else:
                plag = plag - 1
            print("\n" * 2)
        elif answer == "w":
            if (len(menu_list)//n) + 1 == plag + 1:
                plag = 0
            else:
                plag = plag + 1
            print("\n" * 2)

        try:
            if 1 <= int(answer) <= len(menu_list):
                buy()
            else:
                print("\n유효한 숫자를 입력하세요.\n")
        except:
            if answer != "q" or answer != "w":
                print("\n다시 입력해 주십시오.\n")

def main():
    print("\n" * 2)
    print("(이 게임은 9칸의 로그 화면을 요구합니다.)\n")
    input("게임을 시작하려면 엔터")

    player_1 = player(2, 0, 0, 0, 0, 0, 0, 0, [])

    vending_machine()



if __name__ == "__main__":
    main()

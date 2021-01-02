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

def vending_machine():
    while True:
        print("\n" * 2)
        print("구겨진 지폐, 불량동전 투입금지")
        input(": ")

def main():
    print("\n" * 2)
    print("(이 게임은 9칸의 로그 화면을 요구합니다.)\n")
    input("게임을 시작하려면 엔터")

    player_1 = player(2, 0, 0, 0, 0, 0, 0, 0, [])

    vending_machine()



if __name__ == "__main__":
    main()

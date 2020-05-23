from random import choice
from random import randint
import time
import math

print("\nthe Martial Arts RPG game project\n")

po_count = 0
ag_count = 0
ad_count = 0

# 체크
def check(message, start, end):
    if message in list(map(str, range(start, end + 1))):
        message = int(message)
        return message
    else:
        return message

# 플레이어 클래스
class Player:
    def __init__(self, name, Arena, point, health, M_martial_arts_equipment, S_martial_arts_equipment, inven, condition, money, liv, exp):
        self.name = name
        self.Arena = Arena
        self.point = point
        self.health = health
        self.M_martial_arts_equipment = {"M_martial_arts_1": ["없음"], "M_martial_arts_2": ["없음"], "M_martial_arts_3": ["없음"], "M_martial_arts_4": ["없음"]}
        self.S_martial_arts_equipment = {"s_martial_arts_1": ["없음"], "s_martial_arts_2": ["없음"]}
        self.inven = {"main_martial_arts": [], "sub_martial_arts": [], "item": []}
        self.condition = condition
        self.money = money
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        player_arena = change_3(self.Arena)
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n레벨 : {self.liv}\n아레나 : {player_arena}\n점수 : {self.point}\n돈 : {self.money}")

    # 전투중 상태,무공 확인
    def F_showinfo(self):
        player_condition = change_2(self)
        print(f"{'나의 상태':=^25}\n이름 : {self.name}\n상태 : {player_condition}\n체력 : {self.health}")
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

    # 장착 무술 보기 1
    def m_martial_arts_equipment(self):
        if len(self.M_martial_arts_equipment['M_martial_arts_1']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_1'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_2']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_2'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_3']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_3'][0]}")

        if len(self.M_martial_arts_equipment['M_martial_arts_4']) == 2:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][1].name}")
        else:
            print(f"1.{self.M_martial_arts_equipment['M_martial_arts_4'][0]}")

    # 장착 무술 보기 2
    def s_martial_arts_equipment(self):
        if len(self.S_martial_arts_equipment['S_martial_arts_1']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_1'][0]}")

        if len(self.S_martial_arts_equipment['S_martial_arts_2']) == 2:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][1].name}")
        else:
            print(f"1.{self.S_martial_arts_equipment['S_martial_arts_2'][0]}")

# 무공 클래스
class Martial_arts:
    def __init__(self, name, explanation, system, cool_time, count, use):
        self.name = name
        self.explanation = explanation
        self.system = system
        self.cool_time = cool_time
        self.count = count
        self.use = use

# 메인 무공
main_01 = Martial_arts("용승권","1턴간 상대를 공격불능 상태로 만들고 5데미지를 준다.","패왕권법",2,25,'main')
main_02 = Martial_arts("침무묵","2턴간 상대를 공격불능 상태로 만든다.","패왕권법",3,20,'main')
main_03 = Martial_arts("금강불괴","내 데미지를 2턴간 50%으로 낮추고 상대방의 크리티컬 확률을 높인다.","패왕권법",3,15,'main')
main_04 = Martial_arts("호장파풍","상대방에게 20 데미지를 주고 상대방을 1턴간 공격불능 상태로 만든다.","패왕권법",2,10,'main')
main_05 = Martial_arts("패왕오의","4턴간 상대를 공격불능 상태로 만들고 턴당 10데미지를 준다.","패왕권법",5,5,'main')
main_06 = Martial_arts("속박공","상대방에게 10에서 20데미지를 주고 스턴을 1턴간 건다.","반야술법",2,25,'main')
main_07 = Martial_arts("섬무광탄","상대방을 5턴간 크리티컬 확률을 낮춘다. (20%)","반야술법",5,20,'main')
main_08 = Martial_arts("시간역행","무공 쿨타임을 모두 없앤다.","반야술법",6,15,'main')
main_09 = Martial_arts("호신강기","나와 상대방의 데미지를 2턴간 0으로 한다.","반야술법",6,10,'main')
main_10 = Martial_arts("반야수인","나의 크리티컬확률을 1턴간 100%로 하고 상대방을 공격불능 상태로 만든다.","반야술법",2,5,'main')
main_11 = Martial_arts("여래장","상대방에게 10데미지를 주고 2턴간 상대의 크리티컬확률이 매우 낮아진다. (5%)","여래장법",3,25,'main')
main_12 = Martial_arts("오운천수","상대방에게 20데미지를 주고 5턴간 5데미지를 준다.","여래장법",6,20,'main')
main_13 = Martial_arts("여강래회","2턴간 나의 크리티컬 확률이 올라간다. (80%)","여래장법",3,15,'main')
main_14 = Martial_arts("폭발수인","1턴뒤 상대에게 20에서 40데미지를 준다.","여래장법",3,10,'main')
main_15 = Martial_arts("여래수장","내 체력을 50 깎고 상대에게 40데미지를 준다.","여래장법",5,5,'main')
main_16 = Martial_arts("태극의장","5턴간 상대방의 크리티컬 확률을 5%로 한다.","태극조화법",6,25,'main')
main_17 = Martial_arts("의선의술","상대방의 체력을 80%로 회복시킨다.","태극조화법",5,20,'main')
main_18 = Martial_arts("회복의술","나의 체력을 50% 회복시킨다.","태극조화법",5,15,'main')
main_19 = Martial_arts("화룡강림","상대방을 2턴간 10데미지를 주고 50% 확률로 나의 데미지를 2턴간 무시한다.","태극조화법",3,10,'main')
main_20 = Martial_arts("반탄공","공격의 80%를 반사하고 반사를 성공하였을때 4턴간 나의 데미지를 50%로 줄여준다.","태극조화법",7,5,'main')
main_21 = Martial_arts("배위신","2턴간 상대의 크리티컬확률을 5%로 만들고 5턴간 3데미지를 준다.","당문비전",8,25,'main')
main_22 = Martial_arts("독살포","3턴간 크리티컬확률을 5%로 만들고 2턴간 10데미지, 다음3턴간 5데미지를 준다.","당문비전",6,20,'main')
main_23 = Martial_arts("하무정","2턴간 나의 크리티컬 확률을 100%로 만들고 상대방을 공격불능상태로 만든다.","당문비전",7,15,'main')
main_24 = Martial_arts("만천화우","상대방에게 3턴간 15데미지를 준다.","당문비전",4,10,'main')
main_25 = Martial_arts("후격지세","상대방에게 35, 20, 15, 5의 데미지를 순차적으로 입힌다.","당문비전",5,5,'main')

# 보조 무공
sub_01 = Martial_arts("전격","50% 확률로 상대에게 15데미지를 주고 1턴간 공격불능상태로 만든다.","전격",6,5,'sub')
sub_02 = Martial_arts("뇌진법","50% 확률로 상대를 3턴간 공격불능 상태로 만든다.","전격",6,5,'sub')
sub_03 = Martial_arts("뇌전비술","50% 확률로 상대에게 15 ~ 30의 데미지를 주고 2턴간 공격불능 상태로 만든다.","전격",6,5,'sub')
sub_04 = Martial_arts("약골진","50% 확률로 상대 공격력을 2턴간 50%로 만든다.","약골진",6,5,'sub')
sub_05 = Martial_arts("공복진","50% 확률로 상대 공격력을 2턴간 75%로 만들고 3턴간 크리티컬확률을 50%로 만든다.","약골진",6,5,'sub')
sub_06 = Martial_arts("부동진","50% 확률로 나의 크리티컬 확률을 3턴간 80%로 만든다.","약골진",6,5,'sub')
sub_07 = Martial_arts("기관진","50% 확률로 나의 공격력을 2턴간 125%로 만든다.","기관진",6,5,'sub')
sub_08 = Martial_arts("회주복진","50% 확률로 나의 체력을 5턴간 10을 회복한다.","기관진",6,5,'sub')
sub_09 = Martial_arts("회련진","50% 확률로 나의 체력을 40 회복한다.","기관진",6,5,'sub')
sub_10 = Martial_arts("묘행진","50% 확률로 상대의 크리티컬 확률을 3턴간 50%로 만든다.","묘행진",6,5,'sub')
sub_11 = Martial_arts("풍속진","50% 확률로 상대의 크리티컬 확률을 2턴간 75% 로 만들고 나의 크리티컬 확률을 125% 로 만든다.","묘행진",6,5,'sub')
sub_12 = Martial_arts("멸살진","50% 확률로 상대의 크리티컬 확률을 2턴간 125%로 만들고 나의 공격력을 125%로 만든다.","묘행진",6,5,'sub')

# NPC 클래스
class NPC_stats:
    def __init__(self, po_count, ag_count, ad_count):
        self.name = name
        self.liv = liv
        self.po_count = po_count
        self.ag_count = ag_count
        self.ad_count = ad_count
        self.condition = condition
        self.drop_money = drop_money
        self.drop_exp = drop_exp

# 아이템 프린트 2
def item_print_2(item):
    if item.use == 'item':
        print("{0} : {1}\n{2} : {3}".format( \
            '이름', item.name, \
            '설명', item.damage))
    elif item.use == 'main' or item.use == 'sub':
        print("{0} : {1}\n{2} : {3}\n{4} : {5}\n{6} : {7}\n{8} : {9}".format( \
                '이름', item.name, \
                '설명', item.explanation, \
                '분류', item.system, \
                '쿨타임', item.cool_time, \
                '사용 가능 횟수', item.count))

# 아이템 프린트 1
def item_print_1(player_1, ans, item):
    while True:
        item_print_2(item[ans])
        if item.use == item:
            ans_1 = input("\n{0}을(를) 사용하시겟습니까? (y / n) : ".format(item[ans].name))
            if ans_1 == "y":

                item[ans].count -= 1
                if item[ans].count <= 0:
                    del item[ans]
                return player_1
            elif ans_1 == "n":
                break
            else:
                print("올바른 문자를 입력하세요")
        elif item.use == item:
            ans_1 = input("\n{0} 무공을 착용 하시겟습니까? (y / n) : ".format(item[ans].name))
            if ans_1 == "y":
                pass
            elif ans_1 == 'n':
                break
            else:
                print("올바른 문자를 입력하세요")

# 인벤토리 출력
def inventory(player_1, ans):
    while True:
        ans_1 = change_1(ans)
        print("{0:=^25}".format(str(ans_1) + " 인벤토리"))
        print("{0:^12}{1:^12}".format("Num", "Name"))
        if len(player_1.inven[ans]) == 0:
            print("{0:^12}{1:^12}".format("없음", "없음"))
        if ans == 'main' or ans == 'sub':
            for i in range(len(player_1.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, player_1.inven[ans][i].name))
        else:
            for i in range(len(player_1.inven[ans])):
                print("{0:^12}{1:^12}".format(i + 1, player_1.inven[ans][i].name + "  x" + str(player_1.inven[ans][i].count)))
        if ans == 'main' or ans == 'sub':
            ans_2 = input("\n아이템의 정보를 보고 싶다면 해당 아이템의 번호를 입력하세요\n나가려면 (enter)\n:")
        else:
            ans_2 = input("\n해당 무공의 정보를 보고 싶다면 해당 무공의 번호를 입력하세요\n나가려면 (enter)\n:")
        ans_2 = check(ans_2, 1, len(player_1.inven[ans]))
        if type(ans_2) == type(0):
            if ans == 'item':
                print("\n{0:=^25}".format("Num" + str(ans_2) + " 정보"))
                item_print_1(player_1, use, item)
            else:
                print("\n{0:=^25}".format(item.name + " 정보"))
            ans_2 -= 1
            item_print_1(player_1, use, item)
        elif ans_2 == "":
            break
        else:
            print("올바른 숫자를 입력하세요")

# 무술 인벤토리 프린트
def martial_arts_inventory_print(player_1, ans):
    if ans == 'q':
        print(f"{'장착중인 메인 무공':=^25}")
        m_martial_arts_equipment(player_1)
        print("=" * 25)
        inventory(player_1, main)
    elif ans == 'w':
        print(f"{'장착중인 서브 무공':=^25}")
        s_martial_arts_equipment(player_1)
        print("=" * 25)
        inventory(player_1, sub)


# 무술 인벤토리
def martial_arts_inventory(player_1):
    while True:
        ans = input("\n인벤토리를 선택하세요 [메인 무공 (q) /서브 무공 (w)]")
        print("나가려면 (enter)")
        if ans == "q" or ans == "w":
            martial_arts_inventory_print(player_1, ans)
        elif ans == "":
            break
        else:
            print("올바른 문자를 입력하세요")

# 스텟
def level_up(player_1):
    print("\n" * 2)
    print("=" * 25)
    print("=" * 25)
    print("{0:=^25}".format(" 레벨 업 "))
    print("=" * 25)
    print("=" * 25)
    print('Lv. ' + str(player_1.liv) + ' 로 레벨업을 하였습니다\n')

    stats_point == 5

    while stats_point > 0:
        print("{0:=^25}".format(" 스텟 "))
        print("1 힘 스텟 {0}\
            \n2 민첩 스텟 {1}\
            \n3 모험 스텟 {2}".format(po_count, ag_count, ad_count))

        num = input(":")
        if num == '1':
            if po_count == 50:
                continue
            print("{0:=^25}".format(" 힘 스텟 "))
            print("스텟 1당 공격력이 1% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("공격력 1% 가 추가 됩니다")
                po_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue

        elif num == '2':
            if ag_count == 50:
                continue
            print("{0:=^25}".format(" 민첩 스텟 "))
            print("스텟 1당 크리티컬 확률이 1% 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("크리티컬 확률 1% 가 추가 됩니다.")
                ag_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue

        elif num == '3':
            if ad_count == 50:
                continue
            print("{0:=^25}".format(" 모험 스텟 "))
            print("스텟 1당 체력이 5 증가합니다.")
            ans = input("y / n : ")
            if ans == 'y':
                print("체력이 5 추가 됩니다.")
                ad_count += 1
                stats_point -= 1
            elif ans == 'n':
                continue
        else:
            print("올바른 문자를 입력하세요")
    else:
        pass

# 바꾸기
def change_1(ans):
    if ans == 1:
        return '아이템'
    elif ans == 2:
        return '메인 무공'
    elif ans == 3:
        return "보조 무공"
def change_2 (player_1):
    if player_1.condition == 1:
        return '-'
    if player_1.condition == 2:
        return '기절'
def change_3 (point):
    if point == 1:
        return 'Arena no.1 하북팽가'
    elif point == 2:
        return 'Arena no.2 제갈세가'
    elif point == 3:
        return 'Arena no.3 남궁세가'
    elif point == 4:
        return 'Arena no.4 개방'
    elif point == 5:
        return 'Arena no.5 형산파'
    elif point == 6:
        return 'Arena no.6 점창파'
    elif point == 7:
        return 'Arena no.7 아미파'
    elif point == 8:
        return 'Arena no.8 무당파'
    elif point == 9:
        return 'Arena no.9 무림맹'
    elif point == 10:
        return 'Legendary Arena 소림사 (challenger)'
    elif point == 11:
        return 'Legendary Arena 소림사 (master)'
    elif point == 12:
        return 'Legendary Arena 소림사 (champion)'

# 턴 체크
def turn_chack(player_1):
    # 레벨업 체크
    level_up_count = 0

    if player_1.liv == 1:
        if player_1.exp >= 4:
            player_1.exp -= 4
            player_1.liv += 1
            level_up_count += 1
    elif player_1.liv == 2:
        if player_1.exp >= 400:
            player_1.exp -= 400
            player_1.liv += 1
    elif 3 <= player_1.liv <= 4:
        if player_1.exp >= 300:
            player_1.exp -= 300
            player_1.liv += 1
            level_up_count += 1
    elif 5 <= player_1.exp <= 10:
        if player_1.exp >= player_1.exp * 100:
            player_1.liv += 1
            level_up_count += 1
    elif 11 <= player_1.exp <= 20:
        if player_1.exp >= 1000 + (player_1.exp - 10) * 200:
            player_1.liv += 1
            level_up_count += 1
    elif 21 <= player_1.exp <= 30:
        if player_1.exp >= 3000 + (player_1.exp - 20) * 300:
            player_1.liv += 1
            level_up_count += 1
    elif 31 <= player_1.exp <= 40:
        if player_1.exp >= 6000 + (player_1.exp - 30) * 400:
            player_1.liv += 1
            level_up_count += 1
    elif 41 <= player_1.exp <= 50:
        if player_1.exp >= 10000 + (player_1.exp - 40) * 500:
            player_1.liv += 1
            level_up_count += 1
    elif 51 <= player_1.exp <= 60:
        if player_1.exp >= 15000 + (player_1.exp - 50) * 600:
            player_1.liv += 1
            level_up_count += 1
    elif 61 <= player_1.exp <= 70:
        if player_1.exp >= 21000 + (player_1.exp - 60) * 700:
            player_1.liv += 1
            level_up_count += 1
    elif 71 <= player_1.exp <= 80:
        if player_1.exp >= 28000 + (player_1.exp - 70) * 800:
            player_1.liv += 1
            level_up_count += 1
    elif 81 <= player_1.exp <= 90:
        if player_1.exp >= 36000 + (player_1.exp - 80) * 900:
            player_1.liv += 1
            level_up_count += 1
    elif 91 <= player_1.exp <= 100:
        if player_1.exp >= 45000 + (player_1.exp - 90) * 1000:
            player_1.liv += 1
            level_up_count += 1
    elif 101 <= player_1.exp:
        if player_1.exp >= 5500:
            player_1.liv += 1
            level_up_count += 1

    if level_up_count != 0:
        level_up(player_1)

    # 아레나
    if player_1.point <= 500:
        player_1.Arena == 1
    elif 500 < player_1.point <= 1000:
        player_1.Arena == 2
    elif 1000 < player_1.point <= 1500:
        player_1.Arena == 3
    elif 1500 < player_1_1.point <= 2000:
        player_1.Arena == 4
    elif 2000 < player_1.point <= 2500:
        player_1.Arena == 5
    elif 3500 < player_1.point <= 3000:
        player_1.Arena == 6
    elif 3000 < player_1.point <= 3500:
        player_1.Arena == 7
    elif 3500 < player_1.point <= 4000:
        player_1.Arena == 8
    elif 4000 < player_1.point <= 4500:
        player_1.Arena == 9
    elif 4500 < player_1.point <= 5500:
        player_1.Arena == 10
    elif 5500 < player_1.point <= 6500:
        player_1.Arena == 11
    elif 6500 < player_1.point:
        player_1.Arena == 12

# 매치
def match(player_1):
    NPC_liv = player_1.Arena * 5
    NPC_stats = NPC_liv * 5

    NPC_po_count = math.floor(NPC_stats / 3)
    NPC_ag_count = math.floor(NPC_stats / 3)
    NPC_ad_count = math.floor(NPC_stats / 3)

    remainder = NPC_stats - NPC_po_count * 3

    if remainder == 1:
        NPC_po_count += 1
    elif remainder == 2:
        NPC_po_count += 1
        NPC_ad_count += 1

    for_count = randint(50, 100)

    while for_count > 0:
        var_1 = randint(1, 300)
        var_2 = randint(1, 200)
        var_3 = randint(1, 2)

        if var_1 % 3 == 0:
            var_1 = 3
        elif var_1 % 2 == 0:
            var_1 = 2
        else:
            var_1 = 1

        if var_2 % 2 == 0:
            var_2 = 2
        else:
            var_2 = 1

        if var_1 == 1:
            var = randint(0, math.floor(NPC_po_count / 2))
            NPC_po_count -= var
            if var_2 == 1:
                NPC_ag_count += var
            elif var_2 == 2:
                NPC_ad_count += var
        elif var_1 == 2:
            var = randint(0, math.floor(NPC_ag_count / 2))
            NPC_ag_count -= var
            if var_2 == 1:
                NPC_ad_count += var
            elif var_2 == 2:
                NPC_po_count += var
        elif var_1 == 3:
            var = randint(0, math.floor(NPC_ad_count / 2))
            NPC_ad_count -= var
            if var_2 == 1:
                NPC_po_count += var
            elif var_2 == 2:
                NPC_ag_count += var

        if var_3 == 1:
            for_count -= 1

    while True:
        # NPC 이름 설정
        if player_1.Arena == 1:
            npc_name = ["섬전신도 팽도엽", "진산도 팽대형", "오호단문도 팽대회", "웅풍도 팽대집", "복호도 팽철영"]
        elif player_1.Arena == 2:
            npc_name = ["제갈도", "제갈선", "제갈승", "제갈명", "제갈영기"]
        elif player_1.Arena == 3:
            npc_name = ["철검서생 남궁조", "기협 남궁추", "검패 남궁철", "낙성군자 남군도", "절옥검 남궁진"]
        elif player_1.Arena == 4:
            npc_name = ["탈혼주개 손등", "철심수사 모관", "광권 종호", "옥취개 송결", "혹랑 변혁"]
        elif player_1.Arena == 5:
            npc_name = ["수석장로 용성음", "냉홈검 고진", "조화신검 사견심", "비응검 사공표", "칠지신검 좌군풍"]
        elif player_1.Arena == 6:
            npc_name = ["신풍우사 장거릉", "점창일독 백리궁", "제이장로 흔신풍검 도군홍", "제사장로 독검취응 백리장손", "십방신검 사효심", "신응검협 조빙심"]
        elif player_1.Arena == 7:
            npc_name = ["흑미륵 원정", "결진사태", "홍두타 계명", "독나한 계조", "온미륵 계통"]
        elif player_1.Arena == 8:
            npc_name = ["대엽진인", "목엽진인", "선엽진인", "헌령", "현우", "현수"]
        elif player_1.Arena == 9:
            npc_name = ["취록자 허설", "천금공자 혁리의", "십방랑자 사효심", "신검무적 진산월", "산수재 이정문", "소신승", "창천신룡", "복호도", "옥랑검군"]
        elif player_1.Arena == 10:
            npc_name = ["정화", "정선", "정결", "정현", "정명"]
        elif player_1.Arena == 11:
            npc_name = ["대광", "대방", "대각", "대종", "대절", "대범", "대현", "대원"]
        elif player_1.Arena == 12:
            npc_name = ["범범대사", "굉요 대선사", "굉법", "굉지", "굉도", "굉수", "굉원"]

        NPC_name = choice(npc_name)

# 게임 종료
def game_over():
    print("\n게임을 종료하시겠습니까?")
    while True:
        end_ans = input("y / n : ")
        if end_ans == "y":
            print("\n게임을 종료합니다")

            print("gmae over")
            break
        if end_ans == "n":
            print("\n게임을 계속 진행합니다.")
            main()

# 메인
def main():
    input("게임을 시작하려면 엔터")

    print("\n" * 38)

    try:
        import save
    except:

        player_name = input("\n플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")

        player_1 = Player(player_name, 1, 0, 100, [], [], [], 1, 0, 0, 0)

        plag = 0

    time.sleep(1.3)
    print('\n' * 2)
    print("정상적으로 로그인 되었습니다.")
    time.sleep(0.7)
    print("정보 불러오는 중...")
    time.sleep(0.7)
    print("환영합니다." + player_name + "님")
    time.sleep(1)

    while True:

        print("\n" * 38)

        turn_chack(player_1)  # 아레나, 스텟(레벨)

        player_1.showinfo()

        print("{0} : {1}/{2}/{3}".format( \
            '나의스텟 (힘,민첩,모험)', po_count, ag_count, ad_count))

        if plag == 0:
            print("\n도움을 원한다면 'h' 입력")

        ans = input("\n무엇을 하시겠습니까? : ")

        if ans == "q" or ans == "w" or ans == "e" or ans == "r" or ans == "t" or ans == "y":
            match(player_1)
        elif ans == "a":
            martial_arts_inventory(player_1)
        elif ans == "s":
            inventory(player_1, item)
            continue
        elif ans == "d":
            showshop(player_1)
            continue
        elif ans == "z":
            print("\n게임설명\n전투시작 : q,w,e,r,t,y\n무술 장착 및 해제 : a\n인벤토리 : s\n상점 : d\n도움말 : z\n게임종료 : p\
                    \n한국어를 웬만하면 누르지 마세요.(버그의 원인이 됩니다.)\n다 읽으셨다면 enter.")
            input()
        elif ans == "p":
            game_over()
        else:
            print("다시 입력해 주십시오")

        plag += 1

if __name__ == "__main__":
    main()
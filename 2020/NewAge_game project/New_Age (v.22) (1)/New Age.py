from random import choice
from random import randint
import time
import Player
print("\nthe New_Age (basilisk) game project\n")


# 스토리
def story():
    print("오래전 이땅은 인간의 것이 아니였다.")
    print("개척자였던 에나가 괴물을 물리치자 평화가 찾아왔고,")
    print("이땅에 마지막으로 국가가 세워졌다.")
    print("에나의 후손은 황제가 되어 에나의 힘을 계승해 나갔지만")
    print("피가 연해질수록 괴물들을 막아내기 어려워졌다.")
    print("고대의 에나는 전설의 무기가 잘못 하용될경우를 대비하여 봉인하였지만")
    print("사람들은 전설의 무기를 되찾아 평화를 되찾아 평화를 되찾고자 한다.")
    print("\nNew_Age (새로운_시대)")

    
# 체크
def check (message, start, end):
    if message in list(map(str, range(start, end+1))):
        message = int(message)
        return message
    else:
        return message

    
# 플래이어 클래스


# 메인
def main():
    try:
        import save
    except:

        #story()
        player_name = input("플레이어 이름을 입력하십시오. = ")
        while player_name == "":
            print("\n유효한 이름을 입력하십시오")
            player_name = input("플레이어 이름을 입력하십시오. = ")
        player_1 = Player(player_name, 1, [], [], 100, 0, 0, 0, 20, 0, 0)
        player_x = 10
        player_y = 10

        player_liv = 0

        plag = 0

    print("\n정상적으로 로그인 되었습니다.")
    print("정보 불러오는 중...")
    print("환영합니다." + player_name +"님")

    while True:
        # 마을 버프
        if player_1.point == 1:
            player_1.health = player_1.health + 50
            player_1.hunger = 20
            
        # 체력,허기 최대치
        if player_1.health > 100:
            player_1.health = 100
        if player_1.hunger > 20:
            player_1.hunger = 20

        player_1.showinfo()
        
        input()

if __name__ == "__main__":
    main()

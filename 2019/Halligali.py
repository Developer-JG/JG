import random
import time         


# 메인
def main():
    
    print("\nthe Halligali game project")
    input()
    
    player_card = 28
    com_card = 28
    
    while True:
        
        count = 0
        card_count = 0
        stop = 0
        
        while True:
            count = count + 1
            fruit = random.choice(['바나나', '딸기', '라임', '자두'])
            num = random.randint(1,14)
            
            if 1 <= num <= 5:
                num = 1
            elif 6 <= num <= 8:
                num = 2
            elif 9 <= num <= 11:
                num = 3
            elif 12 <= num <= 13:
                num = 4
            elif num == 14:
                num = 5
            '''
            if fruit == 1:
                fruit = "바나나"
            elif fruit == 2:
                fruit = "딸기"
            elif fruit == 3:
                fruit = "라임"
            elif fruit == 4:
                fruit = "자두"
            '''
            if card_count % 2 == 1:
                player_fruit = fruit
                player_num = num
                player_card = player_card - 1

            else:
                com_fruit = fruit
                com_num = num
                com_card = com_card - 1

            card_count = card_count + 1
            
            if card_count > 1:
                print("\n" * 39)
                print("\n{0:=^25}".format(str(count - 1) + " 턴"))
                print("내 카드 남은개수: {0}\
                        \ncom 카드 남은개수: {1}\
                        \n\
                        \n내 카드:    {2} {3}\
                        \ncom의 카드: {4} {5}" \
                        .format(player_card, com_card, player_fruit, player_num, \
                                com_fruit, com_num))
                
                s_time = time.time()
                ans = input()
                n_time = time.time()

                plag = 0
                if player_fruit == com_fruit:
                    if player_num + com_num == 5:
                        plag = 1
                elif player_num == 5:
                    plag = 1
                elif com_num == 5:
                    plag = 1
                
                if plag == 1:
                    print("\n땡땡땡\n")
                    if ans != "":
                        if n_time - s_time < 0.75:
                            print("내가 먼저 종을 눌렀다.")
                            print(n_time - s_time)
                            input()
                            player_card = player_card + count
                            stop = 1
                        else:
                            print("com이 먼저 종을 눌렀다.")
                            print(n_time - s_time)
                            input()
                            com_card = com_card + count
                            stop = 1
                    else:
                        print("아차.. 같은 문자의 숫자의 합이 5였다.")
                        print("com이 먼저 종을 눌렀다.")
                        input()
                        com_card = com_card + count
                        stop = 1
                        
                if stop == 0:
                    if ans != "":
                        print("아차.. 같은 문자의 숫자의 합이 5가 아니였다.")
                        input()
                        com_card = com_card + count
                        stop = 1

            if player_card < 1:
                
                while True:
                    print("내가 최종패배하였다.")
                    re = input()

                    if re == "re":
                        main()

            if com_card < 1:

                while True:
                    print("내가 최종승리하였다!")
                    re = input()

                    if re == "re":
                        main()
                
            if stop == 1:
                break

if __name__ == "__main__":
    main()    

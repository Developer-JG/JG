from random import *

#인삿말
def hello_1(name,hour):
    select = randint(1, 2)
    if select == 1:
        print("{0}님".format(name))
    select = randint(1, 5)
    if select == 1 and 6 <= hour <= 8:
        print("좋은 아침이에요.")
    elif select == 2 and 11 <= hour <= 12:
        print("좋은 점심이에요.")
    elif select == 3 and 17 <= hour <= 18:
        print("좋은 저녁이에요.")
    elif select == 4 and 20 <= hour <= 24:
        print("좋은 밤이에요.")
    else:
        select = randint(1, 3)
        if select == 1:
            print("반가워요.")
        elif select == 2:
            print("안녕하세요.")
        elif select == 3:
            print("좋은 하루에요.")

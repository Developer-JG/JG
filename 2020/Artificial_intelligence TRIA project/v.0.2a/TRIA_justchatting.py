from random import *
import time

time = time.gmtime(time.time()).tm_hour +

#인삿말
def hello_1(set_name,set_time):
    select = randint(1,5)
    if select == 1:
        print("반갑습니다.")
    if select == 2:
        print("빈기워요.")
    if select == 3:

        print("좋은 아침이네.")
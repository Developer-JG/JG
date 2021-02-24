import random
import time

print("\nVictory exists for them\n")

num = 30 # 암호화 자릿수

print(f"성공확률 : {2 ** num}")
input("도전하려면 [enter]")
print()

while True:
    list = []
    for i in range(0, num):
        add = random.randint(0, 1)
        list.append(add)
        print(add, end = '')
        time.sleep(0.1)

    plag = 0
    for i in list:
        if i == 0:
            plag =+ 1

    print("\n" * 1)
    if plag == 0:
        print("성공")
        while True:
            input("성공")
    else:
        print("꽝")

    print()
    input("도전하려면 [enter]\n")
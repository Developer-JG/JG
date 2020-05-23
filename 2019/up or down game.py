import random
c = 0

while c == 0:

    print ("범위를 지정해주세요")
    q = input("=")
    range1 = int(q)

    print("숫자를 맞춰보세요! ( 1 ~" ,q ,")")

    number = random.randint(1, range1)

    plag = 1
    count = 0
    while plag > 0:

        ans = input("=")
        a = int(ans)
        count = count + 1

        if number - a > 0:
            print (ans , "보다 높아요")

        if number - a == 0:
            print ("정답입니다!")
            print ("물어본 횟수:" , count)
            print ()
            plag = 0

        if number - a < 0:
            print (ans , "보다 낮아요")

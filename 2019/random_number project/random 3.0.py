import random
game = 0
def make_question():
    if game == 0:

        a = random.randint(1, 40)
        b = random.randint(1, 30)
        c = random.randint(1, 20)
        d = random.randint(-10, 10)
        e = random.randint(-10, 10)
        op1 = random.randint(1, 2)
        op2 = random.randint(1, 2)

        if sc1 == 0:
            print("1단계")
        if sc1 == 10:
            print("2단계")
        if sc1 == 20:
            print("3단계")

        if sc1 >= 10:
            if op1 == 1:
                a = a + e
                b = b - d
            if op1 == 2:
                a = a + e
                b = b - c

        q = str(a)

        if sc1 >= 20:
            if op1 == 1:
                q = q + "+"
            if op1 == 2:
                q = q + "-"

            q = q + str(b)
            if op2 == 1:
                q = q + "+"
            if op2 == 2:
                q = q + "-"
            q = q + str(c)
            
            return q

        if op1 == 1:
            q = q + "+"
        if op1 == 2:
            q = q + "-"

        q = q + str(b)

        return q

sc1 = 19


for x in range(10000):
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r:
        print("정답")
        sc1 = sc1 + 1
    else:
        print("GAME OVER")
        print("맞춘개수 :", sc1)
        game = game + 1

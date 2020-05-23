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
            print("1단계 (숫자의 연산)")
        if sc1 == 10:
            print("2단계 (음수의 등장)")
        if sc1 == 20:
            print("3단계 (상수의 증가)")
        if sc1 == 30:
            print("4단계 (상수증가 + 음수)")

        if sc1 >= 10:
            if op1 == 1:
                a = a + e
                b = b - d
            if op1 == 2:
                a = a + e
                b = b - c
    
    
        if sc1 >= 20:
            if sc1 <= 30:
                if a < 0:
                    a = -a
                if b < 0:
                    b = -b

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

        if sc1 < 20:
            if op1 == 1:
                q = q + "+"
            if op1 == 2:
                q = q + "-"

            q = q + str(b)

        return q

sc1 = 0


for x in range(10000):
    q = make_question()
    print(q)
    ans1 = input("=")
    r1 = int(ans1)

    if eval(q) == r1:
        print("정답")
        sc1 = sc1 + 1
    else:
        print("GAME OVER")
        print("답은 :", eval(q))
        print("맞춘개수 :", sc1)
        game = game + 1
                  

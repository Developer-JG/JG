import random
game = 0
def make_question():
    if game == 0:
        a = random.randint(1, 40)
        b = random.randint(1, 20)
        op = random.randint(1, 2)

        q = str(a)

        if op == 1:
            q = q + "+"
        if op == 2:
            q = q + "-"

        q = q + str(b)

        return q

sc1 = 0

for x in range(5):
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
    

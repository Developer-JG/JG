import random
x = 0
print ("[The python 'random' project]")
while x < 1:
    game = -1
    print ("경고! 숫자 이외의 다른 문자, 기호를 쓰지 마세요 버그의 원인이 됩니다. (음수가능)")
    print ()
    print ("게임을 시작하고 싶다면 '0'을 입력하세요")
    print ("게임의 각 단계를 연습하고 싶다면 각 단계를 적으세요")
    print ("ex) 3단계를 연습하고 싶다면 '3' 입력 (최대 7)")
    ans1 = input("=")
    r1 = int(ans1)
    sc1 = 1
    
    if r1 == 0:
        game = 0
        print("game start!")
        print()
    if r1 == 1:
        game = 1
        print("1단계 (숫자의 덧셈)")
        print()
    if r1 == 2:
        game = 2
        print("2단계 (더 큰 숫자의 연산)")
        print()
    if r1 == 3:
        game = 3
        print("3단계 (뺄셈의 등장)")
        print()
    if r1 == 4:
        game = 4
        print("4단계 (음수의 등장)")
        print()
    if r1 == 5:
        game = 5
        print("5단계 (상수의 증가)")
        print()
    if r1 == 6:
        game = 6
        print("6단계 (상수증가 + 더 큰 숫자)")
        print()
    if r1 == 7:
        game = 7
        print("7단계 (상수증가 + 더 큰 숫자 + 음수)")
        print()
    if r1 > 7:
        continue
        print()
        print()
    
    if game == 0:
    
        def make_question():

            a = random.randint(1, 40)
            b = random.randint(1, 30)
            c = random.randint(1, 20)
            d = random.randint(-10, 10)
            e = random.randint(-10, 10)
            f = random.randint(-50, 50)
            g = random.randint(-50, 50)
            h = random.randint(-50, 50)
            op1 = random.randint(1, 2)
            op2 = random.randint(1, 2)
            
            if sc1 == 1:
                print("1단계 (숫자의 덧셈)")
            if sc1 == 10:
                print("2단계 (더 큰 숫자의 연산)")
            if sc1 == 20:
                print("3단계 (뺄셈의 등장)")
            if sc1 == 30:
                print("4단계 (음수의 등장)")
            if sc1 == 40:
                print("5단계 (상수의 증가)")
            if sc1 == 50:
                print("6단계 (상수증가 + 더 큰 숫자)")
            if sc1 == 60:
                print("7단계 (상수증가 + 더 큰 숫자 + 음수)")
                
            if sc1 < 10:
                a = a - 20
                b = b - 15

            if sc1 < 20:
                if a < 0:
                    a = -a
                if b < 0:
                    b = -b

            if sc1 >= 10:
                if sc1 < 20:
                    a = a + 10
                    b = b + 10

        
            if sc1 >= 30:
                if sc1 <= 40:
                    if op1 == 1:
                        a = a - e
                        b = b - d
                    if op1 == 2:
                        a = a - e
                        b = b - c

            if sc1 >= 40:
                if sc1 < 60:
                    if a < 0:
                        a = -a
                    if b < 0:
                        b = -b
                    
            if sc1 >= 50:
                a = a - 10
                b = b + 10
                c = c + 10


            if sc1 > 60:
                
                q = str(f)
                
                if op1 == 1:
                    q = q + "+"
                if op1 == 2:
                    q = q + "-"
            
                q = q + str(g)
            
                if op2 == 1:
                    q = q + "+"
                if op2 == 2:
                    q = q + "-"
    
                q = q + str(h)
        
                return q

            if sc1 < 60:
                
                q = str(a)
                
                if sc1 >= 40:
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
                
                    q = q + "+"
                
                    q = q + str(b)
        
                    return q

    if game == 1:
        
        def level_1 ():
            a = random.randint(1, 20)
            b = random.randint(1, 15)
            
            q = str(a)
            
            q = q + "+"
            
            q = q + str(b)
            
            return q
        
    if game == 2:
        
        def level_2 ():
            a = random.randint(10, 50)
            b = random.randint(10, 40)
            
            q = str(a)
            
            q = q + "+"
            
            q = q + str(b)
            
            return q

    if game == 3:
        
        def level_3 ():
            a = random.randint(1, 40)
            b = random.randint(1, 30)
            op1 = random.randint(1,2)
            
            q = str(a)

            if op1 == 1:
                q = q + "+"
            if op1 == 2:
                q = q + "-"
            
            q = q + str(b)
            
            return q

    if game == 4:
        
        def level_4 ():
            a = random.randint(-10, 50)
            b = random.randint(-10, 40)
            op1 = random.randint(1, 2)

            
            q = str(a)
            
            if op1 == 1:
                q = q + "+"
            if op1 == 2:
                q = q + "-"
                
            q = q + str(b)
            
            return q

    if game == 5:
        
        def level_5 ():
            a = random.randint(1, 50)
            b = random.randint(1, 40)
            c = random.randint(1, 20)
            op1 = random.randint(1, 2)
            op2 = random.randint(1, 2)
            
            q = str(a)
            
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

    if game == 6:
        
        def level_6 ():
            a = random.randint(1, 40)
            b = random.randint(1, 40)
            c = random.randint(1, 30)
            op1 = random.randint(1, 2)
            op2 = random.randint(1, 2)

            q = str(a)
            
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

    if game == 7:
        
        def level_7 ():
            a = random.randint(-40, 40)
            b = random.randint(-30, 40)
            c = random.randint(-30, 30)
            op1 = random.randint(1, 2)
            op2 = random.randint(1, 2)

            q = str(a)
            
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


    sc1 = 1

    if game == 0:
        
        while sc1 < 10000:
            q = make_question()
            print(q)
            ans2 = input("=")
            r = int(ans2)
            
            if eval(q) == r:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q))
                print("맞춘개수 :", sc1)
                print()

    if game == 1:
        
        while sc1 < 10000:
            q1 = level_1()
            print(q1)
            ans2 = input("=")
            r1 = int(ans2)
            
            if eval(q1) == r1:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q1))
                print("맞춘개수 :", sc1)
                print()

    if game == 2:
    
        while sc1 < 10000:
            q2 = level_2()
            print(q2)
            ans2 = input("=")
            r2 = int(ans2)
        
            if eval(q2) == r2:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q2))
                print("맞춘개수 :", sc1)
                print()

    if game == 3:
    
        while sc1 < 10000:
            q3 = level_3()
            print(q3)
            ans2 = input("=")
            r3 = int(ans2)
        
            if eval(q3) == r3:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q3))
                print("맞춘개수 :", sc1)
                print()

    if game == 4:
    
        while sc1 < 10000:
            q4 = level_4()
            print(q4)
            ans2 = input("=")
            r4 = int(ans2)
        
            if eval(q4) == r4:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q4))
                print("맞춘개수 :", sc1)
                print()
                
    if game == 5:
    
        while sc1 < 10000:
            q5 = level_5()
            print(q5)
            ans2 = input("=")
            r5 = int(ans2)
        
            if eval(q5) == r5:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q5))
                print("맞춘개수 :", sc1)
                print()

    if game == 6:
    
        while sc1 < 10000:
            q6 = level_6()
            print(q6)
            ans2 = input("=")
            r6 = int(ans2)
        
            if eval(q6) == r6:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q6))
                print("맞춘개수 :", sc1)
                print()
                
    if game == 7:
    
        while sc1 < 10000:
            q7 = level_7()
            print(q7)
            ans2 = input("=")
            r7 = int(ans2)
        
            if eval(q7) == r7:
                print("정답 :",sc1)
                print()
                sc1 = sc1 + 1
            else:
                sc1 = 1
                print("GAME OVER")
                print("답은 :", eval(q7))
                print("맞춘개수 :", sc1)
                print()

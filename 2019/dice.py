import random
print ("주사위 개수")
print ("매번 바꾸기 : 1")
print ("바꾸지 않기 : 2")
ans = input("=")
a = int(ans)
if a == 1:
    while a < 5:

        ans1 = input("주사위 개수를 입력하세요.")
        m1 = int(ans1)
    
        number1 = random.randint(1, 6)
        number2 = random.randint(1, 6)

        if m1 == 1:
            print("주사위:" , number1 )
    
        if m1 == 2:
            if number1 == number2:
                print("더블!" , number1 , number2)
            else:
                print("1번 주사위:" , number1 )
                print("2번 주사위:" , number2 )
        print () 

if a == 2:
    print ("주사위 개수를 입력하세요. (최대 2개)")
    ans2 = input ("=")
    m2 = int(ans2)
    if m2 > 2:
        m2 = 2
    if m2 < 1:
        m2 = 1
    while a < 5:
    
        number3 = random.randint(1, 6)
        number4 = random.randint(1, 6)

        if m2 == 1:
            print("주사위:" , number3 )
    
        if m2 == 2:
            if number3 == number4:
                print("더블!" , number3 , number4)
            else:
                print("1번 주사위:" , number3 )
                print("2번 주사위:" , number4 )
        print ()        
        z2 = input("다음 주사위")
        print ()
                

from random import randint
import time

while True:
    re = 0
    while re != 30:

        print("\n" * 4)
        
        ran = randint(1, 10000)

        if  1 <= ran <= 500:
            print ("꽝 (5%)")

        if 501 <= ran <= 4500:
            print ("자유시간 x 2 (40%)")

        if 4501 <= ran <= 7000:
            print ("자유시간 x 4 (25%)")

        if 7001 <= ran <= 8500:
            print ("오예스 x 2 (15%)")

        if 8501 <= ran <= 9500:
            print ("오예스 x 4 (10%)")

        if 9501 <= ran <= 9800:
            print ("자유시간 x 10 (3%)")

        if 9801 <= ran <= 9907:
            print ("오예스 x 10 (1.06%)")

        if 9908 <= ran <= 10000:
            print ("문화상품권 (0.02%)")

        re = re + 1

        time.sleep(0.1)
    
    print("\n" * 4)
    print("\n{0:=^25}\n".format("결과"))

    ran = randint(1, 10000)

    if  1 <= ran <= 500:
        print ("꽝 (5%)")

    if 501 <= ran <= 4500:
        print ("자유시간 x 2 (40%)")

    if 4501 <= ran <= 7000:
        print ("자유시간 x 4 (25%)")

    if 7001 <= ran <= 8500:
        print ("오예스 x 2 (15%)")

    if 8501 <= ran <= 9500:
        print ("오예스 x 4 (10%)")

    if 9501 <= ran <= 9800:
        print ("자유시간 x 10 (3%)")

    if 9801 <= ran <= 9907:
        print ("오예스 x 10 (1.06%)")

    if 9908 <= ran <= 10000:
        print ("문화상품권 (0.02%)")

    input()

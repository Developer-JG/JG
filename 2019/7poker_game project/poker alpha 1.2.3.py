import random

plag = 2

pm = 2000
cm = 2000

while plag > 0:
    plag = 10
    bet = 0
    while plag > 1:
        print ("게임을 시작합니다")
        print ("기본배팅 : 10원")
        print()
        pm = pm - 10
        cm = cm - 10
        bet = 20
        plag = 0
        plag2 = 0
        ans1 = 0

        shdc = ['스페이드', '하트', '다이아', '클로버']

        pcdn1 = random.randint(1, 13)
        pcdn2 = random.randint(1, 13)
        pcdn3 = random.randint(1, 13)
        pcdn4 = random.randint(1, 13)
        pcdn5 = random.randint(1, 13)
        pcdn6 = random.randint(1, 13)
        pcdn7 = random.randint(1, 13)

        pcd1 = random.randint(1, 4)
        pcdp2 = random.choice(shdc)
        pcdp3 = random.choice(shdc)
        pcd4 = random.randint(1, 4)
        pcd5 = random.randint(1, 4)
        pcd6 = random.randint(1, 4)
        pcd7 = random.randint(1, 4)

        ccdn1 = random.randint(1, 13)
        ccdn2 = random.randint(1, 13)
        ccdn3 = random.randint(1, 13)
        ccdn4 = random.randint(1, 13)
        ccdn5 = random.randint(1, 13)
        ccdn6 = random.randint(1, 13)
        ccdn7 = random.randint(1, 13)

        ccd1 = random.randint(1, 4)
        pcdp2 = random.choice(shdc)
        pcdp3 = random.choice(shdc)
        ccd4 = random.randint(1, 4)
        ccd5 = random.randint(1, 4)
        ccd6 = random.randint(1, 4)
        ccd7 = random.randint(1, 4)

        cb1 = random.randint(1, 10)
        cb2 = random.randint(1, 10)
        cb3 = random.randint(1, 10)
        cb4 = random.randint(1, 10)

        cr1 = random.randint(1, 2)
        cr2 = random.randint(1, 2)
        cr3 = random.randint(1, 2)
        cr4 = random.randint(1, 2)

        if ccd1 == 1:
            ccdp1 = "스페이드"
        elif ccd1 == 2:
            ccdp1 = "다이아몬드"
        elif ccd1 == 3:
            ccdp1 = "하트"
        elif ccdp1 == 1:
            ccdp1 = "클로버"

        if pcd1 == 4:
            pcdp1 = "스페이드"
        elif pcd1 == 3:
            pcdp1 = "다이아몬드"
        elif pcd1 == 2:
            pcdp1 = "하트"
        elif pcd1 == 1:
            pcdp1 = "클로버"

        print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ]")
        print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"]")

        icn1 = int(ccdn1)
        ipn1 = int(pcdn1)

        print ()

        plag1 = 0
        icn = int(ccdn1)
        ipn = int(pcdn1)
        if icn - ipn > 0:
            print ("com1의 선공")
            plag1 = 2
        if icn - ipn < 0:
            print ("나의 선공")
            plag1 = 1
        if icn - ipn == 0:
            if pcd1 - ccd1 > 0:
                print ("나의 선공")
                plag1 = 1
            if pcd1 - ccd1 < 0:
                print ("com1의 선공")
                plag1 = 2 
                    
        if plag1 == 1:
            print ()
            print ("배팅하시겠습니까? 플레이어 돈:",pm,"cm1 돈:",cm,"배팅금액:",bet)
            print ("[ford = 0] [check = 1] [raise = 2] [all in = 3]")
            q = input("=")
            ans = int(q)
            print ()

            if ans < 0:
                ans = 0
            if ans > 3:
                ans = 3

            if ans == 0:
                print ("죽습니다.")
                cm = cm + bet
                plag2 = 1
            if ans == 1:
                print ("돈을 걸지 않습니다. 체크")
            if ans == 2:
                print ("판돈을 올립니다. 레이즈")
                print ("얼마나 베팅하시겠습니까? (최대 10)")
                q = input("=")
                ans1 = int(q)
                if ans1 > 10 :
                    ans1 = 10
                if ans1 < 1 :
                    ans1 = 1
                bet = bet + ans1
                pm = pm - ans1
                print (ans1,"배팅하셨습니다.")
                
            if ans == 3:
                if pm < 100:
                    print ("올인!")
                    bet = bet + pm
                    pm = 0
                else:
                    print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans1 = int(q)
                    if ans1 > 10 :
                        ans1 = 10
                    if ans1 < 1 :
                        ans1 = 1
                    print (ans1,"배팅하셨습니다.")
                    bet = bet + ans1
                    pm = pm - ans1
                    
            if plag2 != 1:
                print ()
                icr1 = int(cr1)
                if icr1 == 1:
                    if ans == 1:
                        print ("com1의 체크. 총 배팅:",bet)
                    if ans == 2:
                        bet = bet + ans1
                        pm = pm - ans1
                        print ("com1의 콜. 총 배팅:",bet)
                    if ans == 3:
                        bet = bet + ans1
                        pm = pm - ans1
                        print ("com1의 콜. 총 배팅:",bet)
                if icr1 == 2:
                    print ("com1의 레이즈")
                    icb1 = int(cb1)
                    if ans1 > 0:
                        ans2 = ans1 + icb1
                    else:
                        ans2 = icb1
                    bet = bet + ans2
                    cm = cm - ans2
                    print ("com1이 ",ans2,"배팅 하였습니다. 총 배팅:",bet)
                    
        if plag1 == 2:
            print ()
            icr1 = int(cr1)
            if icr1 == 1:
                print ("com1의 체크")
            if icr1 == 2:
                print ("com1의 레이즈")
                icb1 = int(cb1)
                print ("com1이 ",icb1,"배팅 하였습니다.")
                ans1 = icb1
                bet = bet + icb1
                cm = cm - icb1

            print ()
            print ("배팅하시겠습니까? 플레이어 돈:",pm,"cm1 돈:",cm,"배팅금액:",bet)
            print ("[ford = 0] [call = 1] [raise = 2] [all in = 3]")
            q = input("=")
            ans = int(q)
            print ()

            if ans < 0:
                ans = 0
            if ans > 3:
                ans = 3

            if ans == 0:
                print ("죽습니다.")
                cm = cm + bet
                plag2 = 1
            if ans == 1:
                if icr1 == 1:
                    print ("돈을 걸지 않습니다. 체크")
                if icr1 == 2:
                    print ("판돈 올린것을 받아들입니다. 콜")
                    bet = bet + ans1
                    pm = pm - ans1
                    print (ans1,"배팅 하셨습니다. 총 배팅:",bet)
            if ans == 2:
                print ("판돈을 올립니다. 레이즈")
                print ("얼마나 베팅하시겠습니까? (최대 10)")
                q = input("=")
                ans2 = int(q)
                if ans2 > 10 :
                    ans2 = 10
                if ans2 < 1 :
                    ans2 = 1
                bet = bet + ans2
                pm = pm - ans2
                print (ans2,"배팅하셨습니다. 총 배팅:",bet)
                
            if ans == 3:
                if pm < 100:
                    print ("올인!")
                    bet = bet + pm
                    pm = 0
                else:
                    print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans2 = int(q)
                    if ans2 > 10 :
                        ans2 = 10
                    if ans2 < 1 :
                        ans2 = 1
                    bet = bet + ans2
                    pm = pm - ans2
                    print (ans2,"배팅하셨습니다. 총 배팅:",bet)
                    
        if plag2 < 1:
            if ccd4 == 1:
                ccdp4 = "스페이드"
            elif ccd4 == 2:
                ccdp4 = "다이아몬드"
            elif ccd4 == 3:
                ccdp4 = "하트"
            else:
                ccdp4 = "클로버"
            
            if pcd4 == 1:
                pcdp4 = "스페이드"
            elif pcd4 == 2:
                pcdp4 = "다이아몬드"
            elif pcd4 == 3:
                pcdp4 = "하트"
            else:
                pcdp4 = "클로버"
            print ()
            print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ] [",ccdp4, ccdn4,"]")
            print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"] [",pcdp4,pcdn4,"]")

            
            icp1 = int(ccd1)
            icp4 = int(ccd4)
            ipp1 = int(pcd1)
            ipp4 = int(pcd4)
            icn1 = int(ccdn1)
            icn4 = int(ccdn4)
            ipn1 = int(pcdn1)
            ipn4 = int(pcdn4)

            if icp1 == 1:
                icp1 = 4
            elif icp1 == 2:
                icp1 = 3
            elif icp1 == 3:
                icp1 = 2
            elif icp1 == 4:
                icp1 = 1
                
            if icp4 == 1:
                icp4 = 4
            elif icp4 == 2:
                icp4 == 3
            elif icp4 == 3:
                icp4 = 2
            elif icp4 == 4:
                icp4 = 1
                
            if ipp1 == 1:
                icpp1 = 4
            elif ipp1 == 2:
                ipp1 = 3
            elif ipp1 == 3:
                ipp1 = 2
            elif ipp1 == 4:
                ipp1 = 1

            if ipp4 == 1:
                ipp4 = 4
            elif ipp4 == 2:
                ipp4 = 3
            elif ipp4 == 3:
                ipp4 = 2
            elif ipp4 == 4:
                ipp4 = 1

            jcp1 = icp1 * 100
            jcp4 = icp4 * 100
            jpp1 = ipp1 * 100
            jpp4 = ipp4 * 100

            kcd1 = jcp1 + icn1
            kcd4 = jcp4 + icn4
            kpd1 = jpp1 + ipn1
            kpd4 = jpp4 + ipn4
    
            plag3 = 0

            kpd1 = int(kpd1)
            kpd4 = int(kpd4)
            kcd1 = int(kcd1)
            kcd4 = int(kcd4)
            
            if icn1 == icn4:
                if ipn1 == ipn4:
                    if kcd1 > kcd4:
                        kcd = kcd1
                    elif kcd1 < kcd4:
                        kcd = kcd4

                    if kpd1 > kpd4:
                        kpd = kpd1
                    elif kpd1 < kpd4:
                        kpd = kpd4
                    
                    if kpd - kcd > 0:
                        print ("나의 선공")
                        plag3 = 1
                    if kpd - kcd < 0:
                        print ("com1의 선공")
                        plag3 = 2
                elif ipn1 != ipn4:
                    print ("com1의 선공")
                    plag3 = 2
            elif ipn1 == ipn4:
                if icn1 != icn4:
                    print ("나의 선공")
                    plag3 = 1
                    
            if plag3 == 0:        
                if kcd1 > kcd4:
                    kcd = kcd1
                elif kcd1 > kcd4:
                    kcd = kcd4

                if kpd1 > kpd4:
                    kpd = kpd1
                elif kpd1 < kpd4:
                    kpd = kpd4
                    
                if kpd > kcd:
                    print ("나의 선공")
                    plag3 = 1
                if kpd < kcd:
                    print ("com1의 선공")
                    plag3 = 2
            
        break                
        plag = 10

        q = input()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        print()
        q = input()
        

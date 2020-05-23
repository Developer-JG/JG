import random

plag = 2

pm = 2000
cm = 2000

print ()
print ("[The python 7poker project]")
print ()

while plag > 0:
    plag = 10
    bet = 0
    while plag > 1:
        print ("게임을 시작합니다")
        print ("기본배팅 : 10원")
        print ()
        pm = pm - 10
        cm = cm - 10
        bet = 20
        print ("플레이어 돈:",pm,"cm1의 돈:",cm)
        print()
        print ("셔플중")
        print()
        plag = 0
        plag2 = 0
        plag4 = 0
        ans1 = 0
        ans2 = 0
        ans3 = 0
        ans4 = 0
        ans9 = 0
        ipp = 0
        icp = 0

        plag50 = 0
        
        while plag50 != 1:
        
            pcdn1 = random.randint(1, 13)
            pcdn2 = random.randint(1, 13)
            pcdn3 = random.randint(1, 13)
            pcdn4 = random.randint(1, 13)
            pcdn5 = random.randint(1, 13)
            pcdn6 = random.randint(1, 13)
            pcdn7 = random.randint(1, 13)
                        
            pcd1 = random.randint(1, 4)
            pcd2 = random.randint(1, 4)
            pcd3 = random.randint(1, 4)
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
            ccd2 = random.randint(1, 4)
            ccd3 = random.randint(1, 4)
            ccd4 = random.randint(1, 4)
            ccd5 = random.randint(1, 4)
            ccd6 = random.randint(1, 4)
            ccd7 = random.randint(1, 4)
    
            cb1 = random.randint(1, 10)
            cb2 = random.randint(1, 10)
            cb3 = random.randint(1, 10)
            cb4 = random.randint(1, 10)

            cr1 = random.randint(1, 2)
            
            icp1 = int(ccd1)
            icp2 = int(ccd2)
            icp3 = int(ccd3)
            icp4 = int(ccd4)
            icp5 = int(ccd5)
            icp6 = int(ccd6)
            icp7 = int(ccd7)
            
            ipp1 = int(pcd1)
            ipp2 = int(pcd2)
            ipp3 = int(pcd3)
            ipp4 = int(pcd4)
            ipp5 = int(pcd5)
            ipp6 = int(pcd6)
            ipp7 = int(pcd7)

            icn1 = int(ccdn1)
            icn2 = int(ccdn2)
            icn3 = int(ccdn3)
            icn4 = int(ccdn4)
            icn5 = int(ccdn5)
            icn6 = int(ccdn6)
            icn7 = int(ccdn7)

            ipn1 = int(pcdn1)
            ipn2 = int(pcdn2)
            ipn3 = int(pcdn3)
            ipn4 = int(pcdn4)
            ipn5 = int(pcdn5)
            ipn6 = int(pcdn6)
            ipn7 = int(pcdn7)
            
            jcp1 = icp1 * 100
            jcp2 = icp2 * 100
            jcp3 = icp3 * 100
            jcp4 = icp4 * 100
            jcp5 = icp5 * 100
            jcp6 = icp6 * 100
            jcp7 = icp7 * 100
            jpp1 = ipp1 * 100
            jpp2 = ipp2 * 100
            jpp3 = ipp3 * 100
            jpp4 = ipp4 * 100
            jpp5 = ipp5 * 100
            jpp6 = ipp6 * 100
            jpp7 = ipp7 * 100
            
            kcd1 = jcp1 + icn1
            kcd2 = jcp2 + icn2
            kcd3 = jcp3 + icn3
            kcd4 = jcp4 + icn4
            kcd5 = jcp5 + icn5
            kcd6 = jcp6 + icn6
            kcd7 = jcp7 + icn7
            kpd1 = jpp1 + ipn1
            kpd2 = jpp2 + ipn2
            kpd3 = jpp3 + ipn3
            kpd4 = jpp4 + ipn4
            kpd5 = jpp5 + ipn5
            kpd6 = jpp6 + ipn6
            kpd7 = jpp7 + ipn7
            
            kpd1 = int(kpd1)
            kpd2 = int(kpd2)
            kpd3 = int(kpd3)
            kpd4 = int(kpd4)
            kpd5 = int(kpd5)
            kpd6 = int(kpd6)
            kpd7 = int(kpd7)
            kcd1 = int(kcd1)
            kcd2 = int(kcd2)
            kcd3 = int(kcd3)
            kcd4 = int(kcd4)
            kcd5 = int(kcd5)
            kcd6 = int(kcd6)
            kcd7 = int(kcd7)
            
            plag4 = 0
            
            if kcd1 != kcd2:
                if kcd2 != kcd3:
                    if kcd3 != kcd4:
                        if kcd4 != kcd5:
                            if kcd5 != kcd6:
                                if kcd6 != kcd7:
                                    if kcd7 != kpd1:
                                        if kpd1 != kpd2:
                                            if kpd2 != kpd3:
                                                if kpd3 != kpd4:
                                                    if kpd4 != kpd5:
                                                        if kpd5 != kpd6:
                                                            if kpd6 != kpd7:
                                                                if kpd7 != kcd1:
                                                                    if kcd1 != kcd3:
                                                                        if kcd2 != kcd4:
                                                                            if kcd3 != kcd5:
                                                                                if kcd4 != kcd6:
                                                                                    if kcd5 != kcd7:
                                                                                        if kcd6 != kpd1:
                                                                                            if kcd7 != kpd2:
                                                                                                if kpd1 != kpd3:
                                                                                                    if kpd2 != kpd4:
                                                                                                        if kpd3 != kpd5:
                                                                                                            if kpd4 != kpd6:
                                                                                                                if kpd5 != kpd7:
                                                                                                                    if kpd6 != kcd1:
                                                                                                                        if kpd7 != kcd2:
                                                                                                                            if kcd1 != kcd4:
                                                                                                                                if kcd2 != kcd5:
                                                                                                                                    if kcd3 != kcd6:
                                                                                                                                        if kcd4 != kcd7:
                                                                                                                                            if kcd5 != kpd1:
                                                                                                                                                if kcd6 != kpd2:
                                                                                                                                                    if kcd7 != kpd3:
                                                                                                                                                        if kpd1 != kpd4:
                                                                                                                                                            if kpd2 != kpd5:
                                                                                                                                                                if kpd3 != kpd6:
                                                                                                                                                                    if kpd4 != kpd7:
                                                                                                                                                                        if kpd5 != kcd1:
                                                                                                                                                                            if kpd6 != kcd2:
                                                                                                                                                                                if kpd7 != kcd3:
                                                                                                                                                                                    if kcd1 != kcd5:
                                                                                                                                                                                        if kcd2 != kcd6:
                                                                                                                                                                                            if kcd3 != kcd7:
                                                                                                                                                                                                if kcd4 != kpd1:
                                                                                                                                                                                                    if kcd5 != kpd2:
                                                                                                                                                                                                        if kcd6 != kpd3:
                                                                                                                                                                                                            if kcd7 != kpd4:
                                                                                                                                                                                                                if kpd1 != kpd5:
                                                                                                                                                                                                                    if kpd2 != kpd6:
                                                                                                                                                                                                                        if kpd3 != kpd7:
                                                                                                                                                                                                                            if kpd4 != kcd1:
                                                                                                                                                                                                                                if kpd5 != kcd2:
                                                                                                                                                                                                                                    if kpd6 != kcd3:
                                                                                                                                                                                                                                        if kpd7 != kcd4:
                                                                                                                                                                                                                                            if kcd1 != kcd6:
                                                                                                                                                                                                                                                if kcd2 != kcd7:
                                                                                                                                                                                                                                                    if kcd3 != kpd1:
                                                                                                                                                                                                                                                        if kcd4 != kpd2:
                                                                                                                                                                                                                                                            if kcd5 != kpd3:
                                                                                                                                                                                                                                                                if kcd6 != kpd4:
                                                                                                                                                                                                                                                                    if kcd7 != kpd5:
                                                                                                                                                                                                                                                                        if kpd1 != kpd6:
                                                                                                                                                                                                                                                                            if kpd2 != kpd7:
                                                                                                                                                                                                                                                                                if kpd3 != kcd1:
                                                                                                                                                                                                                                                                                    if kpd4 != kcd2:
                                                                                                                                                                                                                                                                                        if kpd5 != kcd3:
                                                                                                                                                                                                                                                                                            if kpd6 != kcd4:
                                                                                                                                                                                                                                                                                                if kpd7 != kcd5:
                                                                                                                                                                                                                                                                                                    if kcd1 != kcd7:
                                                                                                                                                                                                                                                                                                        if kcd2 != kpd1:
                                                                                                                                                                                                                                                                                                            if kcd3 != kpd2:
                                                                                                                                                                                                                                                                                                                if kcd4 != kpd3:
                                                                                                                                                                                                                                                                                                                    if kcd5 != kpd4:
                                                                                                                                                                                                                                                                                                                        if kcd6 != kpd5:
                                                                                                                                                                                                                                                                                                                            if kcd7 != kpd6:
                                                                                                                                                                                                                                                                                                                                if kpd1 != kpd7:
                                                                                                                                                                                                                                                                                                                                    if kpd2 != kcd1:
                                                                                                                                                                                                                                                                                                                                        if kpd3 != kcd2:
                                                                                                                                                                                                                                                                                                                                            if kpd4 != kcd3:
                                                                                                                                                                                                                                                                                                                                                if kpd5 != kcd4:
                                                                                                                                                                                                                                                                                                                                                    if kpd6 != kcd5:
                                                                                                                                                                                                                                                                                                                                                        if kpd7 != kcd6:
                                                                                                                                                                                                                                                                                                                                                            if kcd1 != kpd1:
                                                                                                                                                                                                                                                                                                                                                                if kcd2 != kpd2:
                                                                                                                                                                                                                                                                                                                                                                    if kcd3 != kpd3:
                                                                                                                                                                                                                                                                                                                                                                        if kcd4 != kpd4:
                                                                                                                                                                                                                                                                                                                                                                            if kcd5 != kpd5:
                                                                                                                                                                                                                                                                                                                                                                                if kcd6 != kpd6:
                                                                                                                                                                                                                                                                                                                                                                                    if kcd7 != kpd7:
                                                                                                                                                                                                                                                                                                                                                                                        plag50 = 1
    
    
        plag3 = 0
        
        if ccd1 == 4:
            ccdp1 = "스페이드"
        elif ccd1 == 3:
            ccdp1 = "다이아몬드"
        elif ccd1 == 2:
            ccdp1 = "하트"
        elif ccd1 == 1:
            ccdp1 = "클로버"

        if ccd2 == 4:
            ccdp2 = "스페이드"
        elif ccd2 == 3:
            ccdp2 = "다이아몬드"
        elif ccd2 == 2:
            ccdp2 = "하트"
        elif ccd2 == 1:
            ccdp2 = "클로버"

        if ccd3 == 4:
            ccdp3 = "스페이드"
        elif ccd3 == 3:
            ccdp3 = "다이아몬드"
        elif ccd3 == 2:
            ccdp3 = "하트"
        elif ccd3 == 1:
            ccdp3 = "클로버"

        if pcd1 == 4:
            pcdp1 = "스페이드"
        elif pcd1 == 3:
            pcdp1 = "다이아몬드"
        elif pcd1 == 2:
            pcdp1 = "하트"
        elif pcd1 == 1:
            pcdp1 = "클로버"

        if pcd2 == 4:
            pcdp2 = "스페이드"
        elif pcd2 == 3:
            pcdp2 = "다이아몬드"
        elif pcd2 == 2:
            pcdp2 = "하트"
        elif pcd2 == 1:
            pcdp2 = "클로버"

        if pcd3 == 4:
            pcdp3 = "스페이드"
        elif pcd3 == 3:
            pcdp3 = "다이아몬드"
        elif pcd3 == 2:
            pcdp3 = "하트"
        elif pcd3 == 1:
            pcdp3 = "클로버"

        print ("첫번째 턴!")
        print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ]")
        print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"]")

        icn1 = int(ccdn1)
        ipn1 = int(pcdn1)

        print ()

        plag1 = 0
        icn = int(ccdn1)
        ipn = int(pcdn1)

        if ipn == 1:
            ipn = 14
        if icn == 1:
            icn = 14

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

        if ipn == 14:
            ipn = 1
        if icn == 14:
            icn = 1
                    
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
                if ans1 != 0:
                    if ans1 > 10 :
                        ans1 = 10
                    bet = bet + ans1
                    pm = pm - ans1
                    print (ans1,"배팅하셨습니다.")
                else:
                    print ("돈을 걸지 않습니다. 체크")
                
            if ans == 3:
                if pm < 100:
                    print ("올인!")
                    bet = bet + pm
                    pm = 0
                    plag2 = 1
                else:
                    print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans1 = int(q)
                    if ans1 != 0:
                        if ans1 > 10 :
                            ans1 = 10
                        bet = bet + ans1
                        pm = pm - ans1
                        print (ans1,"배팅하셨습니다.")
                    else:
                        print ("돈을 걸지 않습니다. 체크")
                    
            print ()
            if plag2 == 0:
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
                    print ("com1이 ",ans2," 배팅 하였습니다. 총 배팅:",bet)
                    
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
                    ans2 = ans1
                    bet = bet + ans2
                    pm = pm - ans2
                    print (ans2,"배팅 하셨습니다. 총 배팅:",bet)
            if ans == 2:
                print ("판돈을 올립니다. 레이즈")
                print ("얼마나 베팅하시겠습니까? (최대 10)")
                q = input("=")
                ans9 = int(q)
                if ans9 != 0:
                    if ans9 > 10 :
                        ans9 = 10
                    ans2 = ans1 + ans9
                    bet = bet + ans2
                    pm = pm - ans2
                    print (ans2,"배팅하셨습니다. 총 배팅:",bet)
                else:
                    print ("돈을 걸지 않습니다. 체크")
                
            if ans == 3:
                if pm < 100:
                    print ("올인!")
                    bet = bet + pm
                    pm = 0
                    plag2 = 1
                else:
                    print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans9 = int(q)
                    if ans9 != 0:
                        if ans9 > 10 :
                            ans9 = 10
                        ans2 = ans1 + ans9
                        bet = bet + ans2
                        pm = pm - ans2
                        print (ans2,"배팅하셨습니다. 총 배팅:",bet)
                    else:
                        print ("돈을 걸지 않습니다. 체크")
                    
        if ccd4 == 4:
            ccdp4 = "스페이드"
        elif ccd4 == 3:
            ccdp4 = "다이아몬드"
        elif ccd4 == 2:
            ccdp4 = "하트"
        elif ccd4 == 1:
            ccdp4 = "클로버"
            
        if pcd4 == 4:
            pcdp4 = "스페이드"
        elif pcd4 == 3:
            pcdp4 = "다이아몬드"
        elif pcd4 == 2:
            pcdp4 = "하트"
        elif pcd4 == 1:
            pcdp4 = "클로버"
        if plag2 != 1:
            print ()
            print ()
            print ()
            print ("두번째 턴!")
            print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ] [",ccdp4, ccdn4,"]")
            print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"] [",pcdp4,pcdn4,"]")
            print ()

            plag3 = 0
            plag7 = 0

            if icn1 == 1:
                icn1 = 14
            if icn4 == 1:
               icn4 = 14
            if ipn1 == 1:
                ipn1 = 14
            if ipn4 == 1:
                ipn4 = 14
        
            if ipn1 == ipn4:
                plag3 = 1
                plag7 = plag7 + 1
            if icn1 == icn4:
                plag3 = 2
                plag7 = plag7 + 1
            if plag7 == 2:
                plag3 = 0

            if plag3 == 0:
                if icn1 > icn4:
                    icn = icn1
                elif icn1 < icn4:
                    icn = icn4
                if ipn1 > ipn4:
                    ipn = ipn1
                elif ipn1 < ipn4:
                    ipn = ipn4

                if ipn < icn:
                    plag3 = 2
                if ipn > icn:
                    plag3 = 1
                if ipn == icn:
                    plag3 = 0

            if plag3 == 0:
                if icp1 > icp4:
                    icp = icp1
                elif icp1 < icp4:
                    icp = icp4
                if ipp1 > ipp4:
                    ipp = ipp1
                elif ipp1 < ipp4:
                    ipp = ipp4

                if ipp < icp:
                    plag3 = 2
                if ipp > icp:
                    plag3 = 1

            if plag3 == 1:
                print ("나의 선공")
            if plag3 == 2:
                print ("com1의 선공")
            

            if icn1 == 14:
                icn1 = 1
            if icn4 == 14:
                icn4 = 1
            if ipn1 == 14:
                ipn1 = 1
            if ipn4 == 14:
                ipn4 = 1

            if plag3 == 1:
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
                    if ans2 > 0:
                        print ("판돈 올린것을 받아들입니다. 콜")
                        ans4 = ans2
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅 하셨습니다. 총 배팅:",bet)
                    else:
                        print ("돈을 걸지 않습니다. 체크")
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans3 = int(q)
                    if ans3 != 0:
                        if ans3 > 10 :
                            ans3 = 10
                        ans4 = ans3 + ans2
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅하셨습니다.")
                    else:
                        ans4 = ans3 + ans3
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅하셨습니다.")
            
                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans3 = int(q)
                        if ans3 != 0:
                            if ans3 > 10 :
                                ans3 = 10
                            ans4 = ans3 + ans2
                            bet = bet + ans4
                            pm = pm - ans4
                            print (ans4,"배팅하셨습니다.")
                        else:
                            ans4 = ans3
                            bet = bet + ans4
                            pm = pm - ans4
                            print (ans4,"배팅하셨습니다.")
                    
                print ()
                if plag2 == 0:
                    print ("com1의 레이즈")
                    icb2 = int(cb2)
                    ans4 = ans4 + icb2
                    bet = bet + ans4
                    pm = pm - ans4
                    print ("com1이 ",ans4,"배팅 하였습니다. 총 배팅:",bet)
                        
            if plag3 == 2:
                print ()
                print ("com1의 레이즈")
                icb2 = int(cb2)
                ans3 = ans2 + icb2
                bet = bet + ans3
                cm = cm - ans3
                print ("com1이 ",ans3,"배팅 하였습니다. 총 배팅:",bet)

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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans4 = ans3
                    bet = bet + ans4
                    pm = pm - ans4
                    print (ans4,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans4 = int(q)
                    if ans4 != 0:
                        if ans4 > 10 :
                            ans4 = 10
                        ans4 = ans3 + ans4
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅하셨습니다. 총 배팅:",bet)
                    else:
                        print ("판돈 올린것을 받아들입니다. 콜")
                        ans4 = ans3
                        print (ans4,"배팅하셨습니다. 총 배팅:",bet)

                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans4 = int(q)
                        if ans4 > 10 :
                            ans4 = 10
                        if ans4 < 1 :
                            ans4 = 1
                        ans4 = ans3 + ans4
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅하셨습니다. 총 배팅:",bet)
             
            if ccd5 == 4:
                ccdp5 = "스페이드"
            elif ccd5 == 3:
                ccdp5 = "다이아몬드"
            elif ccd5 == 2:
                ccdp5 = "하트"
            elif ccd5 == 1:
                ccdp5 = "클로버"
            
            if pcd5 == 4:
                pcdp5 = "스페이드"
            elif pcd5 == 3:
                pcdp5 = "다이아몬드"
            elif pcd5 == 2:
                pcdp5 = "하트"
            elif pcd5 == 1:
                pcdp5 = "클로버"

        if plag2 != 1:
            
            print ()
            print ()
            print ()
            print ("세번째 턴!")
            print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ] [",ccdp4, ccdn4,"] [",ccdp5,ccdn5,"]")
            print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"] [",pcdp4,pcdn4,"] [",pcdp5,pcdn5,"]")
            print ()
    

            plag4 = 0
            plag5 = 0
            plag6 = 0

            if ipn1 == 1:
                ipn1 = 14
            if ipn4 == 1:
                ipn4 = 14
            if ipn5 == 1:
                ipn5 = 14
            if icn1 == 1:
                icn1 = 14
            if icn4 == 1:
                icn4 = 14
            if icn5 == 1:
                icn5 = 14

            if ipn1 == ipn4 == ipn5:
                plag4 = 1
                plag5 = 1
            if icn1 == icn4 == icn5:
                plag4 = 2
                plag6 = 1
            if plag5 == plag6:
                plag4 = 0

            if plag == 0:
                if ipn1 == ipn4:
                    plag5 = 1
                    plag4 = 1
                if ipn4 == ipn5:
                    plag5 = 1
                    plag4 = 1
                if ipn5 == ipn1:
                    plag5 = 1
                    plag4 = 1

                if icn1 == icn4:
                    plag5 = 1
                    plag4 = 2
                if icn4 == icn5:
                    plag5 = 1
                    plag4 = 2
                if icn5 == icn1:
                    plag5 = 1
                    plag4 = 1

                if plag5 == plag6 == 1:
                    plag4 = 0

            if plag4 == 0:
                if ipn1 > ipn4:
                    ipn = ipn1
                elif ipn1 < ipn4:
                    ipn = ipn4
                if ipn > ipn5:
                    ipn = ipn
                elif ipn1 < ipn5:
                    ipn = ipn5
    
                if icn1 > icn4:
                    icn = icn1
                elif icn1 < icn4:
                    icn = icn4
                if icn > icn5:
                    icn = icn
                elif icn1 < icn5:
                    icn = icn5

                if icn < ipn:
                    plag4 = 1
                elif icn > ipn:
                    plag4 = 2
                elif icn == ipn:
                    plag4 = 0

            if plag4 == 0:
                if ipp1 > ipp4:
                    ipp = ipp1
                elif ipp1 < ipp4:
                    ipp = ipp4
                if ipp > ipp5:
                    ipp = ipp
                elif ipp < ipp5:
                    ipp = ipp5

                if icp1 > icp4:
                    icp = icp1
                elif icp1 < icp4:
                    icp = icp4
                if icp > icp5:
                    icp = icp
                elif icp < icp5:
                    icp = icp5

                if icp < ipp:
                    plag4 = 1
                elif icp > ipp:
                    plag4 = 2
                  

            if plag4 == 1:
                print ("나의 선공")
            elif plag4 == 2:
                print ("com1의 선공")

            if plag4 == 1:
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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans6 = ans4
                    bet = bet + ans6
                    pm = pm - ans6
                    print (ans6,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans6 = int(q)
                    if ans6 != 0:
                        if ans6 > 10 :
                            ans6 = 10
                        ans6 = ans4 + ans6
                        bet = bet + ans6
                        pm = pm - ans6
                        print (ans6,"배팅하셨습니다.")
                    else:
                        ans6 = ans4 + ans5
                        bet = bet + ans6
                        pm = pm - ans6
                        print (ans6,"배팅하셨습니다.")
            
                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans6 = int(q)
                        if ans6 != 0:
                            if ans6 > 10 :
                                ans6 = 10
                            ans6 = ans4 + ans6
                            bet = bet + ans6
                            pm = pm - ans6
                            print (ans5,"배팅하셨습니다.")
                        else:
                            ans6 = ans4
                            bet = bet + ans6
                            pm = pm - ans6
                            print (ans6,"배팅하셨습니다.")
                    
                print ()
                if plag2 == 0:
                    print ("com1의 레이즈")
                    icb3 = int(cb3)
                    ans7 = ans6 + icb3
                    bet = bet + ans7
                    pm = pm - ans7
                    print ("com1이 ",ans7,"배팅 하였습니다. 총 배팅:",bet)
                        
            if plag4 == 2:
                print ()
                print ("com1의 레이즈")
                icb3 = int(cb3)
                ans6 = ans4 + icb3
                bet = bet + ans6
                cm = cm - ans6
                print ("com1이 ",ans6,"배팅 하였습니다. 총 배팅:",bet)

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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans7 = ans6
                    bet = bet + ans7
                    pm = pm - ans7
                    print (ans7,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans7 = int(q)
                    if ans7 != 0:
                        if ans7 > 10 :
                            ans7 = 10
                        ans7 = ans6 + ans7
                        bet = bet + ans7
                        pm = pm - ans7
                        print (ans7,"배팅하셨습니다. 총 배팅:",bet)
                    else:
                        print ("판돈 올린것을 받아들입니다. 콜")
                        ans7 = ans6
                        print (ans7,"배팅하셨습니다. 총 배팅:",bet)

                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans7 = int(q)
                        if ans7 > 10 :
                            ans7 = 10
                        if ans7 < 1 :
                            ans7 = 1
                        ans7 = ans6 + ans7
                        bet = bet + ans7
                        pm = pm - ans7
                        print (ans7,"배팅하셨습니다. 총 배팅:",bet)
    
            if ipn1 == 1:
                ipn1 = 14
            if ipn4 == 1:
                ipn4 = 14
            if ipn5 == 1:
                ipn5 = 14
            if ipn6 == 1:
                ipn6 = 14
            if icn1 == 1:
                icn1 = 14
            if icn4 == 1:
                icn4 = 14
            if icn5 == 1:
                icn5 = 14
            if icn6 == 1:
                icn6 = 14

            plag7 = 0
            plag8 = 0
            plag9 = 0
                
            if ipn1 == ipn4 == ipn5 == ipn6:
                plag7 = 1
                plag8 = 1
            if icn1 == icn4 == icn5 == icn6:
                plag7 = 2
                plag9 = 1
            if plag8 == plag9 == 1:
                if icn1 > ipn1:
                    plag7 = 2
                elif icn1 < ipn2:
                    plag7 = 1

            lists = [ipn1, ipn4, ipn5, ipn6]

            a = 0

            for lst in lists:
                a = a + 1
                if a == 1:
                    iipn1 = lst
                if a == 2:
                    iipn2 = lst
                if a == 3:
                    iipn3 = lst
                if a == 4:
                    iipn4 = lst

            llists = [icn1, icn4, icn5, icn6]

            a = 0

            for lst in lists:
                a = a + 1
                if a == 1:
                    iicn1 = lst
                if a == 2:
                    iicn2 = lst
                if a == 3:
                    iicn3 = lst
                if a == 4:
                    iicn4 = lst
                            
            if plag7 == 0:
                if iicn1 == iicn2 == iicn3:
                    plag7 = 2
                    plag9 = 1
                elif iicn4 == iicn2 == iicn3:
                    plag7 = 2
                    plag9 = 1
                        
                if iipn1 == iipn2 == iipn3:
                    plag7 = 2
                    plag8 = 1
                elif iipn4 == iipn2 == iipn3:
                    plag7 = 2
                    plag8 = 1
                
                if plag8 == plag9 == 1:
                    if ipn5 > icn5:
                        plag7 = 1
                    elif ipn < icn5:
                        plag7 = 2
                
            if plag7 == 0:
                if iipn1 == iipn2:
                    if iipn3 == iipn4:
                        plag7 = 1
                        plag8 = 1

                if iicn1 == iicn2:
                    if iicn3 == iicn4:
                        plag7 = 2
                        plag9 = 1
                if plag8 == plag9 == 1:
                    if iicn1 > iipn1:
                        plag7 = 2
                    elif iicn1 < iipn1:
                        plag7 = 1
                            
            if plag7 == 0:
                if iipn1 == iipn2:
                    plag8 = plag8 + 1
                if iipn2 == iipn3:
                    plag8 = plag8 + 1
                if iipn3 == iipn4:
                    plag8 = plag8 + 1
                        
                if iicn1 == iicn2:
                    plag9 = plag9 + 1
                if iicn2 == iicn3:
                    plag9 = plag9 + 1
                if iicn3 == iicn4:
                    plag9 = plag9 + 1
                        
                if plag9 > plag8:
                    plag7 = 2
                elif plag9 < plag8:
                    plag7 = 1
            
                if plag7 == 0:
                    if iipn1 > iicn1:
                        plag7 = 1
                    elif iipn1 < iicn1:
                        plag7 = 0

            if plag7 == 1:
                print ("나의 선공")
            elif plag7 == 2:
                print ("com1의 선공")
            
            if plag7 == 1:
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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans8 = ans7
                    bet = bet + ans8
                    pm = pm - ans8
                    print (ans8,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans8 = int(q)
                    if ans8 != 0:
                        if ans8 > 10 :
                            ans8 = 10
                        ans8 = ans7 + ans8
                        bet = bet + ans8
                        pm = pm - ans8
                        print (ans8,"배팅하셨습니다.")
                    else:
                        ans8 = ans7 + ans7
                        bet = bet + ans8
                        pm = pm - ans8
                        print (ans8,"배팅하셨습니다.")
            
                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans8 = int(q)
                        if ans8 != 0:
                            if ans8 > 10 :
                                ans8 = 10
                            ans8 = ans7 + ans8
                            bet = bet + ans8
                            pm = pm - ans8
                            print (ans7,"배팅하셨습니다.")
                        else:
                            ans8 = ans7
                            bet = bet + ans8
                            pm = pm - ans8
                            print (ans8,"배팅하셨습니다.")

                print ()
                if plag2 == 0:
                    print ("com1의 레이즈")
                    icb4 = int(cb4)
                    ans8 = ans8 + icb4
                    bet = bet + ans8
                    pm = pm - ans8
                    print ("com1이 ",ans8,"배팅 하였습니다. 총 배팅:",bet)
        
            if plag7 == 2:
                print ()
                print ("com1의 레이즈")
                icb4 = int(cb4)
                ans8 = ans7 + icb4
                bet = bet + ans8
                cm = cm - ans8
                print ("com1이 ",ans8,"배팅 하였습니다. 총 배팅:",bet)
                
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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans8 = ans8
                    bet = bet + ans8
                    pm = pm - ans8
                    print (ans8,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans8 = int(q)
                    if ans8 != 0:
                        if ans8 > 10 :
                            ans8 = 10
                        ans8 = ans8 + ans8
                        bet = bet + ans8
                        pm = pm - ans8
                        print (ans8,"배팅하셨습니다. 총 배팅:",bet)
                    else:
                        print ("판돈 올린것을 받아들입니다. 콜")
                        ans8 = ans8
                        print (ans8,"배팅하셨습니다. 총 배팅:",bet)
            
                if ans == 3:
                    if pm < 100:
                        print ("올인!")
                        bet = bet + pm
                        pm = 0
                        plag2 = 1
                    else:
                        print ("올인은 남은돈이 100 이하일때만 할 수 있습니다. 남은플레이어 돈:",pm)
                        print ("판돈을 올립니다. 레이즈")
                        print ("얼마나 베팅하시겠습니까? (최대 10)")
                        q = input("=")
                        ans8 = int(q)
                        if ans8 > 10 :
                            ans8 = 10
                        if ans8 < 1 :
                            ans8 = 1
                        ans8 = ans8 + ans8
                        bet = bet + ans8
                        pm = pm - ans8
                        print (ans8,"배팅하셨습니다. 총 배팅:",bet)

        bet1 = bet
        
        print ()
        print ()
        print ()
        print ()

        if ccd1 == 4:
            ccdp1 = "스페이드"
        elif ccd1 == 3:
            ccdp1 = "다이아몬드"
        elif ccd1 == 2:
            ccdp1 = "하트"
        elif ccd1 == 1:
            ccdp1 = "클로버"

        if pcd1 == 4:
            pcdp1 = "스페이드"
        elif pcd1 == 3:
            pcdp1 = "다이아몬드"
        elif pcd1 == 2:
            pcdp1 = "하트"
        elif pcd1 == 1:
            pcdp1 = "클로버"

        if ccd2 == 4:
            ccdp2 = "스페이드"
        elif ccd2 == 3:
            ccdp2 = "다이아몬드"
        elif ccd2 == 2:
            ccdp2 = "하트"
        elif ccd2 == 1:
            ccdp2 = "클로버"

        if pcd2 == 4:
            pcdp2 = "스페이드"
        elif pcd2 == 3:
            pcdp2 = "다이아몬드"
        elif pcd2 == 2:
            pcdp2 = "하트"
        elif pcd2 == 1:
            pcdp2 = "클로버"

        if ccd3 == 4:
            ccdp3 = "스페이드"
        elif ccd3 == 3:
            ccdp3 = "다이아몬드"
        elif ccd3 == 2:
            ccdp3 = "하트"
        elif ccd3 == 1:
            ccdp3 = "클로버"

        if pcd3 == 4:
            pcdp3 = "스페이드"
        elif pcd3 == 3:
            pcdp3 = "다이아몬드"
        elif pcd3 == 2:
            pcdp3 = "하트"
        elif pcd3 == 1:
            pcdp3 = "클로버"

        if ccd4 == 4:
            ccdp4 = "스페이드"
        elif ccd4 == 3:
            ccdp4 = "다이아몬드"
        elif ccd4 == 2:
            ccdp4 = "하트"
        elif ccd4 == 1:
            ccdp4 = "클로버"

        if pcd4 == 4:
            pcdp4 = "스페이드"
        elif pcd4 == 3:
            pcdp4 = "다이아몬드"
        elif pcd4 == 2:
            pcdp4 = "하트"
        elif pcd4 == 1:
            pcdp4 = "클로버"
            
        if ccd5 == 4:
            ccdp5 = "스페이드"
        elif ccd5 == 3:
            ccdp5 = "다이아몬드"
        elif ccd5 == 2:
            ccdp5 = "하트"
        elif ccd5 == 1:
            ccdp5 = "클로버"
        
        if pcd5 == 4:
            pcdp5 = "스페이드"
        elif pcd5 == 3:
            pcdp5 = "다이아몬드"
        elif pcd5 == 2:
            pcdp5 = "하트"
        elif pcd5 == 1:
            pcdp5 = "클로버"
        
        if ccd6 == 4:
            ccdp6 = "스페이드"
        elif ccd6 == 3:
            ccdp6 = "다이아몬드"
        elif ccd6 == 2:
            ccdp6 = "하트"
        elif ccd6 == 1:
            ccdp6 = "클로버"
            
        if pcd6 == 4:
            pcdp6 = "스페이드"
        elif pcd6 == 3:
            pcdp6 = "다이아몬드"
        elif pcd6 == 2:
            pcdp6 = "하트"
        elif pcd6 == 1:
            pcdp6 = "클로버"

        if ccd7 == 4:
            ccdp7 = "스페이드"
        elif ccd7 == 3:
            ccdp7 = "다이아몬드"
        elif ccd7 == 2:
            ccdp7 = "하트"
        elif ccd7 == 1:
            ccdp7 = "클로버"
            
        if pcd7 == 4:
            pcdp7 = "스페이드"
        elif pcd7 == 3:
            pcdp7 = "다이아몬드"
        elif pcd7 == 2:
            pcdp7 = "하트"
        elif pcd7 == 1:
            pcdp7 = "클로버"
            
            
        print ("com1의 패:[",ccdp1, ccdn1,"] [",ccdp2, ccdn2,"] [",ccdp3,ccdn3,"] [",ccdp4, ccdn4,"] [",ccdp5,ccdn5,"][",ccdp6, ccdn6,"] [",ccdp7,ccdn7,"]")
        print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"] [",pcdp4,pcdn4,"] [",pcdp5,pcdn5,"] [",pcdp6,pcdn6,"] [",pcdp7,pcdn7,"]")
        print ()
        print ()
        print ()
        
        if plag2 == 0:
            ppat1 = 0
            ppat2 = 0
            ppat3 = 0
            ppat4 = 0

            eplag1 = 0
            eplag2 = 0
            eplag3 = 0
            eplag4 = 0

            pnum1 = 0
            pnum2 = 0
            pnum3 = 0
            pnum4 = 0
            pnum5 = 0
            pnum6 = 0
            pnum7 = 0

            ppn1 = 0
            ppn2 = 0
            ppn3 = 0
            ppn4 = 0
            ppn5 = 0
            ppn6 = 0
            ppn7 = 0

            a = 0

            player = 100000

            if pcdn1 == 1:
                pcdn1 = 14
            if pcdn2 == 1:
                pcdn2 = 14
            if pcdn3 == 1:
                pcdn3 = 14
            if pcdn4 == 1:
                pcdn4 = 14
            if pcdn5 == 1:
                pcdn5 = 14
            if pcdn6 == 1:
                pcdn6 = 14
            if pcdn7 == 1:
                pcdn7 = 14

            lists = [pcd1, pcd2, pcd3, pcd4, pcd5, pcd6, pcd7]

            a = 0

            for lst in lists:
                if lst == 4:
                    ppat1 = ppat1 + 1
                if lst == 3:
                    ppat2 = ppat2 + 1
                if lst == 2:
                    ppat3 = ppat3 + 1
                if lst == 1:
                    ppat4 = ppat4 + 1

            if ppat1 >= 5:
                if pcd1 == 4:
                    if pcdn1 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn1 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn1 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn1 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn1 == 10:
                        eplag1 = eplag1 + 1
                if pcd2 == 4:
                    if pcdn2 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn2 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn2 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn2 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn2 == 10:
                        eplag1 = eplag1 + 1
                if pcd3 == 4:
                    if pcdn3 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn3 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn3 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn3 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn3 == 10:
                        eplag1 = eplag1 + 1
                if pcd4 == 4:
                    if pcdn4 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn4 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn4 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn4 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn4 == 10:
                        eplag1 = eplag1 + 1
                if pcd5 == 4:
                    if pcdn5 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn5 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn5 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn5 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn5 == 10:
                        eplag1 = eplag1 + 1
                if pcd6 == 4:
                    if pcdn6 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn6 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn6 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn6 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn6 == 10:
                        eplag1 = eplag1 + 1
                if pcd7 == 4:
                    if pcdn7 == 14:
                        eplag1 = eplag1 + 1
                    if pcdn7 == 13:
                        eplag1 = eplag1 + 1
                    if pcdn7 == 12:
                        eplag1 = eplag1 + 1
                    if pcdn7 == 11:
                        eplag1 = eplag1 + 1
                    if pcdn7 == 10:
                        eplag1 = eplag1 + 1
            if ppat2 >= 5:
                if pcd1 == 3:
                    if pcdn1 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn1 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn1 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn1 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn1 == 10:
                        eplag2 = eplag2 + 1
                if pcd2 == 3:
                    if pcdn2 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn2 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn2 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn2 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn2 == 10:
                        eplag2 = eplag2 + 1
                if pcd3 == 3:
                    if pcdn3 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn3 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn3 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn3 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn3 == 10:
                        eplag2 = eplag2 + 1
                if pcd4 == 3:
                    if pcdn4 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn4 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn4 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn4 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn4 == 10:
                        eplag2 = eplag2 + 1
                if pcd5 == 3:
                    if pcdn5 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn5 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn5 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn5 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn5 == 10:
                        eplag2 = eplag2 + 1
                if pcd6 == 3:
                    if pcdn6 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn6 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn6 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn6 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn6 == 10:
                        eplag2 = eplag2 + 1
                if pcd7 == 3:
                    if pcdn7 == 14:
                        eplag2 = eplag2 + 1
                    if pcdn7 == 13:
                        eplag2 = eplag2 + 1
                    if pcdn7 == 12:
                        eplag2 = eplag2 + 1
                    if pcdn7 == 11:
                        eplag2 = eplag2 + 1
                    if pcdn7 == 10:
                        eplag2 = eplag2 + 1
            if ppat3 >= 5:
                if pcd1 == 2:
                    if pcdn1 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn1 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn1 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn1 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn1 == 10:
                        eplag3 = eplag3 + 1
                if pcd2 == 2:
                    if pcdn2 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn2 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn2 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn2 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn2 == 10:
                        eplag3 = eplag3 + 1
                if pcd3 == 2:
                    if pcdn3 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn3 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn3 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn3 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn3 == 10:
                        eplag3 = eplag3 + 1
                if pcd4 == 2:
                    if pcdn4 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn4 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn4 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn4 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn4 == 10:
                        eplag3 = eplag3 + 1
                if pcd5 == 2:
                    if pcdn5 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn5 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn5 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn5 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn5 == 10:
                        eplag3 = eplag3 + 1
                if pcd6 == 2:
                    if pcdn6 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn6 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn6 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn6 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn6 == 10:
                        eplag3 = eplag3 + 1
                if pcd7 == 2:
                    if pcdn7 == 14:
                        eplag3 = eplag3 + 1
                    if pcdn7 == 13:
                        eplag3 = eplag3 + 1
                    if pcdn7 == 12:
                        eplag3 = eplag3 + 1
                    if pcdn7 == 11:
                        eplag3 = eplag3 + 1
                    if pcdn7 == 10:
                        eplag3 = eplag3 + 1
            if ppat4 >= 5:
                if pcd1 == 1:
                    if pcdn1 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn1 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn1 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn1 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn1 == 10:
                        eplag4 = eplag4 + 1
                if pcd2 == 1:
                    if pcdn2 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn2 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn2 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn2 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn2 == 10:
                        eplag4 = eplag4 + 1
                if pcd3 == 1:
                    if pcdn3 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn3 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn3 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn3 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn3 == 10:
                        eplag4 = eplag4 + 1
                if pcd4 == 1:
                    if pcdn4 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn4 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn4 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn4 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn4 == 10:
                        eplag4 = eplag4 + 1
                if pcd5 == 1:
                    if pcdn5 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn5 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn5 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn5 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn5 == 10:
                        eplag4 = eplag4 + 1
                if pcd6 == 1:
                    if pcdn6 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn6 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn6 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn6 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn6 == 10:
                        eplag4 = eplag4 + 1
                if pcd7 == 1:
                    if pcdn7 == 14:
                        eplag4 = eplag4 + 1
                    if pcdn7 == 13:
                        eplag4 = eplag4 + 1
                    if pcdn7 == 12:
                        eplag4 = eplag4 + 1
                    if pcdn7 == 11:
                        eplag4 = eplag4 + 1
                    if pcdn7 == 10:
                        eplag4 = eplag4 + 1
            if eplag1 >= 5:
                if player > 1:
                    player = 1
            if eplag2 >= 5:
                if player > 2:
                    player = 2
            if eplag3 >= 5:
                if player > 3:
                    player = 3
            if eplag4 >= 5:
                if player > 4:
                    player = 4

            plists = [pcd1, pcd2, pcd3, pcd4, pcd5, pcd6, pcd7]

            plists.sort(reverse=True)

            a = 0

            for b in plists:
                a = a + 1
                if a == 1:
                    ppet1 = b
                if a == 2:
                    ppet2 = b
                if a == 3:
                    ppet3 = b
                if a == 4:
                    ppet4 = b
                if a == 5:
                    ppet5 = b
                if a == 6:
                    ppet6 = b
                if a == 7:
                    ppet7 = b

            if ppet1 == ppet2 == ppet3 == ppet4 == ppet5:
                if ppet1 == pcd1:
                    ppn1 = pcdn1
                if ppet1 == pcd2:
                    ppn2 = pcdn2
                if ppet1 == pcd3:
                    ppn3 = pcdn3
                if ppet1 == pcd4:
                    ppn4 = pcdn4
                if ppet1 == pcd5:
                    ppn5 = pcdn5
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd7:
                    ppn7 = pcdn7
            if ppet2 == ppet3 == ppet4 == ppet5 == ppet6:
                if ppet2 == pcd1:
                    ppn1 = pcdn1
                if ppet2 == pcd2:
                    ppn2 = pcdn2
                if ppet2 == pcd3:
                    ppn3 = pcdn3
                if ppet2 == pcd4:
                    ppn4 = pcdn4
                if ppet2 == pcd5:
                    ppn5 = pcdn5
                if ppet2 == pcd6:
                    ppn6 = pcdn6
                if ppet2 == pcd6:
                    ppn6 = pcdn6
                if ppet2 == pcd7:
                    ppn7 = pcdn7
            if ppet3 == ppet4 == ppet5 == ppet6 == ppet7:
                if ppet3 == pcd1:
                    ppn1 = pcdn1
                if ppet3 == pcd2:
                    ppn2 = pcdn2
                if ppet3 == pcd3:
                    ppn3 = pcdn3
                if ppet3 == pcd4:
                    ppn4 = pcdn4
                if ppet3 == pcd5:
                    ppn5 = pcdn5
                if ppet3 == pcd6:
                    ppn6 = pcdn6
                if ppet3 == pcd6:
                    ppn6 = pcdn6
                if ppet3 == pcd7:
                    ppn7 = pcdn7


            a = 0

            pnum = [ppn1, ppn2, ppn3, ppn4, ppn5, ppn6, ppn7]

            pnum.sort(reverse=True)

            for b in pnum:
                a = a + 1
                if a == 1:
                    pum1 = b
                if a == 2:
                    pum2 = b
                if a == 3:
                    pum3 = b
                if a == 4:
                    pum4 = b
                if a == 5:
                    pum5 = b
                if a == 6:
                    pum6 = b
                if a == 7:
                    pum7 = b

            if pum1 == 14:
                if pum2 == 5:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if player > 6:
                                    player = 6

            if pum1 == 6:
                if pum2 == 5:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if player > 7:
                                    player = 17

            if pum1 == 7:
                if pum2 == 6:
                    if pum3 == 5:
                        if pum4 == 4:
                            if pum5 == 3:
                                if player > 8:
                                    player = 16

            if pum1 == 8:
                if pum2 == 7:
                    if pum3 == 6:
                        if pum4 == 5:
                            if pum5 == 4:
                                if player > 9:
                                    player = 15

            if pum1 == 9:
                if pum2 == 8:
                    if pum3 == 7:
                        if pum4 == 6:
                            if pum5 == 5:
                                if player > 10:
                                    player = 14

            if pum1 == 10:
                if pum2 == 9:
                    if pum3 == 8:
                        if pum4 == 7:
                            if pum5 == 6:
                                if player > 11:
                                    player = 13

            if pum1 == 11:
                if pum2 == 10:
                    if pum3 == 9:
                        if pum4 == 8:
                            if pum5 == 7:
                                if player > 12:
                                    player = 12

            if pum1 == 12:
                if pum2 == 11:
                    if pum3 == 10:
                        if pum4 == 9:
                            if pum5 == 8:
                                if player > 13:
                                    player = 11

            if pum1 == 13:
                if pum2 == 12:
                    if pum3 == 11:
                        if pum4 == 10:
                            if pum5 == 9:
                                if player > 14:
                                    player = 10

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 12:
                        if pum4 == 11:
                            if pum5 == 2:
                                if player > 15:
                                    player = 9

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 12:
                        if pum4 == 3:
                            if pum5 == 2:
                                if player > 16:
                                    player = 8

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if player > 17:
                                    player = 7

            a = 0

            pnum1 = [pcdn1, pcdn2, pcdn3, pcdn4, pcdn5, pcdn6, pcdn7]

            pnum1.sort(reverse=True)

            for b in pnum1:
                a = a + 1
                if a == 1:
                    pum1 = b
                if a == 2:
                    pum2 = b
                if a == 3:
                    pum3 = b
                if a == 4:
                    pum4 = b
                if a == 5:
                    pum5 = b
                if a == 6:
                    pum6 = b
                if a == 7:
                    pum7 = b

            if pum1 == pum2 == pum3 == pum4:
                if pum4 == 14:
                    if player > 20:
                        player = 20
                if pum4 == 2:
                    if player > 32:
                        player = 32
                if pum4 == 3:
                    if player > 31:
                        player = 31
                if pum4 == 4:
                    if player > 30:
                        player = 30
                if pum4 == 5:
                    if player > 29:
                        player = 29
                if pum4 == 6:
                    if player > 28:
                        player = 28
                if pum4 == 7:
                    if player > 27:
                        player = 27
                if pum4 == 8:
                    if player > 26:
                        player = 26
                if pum4 == 9:
                    if player > 25:
                        player = 25
                if pum4 == 10:
                    if player > 24:
                        player = 24
                if pum4 == 11:
                    if player > 23:
                        player = 23
                if pum4 == 12:
                    if player > 22:
                        player = 22
                if pum4 == 13:
                    if player > 21:
                        player = 21

            if pum2 == pum3 == pum4 == pum5:
                if pum4 == 14:
                    if player > 20:
                        player = 20
                if pum4 == 2:
                    if player > 32:
                        player = 32
                if pum4 == 3:
                    if player > 31:
                        player = 31
                if pum4 == 4:
                    if player > 30:
                        player = 30
                if pum4 == 5:
                    if player > 29:
                        player = 29
                if pum4 == 6:
                    if player > 28:
                        player = 28
                if pum4 == 7:
                    if player > 27:
                        player = 27
                if pum4 == 8:
                    if player > 26:
                        player = 26
                if pum4 == 9:
                    if player > 25:
                        player = 25
                if pum4 == 10:
                    if player > 24:
                        player = 24
                if pum4 == 11:
                    if player > 23:
                        player = 23
                if pum4 == 12:
                    if player > 22:
                        player = 22
                if pum4 == 13:
                    if player > 21:
                        player = 21

            if pum3 == pum4 == pum5 == pum6:
                if pum4 == 14:
                    if player > 20:
                        player = 20
                if pum4 == 2:
                    if player > 32:
                        player = 32
                if pum4 == 3:
                    if player > 31:
                        player = 31
                if pum4 == 4:
                    if player > 30:
                        player = 30
                if pum4 == 5:
                    if player > 29:
                        player = 29
                if pum4 == 6:
                    if player > 28:
                        player = 28
                if pum4 == 7:
                    if player > 27:
                        player = 27
                if pum4 == 8:
                    if player > 26:
                        player = 26
                if pum4 == 9:
                    if player > 25:
                        player = 25
                if pum4 == 10:
                    if player > 24:
                        player = 24
                if pum4 == 11:
                    if player > 23:
                        player = 23
                if pum4 == 12:
                    if player > 22:
                        player = 22
                if pum4 == 13:
                    if player > 21:
                        player = 21

            if pum4 == pum5 == pum6 == pum7:
                if pum4 == 14:
                    if player > 20:
                        player = 20
                if pum4 == 2:
                    if player > 32:
                        player = 32
                if pum4 == 3:
                    if player > 31:
                        player = 31
                if pum4 == 4:
                    if player > 30:
                        player = 30
                if pum4 == 5:
                    if player > 29:
                        player = 29
                if pum4 == 6:
                    if player > 28:
                        player = 28
                if pum4 == 7:
                    if player > 27:
                        player = 27
                if pum4 == 8:
                    if player > 26:
                        player = 26
                if pum4 == 9:
                    if player > 25:
                        player = 25
                if pum4 == 10:
                    if player > 24:
                        player = 24
                if pum4 == 11:
                    if player > 23:
                        player = 23
                if pum4 == 12:
                    if player > 22:
                        player = 22
                if pum4 == 13:
                    if player > 21:
                        player = 21

            if pum1 == pum2:
                if pum3 == pum4 == pum5:
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum1 == pum2 == pum3:
                if pum4 == pum5:
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum1 == pum2:
                if pum4 == pum5 == pum6:
                    if pum4 == 14:
                        if player > 35:
                            player = 35
                    if pum4 == 2:
                        if player > 47:
                            player = 47
                    if pum4 == 3:
                        if player > 46:
                            player = 46
                    if pum4 == 4:
                        if player > 45:
                            player = 45
                    if pum4 == 5:
                        if player > 44:
                            player = 44
                    if pum4 == 6:
                        if player > 43:
                            player = 43
                    if pum4 == 7:
                        if player > 42:
                           player = 42
                    if pum4 == 8:
                        if player > 41:
                            player = 41
                    if pum4 == 9:
                        if player > 40:
                            player = 40
                    if pum4 == 10:
                        if player > 39:
                            player = 39
                    if pum4 == 11:
                        if player > 38:
                            player = 38
                    if pum4 == 12:
                        if player > 37:
                            player = 37
                    if pum4 == 13:
                        if player > 36:
                            player = 36

            if pum2 == pum3 == pum4:
                if pum5 == pum6:
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum2 == pum3:
                if pum4 == pum5 == pum6:
                    if pum4 == 14:
                        if player > 35:
                            player = 35
                    if pum4 == 2:
                        if player > 47:
                            player = 47
                    if pum4 == 3:
                        if player > 46:
                            player = 46
                    if pum4 == 4:
                        if player > 45:
                            player = 45
                    if pum4 == 5:
                        if player > 44:
                            player = 44
                    if pum4 == 6:
                        if player > 43:
                            player = 43
                    if pum4 == 7:
                        if player > 42:
                           player = 42
                    if pum4 == 8:
                        if player > 41:
                            player = 41
                    if pum4 == 9:
                        if player > 40:
                            player = 40
                    if pum4 == 10:
                        if player > 39:
                            player = 39
                    if pum4 == 11:
                        if player > 38:
                            player = 38
                    if pum4 == 12:
                        if player > 37:
                            player = 37
                    if pum4 == 13:
                        if player > 36:
                            player = 36

            if pum1 == pum2 == pum3:
                if pum6 == pum7:
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum1 == pum2 == pum3:
                if pum5 == pum6 :
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum1 == pum2:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if player > 35:
                            player = 35
                    if pum5 == 2:
                        if player > 47:
                            player = 47
                    if pum5 == 3:
                        if player > 46:
                            player = 46
                    if pum5 == 4:
                        if player > 45:
                            player = 45
                    if pum5 == 5:
                        if player > 44:
                            player = 44
                    if pum5 == 6:
                        if player > 43:
                            player = 43
                    if pum5 == 7:
                        if player > 42:
                           player = 42
                    if pum5 == 8:
                        if player > 41:
                            player = 41
                    if pum5 == 9:
                        if player > 40:
                            player = 40
                    if pum5 == 10:
                        if player > 39:
                            player = 39
                    if pum5 == 11:
                        if player > 38:
                            player = 38
                    if pum5 == 12:
                        if player > 37:
                            player = 37
                    if pum5 == 13:
                        if player > 36:
                            player = 36

            if pum2 == pum3 == pum4:
                if pum6 == pum7:
                    if pum3 == 14:
                        if player > 35:
                            player = 35
                    if pum3 == 2:
                        if player > 47:
                            player = 47
                    if pum3 == 3:
                        if player > 46:
                            player = 46
                    if pum3 == 4:
                        if player > 45:
                            player = 45
                    if pum3 == 5:
                        if player > 44:
                            player = 44
                    if pum3 == 6:
                        if player > 43:
                            player = 43
                    if pum3 == 7:
                        if player > 42:
                           player = 42
                    if pum3 == 8:
                        if player > 41:
                            player = 41
                    if pum3 == 9:
                        if player > 40:
                            player = 40
                    if pum3 == 10:
                        if player > 39:
                            player = 39
                    if pum3 == 11:
                        if player > 38:
                            player = 38
                    if pum3 == 12:
                        if player > 37:
                            player = 37
                    if pum3 == 13:
                        if player > 36:
                            player = 36

            if pum2 == pum3:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if player > 35:
                            player = 35
                    if pum5 == 2:
                        if player > 47:
                            player = 47
                    if pum5 == 3:
                        if player > 46:
                            player = 46
                    if pum5 == 4:
                        if player > 45:
                            player = 45
                    if pum5 == 5:
                        if player > 44:
                            player = 44
                    if pum5 == 6:
                        if player > 43:
                            player = 43
                    if pum5 == 7:
                        if player > 42:
                           player = 42
                    if pum5 == 8:
                        if player > 41:
                            player = 41
                    if pum5 == 9:
                        if player > 40:
                            player = 40
                    if pum5 == 10:
                        if player > 39:
                            player = 39
                    if pum5 == 11:
                        if player > 38:
                            player = 38
                    if pum5 == 12:
                        if player > 37:
                            player = 37
                    if pum5 == 13:
                        if player > 36:
                            player = 36

            if pum3 == pum4:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if player > 35:
                            player = 35
                    if pum5 == 2:
                        if player > 47:
                            player = 47
                    if pum5 == 3:
                        if player > 46:
                            player = 46
                    if pum5 == 4:
                        if player > 45:
                            player = 45
                    if pum5 == 5:
                        if player > 44:
                            player = 44
                    if pum5 == 6:
                        if player > 43:
                            player = 43
                    if pum5 == 7:
                        if player > 42:
                           player = 42
                    if pum5 == 8:
                        if player > 41:
                            player = 41
                    if pum5 == 9:
                        if player > 40:
                            player = 40
                    if pum5 == 10:
                        if player > 39:
                            player = 39
                    if pum5 == 11:
                        if player > 38:
                            player = 38
                    if pum5 == 12:
                        if player > 37:
                            player = 37
                    if pum5 == 13:
                        if player > 36:
                            player = 36

            if ppet1 == ppet2 == ppet3 == ppet4 == ppet5:
                if ppet1 == pcd1:
                    ppn1 = pcdn1
                if ppet1 == pcd2:
                    ppn2 = pcdn2
                if ppet1 == pcd3:
                    ppn3 = pcdn3
                if ppet1 == pcd4:
                    ppn4 = pcdn4
                if ppet1 == pcd5:
                    ppn5 = pcdn5
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd7:
                    ppn7 = pcdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if player > 50:
                        player = 50
                if pum5 == 2:
                    if player > 62:
                        player = 62
                if pum5 == 3:
                    if player > 61:
                        player = 61
                if pum5 == 4:
                    if player > 60:
                        player = 60
                if pum5 == 5:
                    if player > 59:
                        player = 59
                if pum5 == 6:
                    if player > 58:
                        player = 58
                if pum5 == 7:
                    if player > 57:
                        player = 57
                if pum5 == 8:
                    if player > 56:
                        player = 56
                if pum5 == 9:
                    if player > 55:
                        player = 55
                if pum5 == 10:
                    if player > 54:
                        player = 54
                if pum5 == 11:
                    if player > 53:
                        player = 53
                if pum5 == 12:
                    if player > 52:
                        player = 52
                if pum5 == 13:
                    if player > 51:
                        player = 51

            if ppet2 == ppet3 == ppet4 == ppet5 == ppet6:
                if ppet1 == pcd1:
                    ppn1 = pcdn1
                if ppet1 == pcd2:
                    ppn2 = pcdn2
                if ppet1 == pcd3:
                    ppn3 = pcdn3
                if ppet1 == pcd4:
                    ppn4 = pcdn4
                if ppet1 == pcd5:
                    ppn5 = pcdn5
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd7:
                    ppn7 = pcdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if player > 50:
                        player = 50
                if pum5 == 2:
                    if player > 62:
                        player = 62
                if pum5 == 3:
                    if player > 61:
                        player = 61
                if pum5 == 4:
                    if player > 60:
                        player = 60
                if pum5 == 5:
                    if player > 59:
                        player = 59
                if pum5 == 6:
                    if player > 58:
                        player = 58
                if pum5 == 7:
                    if player > 57:
                        player = 57
                if pum5 == 8:
                    if player > 56:
                        player = 56
                if pum5 == 9:
                    if player > 55:
                        player = 55
                if pum5 == 10:
                    if player > 54:
                        player = 54
                if pum5 == 11:
                    if player > 53:
                        player = 53
                if pum5 == 12:
                    if player > 52:
                        player = 52
                if pum5 == 13:
                    if player > 51:
                        player = 51
            if ppet3 == ppet4 == ppet5 == ppet6 == ppet7:
                if ppet1 == pcd1:
                    ppn1 = pcdn1
                if ppet1 == pcd2:
                    ppn2 = pcdn2
                if ppet1 == pcd3:
                    ppn3 = pcdn3
                if ppet1 == pcd4:
                    ppn4 = pcdn4
                if ppet1 == pcd5:
                    ppn5 = pcdn5
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd6:
                    ppn6 = pcdn6
                if ppet1 == pcd7:
                    ppn7 = pcdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if player > 50:
                        player = 50
                if pum5 == 2:
                    if player > 62:
                        player = 62
                if pum5 == 3:
                    if player > 61:
                        player = 61
                if pum5 == 4:
                    if player > 60:
                        player = 60
                if pum5 == 5:
                    if player > 59:
                        player = 59
                if pum5 == 6:
                    if player > 58:
                        player = 58
                if pum5 == 7:
                    if player > 57:
                        player = 57
                if pum5 == 8:
                    if player > 56:
                        player = 56
                if pum5 == 9:
                    if player > 55:
                        player = 55
                if pum5 == 10:
                    if player > 54:
                        player = 54
                if pum5 == 11:
                    if player > 53:
                        player = 53
                if pum5 == 12:
                    if player > 52:
                        player = 52
                if pum5 == 13:
                    if player > 51:
                        player = 51

            plag8 = 0
            pum = 0

            if pum7 + 1 == pum6:
                plag8 = plag8 + 1

            if pum7 + 1 == pum5:
                plag8 = plag8 + 1
            if pum6 + 1 == pum5:
                plag8 = plag8 + 1

            if pum7 + 1 == pum4:
                plag8 = plag8 + 1
            if pum6 + 1 == pum4:
                plag8 = plag8 + 1
            if pum5 + 1 == pum4:
                plag8 = plag8 + 1

            if pum6 + 1 == pum3:
                plag8 = plag8 + 1
            if pum5 + 1 == pum3:
                plag8 = plag8 + 1
            if pum4 + 1 == pum3:
                plag8 = plag8 + 1

            if pum3 + 1 == pum2:
                plag8 = plag8 + 1
            if pum4 + 1 == pum2:
                plag8 = plag8 + 1
            if pum3 + 1 == pum2:
                plag8 = plag8 + 1

            if pum4 + 1 == pum1:
                plag8 = plag8 + 1
            if pum3 + 1 == pum1:
                plag8 = plag8 + 1
            if pum2 + 1 == pum1:
                plag8 = plag8 + 1

            if plag8 == 6:
                player = 70


            if pum1 == pum2 == pum3:
                if pum3 == 14:
                    if player > 80:
                        player = 80
                if pum3 == 2:
                    if player > 92:
                        player = 92
                if pum3 == 3:
                    if player > 91:
                        player = 91
                if pum3 == 4:
                    if player > 90:
                        player = 90
                if pum3 == 5:
                    if player > 89:
                        player = 89
                if pum3 == 6:
                    if player > 88:
                        player = 88
                if pum3 == 7:
                    if player > 87:
                        player = 87
                if pum3 == 8:
                    if player > 86:
                        player = 86
                if pum3 == 9:
                    if player > 85:
                        player = 85
                if pum3 == 10:
                    if player > 84:
                        player = 84
                if pum3 == 11:
                    if player > 83:
                        player = 83
                if pum3 == 12:
                    if player > 82:
                        player = 82
                if pum3 == 13:
                    if player > 81:
                        player = 81
            if pum2 == pum3 == pum4:
                if pum3 == 14:
                    if player > 80:
                        player = 80
                if pum3 == 2:
                    if player > 92:
                        player = 92
                if pum3 == 3:
                    if player > 91:
                        player = 91
                if pum3 == 4:
                    if player > 90:
                        player = 90
                if pum3 == 5:
                    if player > 89:
                        player = 89
                if pum3 == 6:
                    if player > 88:
                        player = 88
                if pum3 == 7:
                    if player > 87:
                        player = 87
                if pum3 == 8:
                    if player > 86:
                        player = 86
                if pum3 == 9:
                    if player > 85:
                        player = 85
                if pum3 == 10:
                    if player > 84:
                        player = 84
                if pum3 == 11:
                    if player > 83:
                        player = 83
                if pum3 == 12:
                    if player > 82:
                        player = 82
                if pum3 == 13:
                    if player > 81:
                        player = 81
            if pum3 == pum4 == pum5:
                if pum3 == 14:
                    if player > 80:
                        player = 80
                if pum3 == 2:
                    if player > 92:
                        player = 92
                if pum3 == 3:
                    if player > 91:
                        player = 91
                if pum3 == 4:
                    if player > 90:
                        player = 90
                if pum3 == 5:
                    if player > 89:
                        player = 89
                if pum3 == 6:
                    if player > 88:
                        player = 88
                if pum3 == 7:
                    if player > 87:
                        player = 87
                if pum3 == 8:
                    if player > 86:
                        player = 86
                if pum3 == 9:
                    if player > 85:
                        player = 85
                if pum3 == 10:
                    if player > 84:
                        player = 84
                if pum3 == 11:
                    if player > 83:
                        player = 83
                if pum3 == 12:
                    if player > 82:
                        player = 82
                if pum3 == 13:
                    if player > 81:
                        player = 81
            if pum4 == pum5 == pum6:
                if pum3 == 14:
                    if player > 80:
                        player = 80
                if pum3 == 2:
                    if player > 92:
                        player = 92
                if pum3 == 3:
                    if player > 91:
                        player = 91
                if pum3 == 4:
                    if player > 90:
                        player = 90
                if pum3 == 5:
                    if player > 89:
                        player = 89
                if pum3 == 6:
                    if player > 88:
                        player = 88
                if pum3 == 7:
                    if player > 87:
                        player = 87
                if pum3 == 8:
                    if player > 86:
                        player = 86
                if pum3 == 9:
                    if player > 85:
                        player = 85
                if pum3 == 10:
                    if player > 84:
                        player = 84
                if pum3 == 11:
                    if player > 83:
                        player = 83
                if pum3 == 12:
                    if player > 82:
                        player = 82
                if pum3 == 13:
                    if player > 81:
                        player = 81
            if pum5 == pum6 == pum7:
                if pum3 == 14:
                    if player > 80:
                        player = 80
                if pum3 == 2:
                    if player > 92:
                        player = 92
                if pum3 == 3:
                    if player > 91:
                        player = 91
                if pum3 == 4:
                    if player > 90:
                        player = 90
                if pum3 == 5:
                    if player > 89:
                        player = 89
                if pum3 == 6:
                    if player > 88:
                        player = 88
                if pum3 == 7:
                    if player > 87:
                        player = 87
                if pum3 == 8:
                    if player > 86:
                        player = 86
                if pum3 == 9:
                    if player > 85:
                        player = 85
                if pum3 == 10:
                    if player > 84:
                        player = 84
                if pum3 == 11:
                    if player > 83:
                        player = 83
                if pum3 == 12:
                    if player > 82:
                        player = 82
                if pum3 == 13:
                    if player > 81:
                        player = 81

            plag8 = 0
            plag9 = 0

            if pum1 == pum2:
                if pum2 == pum3:
                    if pum3 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum3 == 3:
                        if player > 111:
                            player = 111
                            
                    if pum3 == 4:
                        if player > 110:
                            player = 110

                    if pum3 == 5:
                        if player > 109:
                            player = 109

                    if pum3 == 6:
                        if player > 108:
                            player = 108

                    if pum3 == 7:
                        if player > 107:
                            player = 107

                    if pum3 == 8:
                        if player > 106:
                            player = 106

                    if pum3 == 9:
                        if player > 105:
                            player = 105

                    if pum3 == 10:
                        if player > 104:
                            player = 104

                    if pum3 == 11:
                        if player > 103:
                            player = 103

                    if pum3 == 12:
                        if player > 102:
                            player = 102

                    if pum3 == 13:
                        if player > 101:
                            player = 101

                    if pum3 == 14:
                        if player > 100:
                            player = 100

                if pum3 == pum4:
                    if pum3 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum3 == 3:
                        if player > 111:
                            player = 111

                    if pum3 == 4:
                        if player > 110:
                            player = 110

                    if pum3 == 5:
                        if player > 109:
                            player = 109
                    
                    if pum3 == 6:
                        if player > 108:
                            player = 108

                    if pum3 == 7:
                        if player > 107:
                            player = 107

                    if pum3 == 8:
                        if player > 106:
                            player = 106

                    if pum3 == 9:
                        if player > 105:
                            player = 105

                    if pum3 == 10:
                        if player > 104:
                            player = 104

                    if pum3 == 11:
                        if player > 103:
                            player = 103

                    if pum3 == 12:
                        if player > 102:
                            player = 102

                    if pum3 == 13:
                        if player > 101:
                            player = 101

                    if pum3 == 14:
                        if player > 100:
                            player = 100

                if pum4 == pum5:
                    if pum5 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum5 == 3:
                        if player > 111:
                            player = 111
                    
                    if pum5 == 4:
                        if player > 110:
                            player = 110

                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107
                    
                    if pum5 == 8:
                        if player > 106:
                            player = 106

                    if pum5 == 9:
                        if player > 105:
                            player = 105

                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum5 == 3:
                        if player > 111:
                            player = 111

                    if pum5 == 4:
                        if player > 110:
                            player = 110
                    
                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106
                    
                    if pum5 == 9:
                        if player > 105:
                            player = 105

                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102
                    
                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if player > 112:
                            player = 112

                    if pum7 == 3:
                        if player > 111:
                            player = 111

                    if pum7 == 4:
                        if player > 110:
                            player = 110

                    if pum7 == 5:
                        if player > 109:
                            player = 109

                    if pum7 == 6:
                        if player > 108:
                            player = 108

                    if pum7 == 7:
                        if player > 107:
                            player = 107

                    if pum7 == 8:
                        if player > 106:
                            player = 106

                    if pum7 == 9:
                        if player > 105:
                            player = 105

                    if pum7 == 10:
                        if player > 104:
                            player = 104
                    
                    if pum7 == 11:
                        if player > 103:
                            player = 103

                    if pum7 == 12:
                        if player > 102:
                            player = 102

                    if pum7 == 13:
                        if player > 101:
                            player = 101

                    if pum7 == 14:
                        if player > 100:
                            player = 100

            if pum2 == pum3:
                if pum3 == pum4:
                    if pum3 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum3 == 3:
                        if player > 111:
                            player = 111
                            
                    if pum3 == 4:
                        if player > 110:
                            player = 110

                    if pum3 == 5:
                        if player > 109:
                            player = 109

                    if pum3 == 6:
                        if player > 108:
                            player = 108
                    
                    if pum3 == 7:
                        if player > 107:
                            player = 107

                    if pum3 == 8:
                        if player > 106:
                            player = 106

                    if pum3 == 9:
                        if player > 105:
                            player = 105
                    
                    if pum3 == 10:
                        if player > 104:
                            player = 104

                    if pum3 == 11:
                        if player > 103:
                            player = 103

                    if pum3 == 12:
                        if player > 102:
                            player = 102

                    if pum3 == 13:
                        if player > 101:
                            player = 101

                    if pum3 == 14:
                        if player > 100:
                            player = 100

                if pum4 == pum5:
                    if pum5 == 2:
                        if player > 112:
                            player = 112

                    if pum5 == 3:
                        if player > 111:
                            player = 111

                    if pum5 == 4:
                        if player > 110:
                            player = 110
                    
                    if pum5 == 5:
                        if player > 109:
                            player = 109
                    
                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106

                    if pum5 == 9:
                        if player > 105:
                            player = 105

                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum5 == 3:
                        if player > 111:
                            player = 111

                    if pum5 == 4:
                        if player > 110:
                            player = 110

                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106
                    
                    if pum5 == 9:
                        if player > 105:
                            player = 105

                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101
                    
                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum7 == 3:
                        if player > 111:
                            player = 111

                    if pum7 == 4:
                        if player > 110:
                            player = 110

                    if pum7 == 5:
                        if player > 109:
                            player = 109

                    if pum7 == 6:
                        if player > 108:
                            player = 108

                    if pum7 == 7:
                        if player > 107:
                            player = 107
                    
                    if pum7 == 8:
                        if player > 106:
                            player = 106
                    
                    if pum7 == 9:
                        if player > 105:
                            player = 105

                    if pum7 == 10:
                        if player > 104:
                            player = 104

                    if pum7 == 11:
                        if player > 103:
                            player = 103

                    if pum7 == 12:
                        if player > 102:
                            player = 102

                    if pum7 == 13:
                        if player > 101:
                            player = 101

                    if pum7 == 14:
                        if player > 100:
                            player = 100

            if pum3 == pum4:
                if pum4 == pum5:
                    if pum5 == 2:
                        if player > 112:
                            player = 112
                
                    if pum5 == 3:
                        if player > 111:
                            player = 111
                            
                    if pum5 == 4:
                        if player > 110:
                            player = 110

                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106

                    if pum5 == 9:
                        if player > 105:
                            player = 105

                    if pum5 == 10:
                        if player > 104:
                            player = 104
                    
                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if player > 112:
                            player = 112

                    if pum5 == 3:
                        if player > 111:
                            player = 111

                    if pum5 == 4:
                        if player > 110:
                            player = 110

                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106

                    if pum5 == 9:
                        if player > 105:
                            player = 105
                    
                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum7 == 3:
                        if player > 111:
                            player = 111
                    
                    if pum7 == 4:
                        if player > 110:
                            player = 110

                    if pum7 == 5:
                        if player > 109:
                            player = 109

                    if pum7 == 6:
                        if player > 108:
                            player = 108

                    if pum7 == 7:
                        if player > 107:
                            player = 107

                    if pum7 == 8:
                        if player > 106:
                            player = 106

                    if pum7 == 9:
                        if player > 105:
                            player = 105

                    if pum7 == 10:
                        if player > 104:
                            player = 104
                    
                    if pum7 == 11:
                        if player > 103:
                            player = 103

                    if pum7 == 12:
                        if player > 102:
                            player = 102
                    
                    if pum7 == 13:
                        if player > 101:
                            player = 101

                    if pum7 == 14:
                        if player > 100:
                            player = 100

            if pum4 == pum5:
                if pum5 == pum6:
                    if pum5 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum5 == 3:
                        if player > 111:
                            player = 111
                    
                    if pum5 == 4:
                        if player > 110:
                            player = 110
                            
                    if pum5 == 5:
                        if player > 109:
                            player = 109

                    if pum5 == 6:
                        if player > 108:
                            player = 108

                    if pum5 == 7:
                        if player > 107:
                            player = 107

                    if pum5 == 8:
                        if player > 106:
                            player = 106

                    if pum5 == 9:
                        if player > 105:
                            player = 105
                    
                    if pum5 == 10:
                        if player > 104:
                            player = 104

                    if pum5 == 11:
                        if player > 103:
                            player = 103

                    if pum5 == 12:
                        if player > 102:
                            player = 102

                    if pum5 == 13:
                        if player > 101:
                            player = 101

                    if pum5 == 14:
                        if player > 100:
                            player = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if player > 112:
                            player = 112
                    
                    if pum7 == 3:
                        if player > 111:
                            player = 111
                    
                    if pum7 == 4:
                        if player > 110:
                            player = 110

                    if pum7 == 5:
                        if player > 109:
                            player = 109

                    if pum7 == 6:
                        if player > 108:
                            player = 108
                    
                    if pum7 == 7:
                        if player > 107:
                            player = 107

                    if pum7 == 8:
                        if player > 106:
                            player = 106

                    if pum7 == 9:
                        if player > 105:
                            player = 105

                    if pum7 == 10:
                        if player > 104:
                            player = 104

                    if pum7 == 11:
                        if player > 103:
                            player = 103

                    if pum7 == 12:
                        if player > 102:
                            player = 102

                    if pum7 == 13:
                        if player > 101:
                            player = 101

                    if pum7 == 14:
                        if player > 100:
                            player = 100

            if pum5 == pum6:
                if pum6 == pum7:
                    if pum7 == 2:
                        if player > 112:
                            player = 112
                
                    if pum7 == 3:
                        if player > 111:
                            player = 111
                            
                    if pum7 == 4:
                        if player > 110:
                            player = 110

                    if pum7 == 5:
                        if player > 109:
                            player = 109

                    if pum7 == 6:
                        if player > 108:
                            player = 108

                    if pum7 == 7:
                        if player > 107:
                            player = 107

                    if pum7 == 8:
                        if player > 106:
                            player = 106

                    if pum7 == 9:
                        if player > 105:
                            player = 105

                    if pum7 == 10:
                        if player > 104:
                            player = 104

                    if pum7 == 11:
                        if player > 103:
                            player = 103
                    
                    if pum7 == 12:
                        if player > 102:
                            player = 102

                    if pum7 == 13:
                        if player > 101:
                            player = 101

                    if pum7 == 14:
                        if player > 100:
                            player = 100



            if pum1 == pum2:
                if pum2 == 2:
                    if player > 127:
                        player = 127
                
                if pum2 == 3:
                    if player > 126:
                        player = 126

                if pum2 == 4:
                    if player > 125:
                        player = 125
                
                if pum2 == 5:
                    if player > 124:
                        player = 124

                if pum2 == 6:
                    if player > 123:
                        player = 123

                if pum2 == 7:
                    if player > 122:
                        player = 122
                
                if pum2 == 8:
                    if player > 121:
                        player = 121
                
                if pum2 == 9:
                    if player > 120:
                        player = 120

                if pum2 == 10:
                    if player > 119:
                        player = 119

                if pum2 == 11:
                    if player > 118:
                        player = 118

                if pum2 == 12:
                    if player > 117:
                        player = 117

                if pum2 == 13:
                    if player > 116:
                        player = 116

                if pum2 == 14:
                    if player > 115:
                        player = 115

            if pum2 == pum3:
                if pum2 == 2:
                    if player > 127:
                        player = 127
                
                if pum2 == 3:
                    if player > 126:
                        player = 126

                if pum2 == 4:
                    if player > 125:
                        player = 125

                if pum2 == 5:
                    if player > 124:
                        player = 124

                if pum2 == 6:
                    if player > 123:
                        player = 123
                
                if pum2 == 7:
                    if player > 122:
                        player = 122

                if pum2 == 8:
                    if player > 121:
                        player = 121

                if pum2 == 9:
                    if player > 120:
                        player = 120

                if pum2 == 10:
                    if player > 119:
                        player = 119

                if pum2 == 11:
                    if player > 118:
                        player = 118

                if pum2 == 12:
                    if player > 117:
                        player = 117

                if pum2 == 13:
                    if player > 116:
                        player = 116

                if pum2 == 14:
                    if player > 115:
                        player = 115

            if pum3 == pum4:
                if pum4 == 2:
                    if player > 127:
                        player = 127

                if pum4 == 3:
                    if player > 126:
                        player = 126
                
                if pum4 == 4:
                    if player > 125:
                        player = 125

                if pum4 == 5:
                    if player > 124:
                        player = 124

                if pum4 == 6:
                    if player > 123:
                        player = 123

                if pum4 == 7:
                    if player > 122:
                        player = 122

                if pum4 == 8:
                    if player > 121:
                        player = 121

                if pum4 == 9:
                    if player > 120:
                        player = 120

                if pum4 == 10:
                    if player > 119:
                        player = 119

                if pum4 == 11:
                    if player > 118:
                        player = 118

                if pum4 == 12:
                    if player > 117:
                        player = 117

                if pum4 == 13:
                    if player > 116:
                        player = 116

                if pum4 == 14:
                    if player > 115:
                        player = 115

            if pum4 == pum5:
                if pum4 == 2:
                    if player > 127:
                        player = 127
                
                if pum4 == 3:
                    if player > 126:
                        player = 126

                if pum4 == 4:
                    if player > 125:
                        player = 125

                if pum4 == 5:
                    if player > 124:
                        player = 124

                if pum4 == 6:
                    if player > 123:
                        player = 123

                if pum4 == 7:
                    if player > 122:
                        player = 122

                if pum4 == 8:
                    if player > 121:
                        player = 121
                
                if pum4 == 9:
                    if player > 120:
                        player = 120

                if pum4 == 10:
                    if player > 119:
                        player = 119

                if pum4 == 11:
                    if player > 118:
                        player = 118

                if pum4 == 12:
                    if player > 117:
                        player = 117

                if pum4 == 13:
                    if player > 116:
                        player = 116

                if pum4 == 14:
                    if player > 115:
                        player = 115

            if pum6 == pum7:
                if pum7 == 2:
                    if player > 127:
                        player = 127

                if pum7 == 3:
                    if player > 126:
                        player = 126

                if pum7 == 4:
                    if player > 125:
                        player = 125

                if pum7 == 5:
                    if player > 124:
                        player = 124

                if pum7 == 6:
                    if player > 123:
                        player = 123

                if pum7 == 7:
                    if player > 122:
                        player = 122

                if pum7 == 8:
                    if player > 121:
                        player = 121

                if pum7 == 9:
                    if player > 120:
                        player = 120

                if pum7 == 10:
                    if player > 119:
                        player = 119

                if pum7 == 11:
                    if player > 118:
                        player = 118
                
                if pum7 == 12:
                    if player > 117:
                        player = 117

                if pum7 == 13:
                    if player > 116:
                        player = 116

                if pum7 == 14:
                    if player > 115:
                        player = 115



            print ("나의 족보")
            print ()

            if 0 < player:
                if player <= 4:
                    print ("!!!! royal straight flush !!!! (0.000153907%)")

            if 6 <= player:
                if player <= 17:
                    print ("!!! straight flush !!! (0.001385169%)")

            if 20 <= player:
                if player <= 32:
                    print ("!! four of a kind !! (0.024009603%)")

            if 35 <= player:
                if player <= 47:
                    print ("! full house ! (0.144057623%)")

            if 50 <=  player:
                if player <= 62:
                    print ("$$$$ flush $$$$ (0.196540154%)")

            if 70 == player:
                print ("$$$ straight $$$ (0.392464678%)")

            if 80 <= player:
                if player <= 92:
                    print ("$$ three of a kind $$ (2.112845138%)")

            if 100 <= player:
                if player <= 112:
                    print ("$ two pair $ (4.75390156%)")

            if 115 <= player:
                if player <= 127:
                    print ("$ one pair $ (42.256902761%)")

            if 128 <= player:
                print (" high card (no pair) (50.117739403%)")
            print()
            print()

            ppat1 = 0
            ppat2 = 0
            ppat3 = 0
            ppat4 = 0

            eplag1 = 0
            eplag2 = 0
            eplag3 = 0
            eplag4 = 0

            pnum1 = 0
            pnum2 = 0
            pnum3 = 0
            pnum4 = 0
            pnum5 = 0
            pnum6 = 0
            pnum7 = 0

            ppn1 = 0
            ppn2 = 0
            ppn3 = 0
            ppn4 = 0
            ppn5 = 0
            ppn6 = 0
            ppn7 = 0

            a = 0

            computer = 100000

            if ccdn1 == 1:
                ccdn1 = 14
            if ccdn2 == 1:
                ccdn2 = 14
            if ccdn3 == 1:
                ccdn3 = 14
            if ccdn4 == 1:
                ccdn4 = 14
            if ccdn5 == 1:
                ccdn5 = 14
            if ccdn6 == 1:
                ccdn6 = 14
            if ccdn7 == 1:
                ccdn7 = 14

            lists = [ccd1, ccd2, ccd3, ccd4, ccd5, ccd6, ccd7]

            a = 0

            for lst in lists:
                if lst == 4:
                    ppat1 = ppat1 + 1
                if lst == 3:
                    ppat2 = ppat2 + 1
                if lst == 2:
                    ppat3 = ppat3 + 1
                if lst == 1:
                    ppat4 = ppat4 + 1

            if ppat1 >= 5:
                if ccd1 == 4:
                    if ccdn1 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn1 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn1 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn1 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn1 == 10:
                        eplag1 = eplag1 + 1
                if ccd2 == 4:
                    if ccdn2 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn2 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn2 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn2 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn2 == 10:
                        eplag1 = eplag1 + 1
                if ccd3 == 4:
                    if ccdn3 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn3 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn3 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn3 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn3 == 10:
                        eplag1 = eplag1 + 1
                if ccd4 == 4:
                    if ccdn4 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn4 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn4 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn4 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn4 == 10:
                        eplag1 = eplag1 + 1
                if ccd5 == 4:
                    if ccdn5 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn5 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn5 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn5 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn5 == 10:
                        eplag1 = eplag1 + 1
                if ccd6 == 4:
                    if ccdn6 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn6 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn6 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn6 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn6 == 10:
                        eplag1 = eplag1 + 1
                if ccd7 == 4:
                    if ccdn7 == 14:
                        eplag1 = eplag1 + 1
                    if ccdn7 == 13:
                        eplag1 = eplag1 + 1
                    if ccdn7 == 12:
                        eplag1 = eplag1 + 1
                    if ccdn7 == 11:
                        eplag1 = eplag1 + 1
                    if ccdn7 == 10:
                        eplag1 = eplag1 + 1
            if ppat2 >= 5:
                if ccd1 == 3:
                    if ccdn1 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn1 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn1 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn1 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn1 == 10:
                        eplag2 = eplag2 + 1
                if ccd2 == 3:
                    if ccdn2 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn2 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn2 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn2 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn2 == 10:
                        eplag2 = eplag2 + 1
                if ccd3 == 3:
                    if ccdn3 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn3 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn3 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn3 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn3 == 10:
                        eplag2 = eplag2 + 1
                if ccd4 == 3:
                    if ccdn4 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn4 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn4 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn4 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn4 == 10:
                        eplag2 = eplag2 + 1
                if ccd5 == 3:
                    if ccdn5 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn5 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn5 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn5 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn5 == 10:
                        eplag2 = eplag2 + 1
                if ccd6 == 3:
                    if ccdn6 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn6 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn6 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn6 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn6 == 10:
                        eplag2 = eplag2 + 1
                if ccd7 == 3:
                    if ccdn7 == 14:
                        eplag2 = eplag2 + 1
                    if ccdn7 == 13:
                        eplag2 = eplag2 + 1
                    if ccdn7 == 12:
                        eplag2 = eplag2 + 1
                    if ccdn7 == 11:
                        eplag2 = eplag2 + 1
                    if ccdn7 == 10:
                        eplag2 = eplag2 + 1
            if ppat3 >= 5:
                if ccd1 == 2:
                    if ccdn1 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn1 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn1 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn1 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn1 == 10:
                        eplag3 = eplag3 + 1
                if ccd2 == 2:
                    if ccdn2 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn2 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn2 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn2 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn2 == 10:
                        eplag3 = eplag3 + 1
                if ccd3 == 2:
                    if ccdn3 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn3 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn3 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn3 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn3 == 10:
                        eplag3 = eplag3 + 1
                if ccd4 == 2:
                    if ccdn4 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn4 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn4 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn4 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn4 == 10:
                        eplag3 = eplag3 + 1
                if ccd5 == 2:
                    if ccdn5 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn5 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn5 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn5 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn5 == 10:
                        eplag3 = eplag3 + 1
                if ccd6 == 2:
                    if ccdn6 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn6 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn6 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn6 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn6 == 10:
                        eplag3 = eplag3 + 1
                if ccd7 == 2:
                    if ccdn7 == 14:
                        eplag3 = eplag3 + 1
                    if ccdn7 == 13:
                        eplag3 = eplag3 + 1
                    if ccdn7 == 12:
                        eplag3 = eplag3 + 1
                    if ccdn7 == 11:
                        eplag3 = eplag3 + 1
                    if ccdn7 == 10:
                        eplag3 = eplag3 + 1
            if ppat4 >= 5:
                if ccd1 == 1:
                    if ccdn1 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn1 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn1 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn1 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn1 == 10:
                        eplag4 = eplag4 + 1
                if ccd2 == 1:
                    if ccdn2 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn2 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn2 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn2 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn2 == 10:
                        eplag4 = eplag4 + 1
                if ccd3 == 1:
                    if ccdn3 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn3 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn3 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn3 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn3 == 10:
                        eplag4 = eplag4 + 1
                if ccd4 == 1:
                    if ccdn4 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn4 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn4 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn4 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn4 == 10:
                        eplag4 = eplag4 + 1
                if ccd5 == 1:
                    if ccdn5 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn5 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn5 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn5 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn5 == 10:
                        eplag4 = eplag4 + 1
                if ccd6 == 1:
                    if ccdn6 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn6 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn6 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn6 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn6 == 10:
                        eplag4 = eplag4 + 1
                if ccd7 == 1:
                    if ccdn7 == 14:
                        eplag4 = eplag4 + 1
                    if ccdn7 == 13:
                        eplag4 = eplag4 + 1
                    if ccdn7 == 12:
                        eplag4 = eplag4 + 1
                    if ccdn7 == 11:
                        eplag4 = eplag4 + 1
                    if ccdn7 == 10:
                        eplag4 = eplag4 + 1
            if eplag1 >= 5:
                if computer > 1:
                    computer = 1
            if eplag2 >= 5:
                if computer > 2:
                    computer = 2
            if eplag3 >= 5:
                if computer > 3:
                    computer = 3
            if eplag4 >= 5:
                if computer > 4:
                    computer = 4

            plists = [ccd1, ccd2, ccd3, ccd4, ccd5, ccd6, ccd7]

            plists.sort(reverse=True)

            a = 0

            for b in plists:
                a = a + 1
                if a == 1:
                    ppet1 = b
                if a == 2:
                    ppet2 = b
                if a == 3:
                    ppet3 = b
                if a == 4:
                    ppet4 = b
                if a == 5:
                    ppet5 = b
                if a == 6:
                    ppet6 = b
                if a == 7:
                    ppet7 = b

            if ppet1 == ppet2 == ppet3 == ppet4 == ppet5:
                if ppet1 == ccd1:
                    ppn1 = ccdn1
                if ppet1 == ccd2:
                    ppn2 = ccdn2
                if ppet1 == ccd3:
                    ppn3 = ccdn3
                if ppet1 == ccd4:
                    ppn4 = ccdn4
                if ppet1 == ccd5:
                    ppn5 = ccdn5
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd7:
                    ppn7 = ccdn7
            if ppet2 == ppet3 == ppet4 == ppet5 == ppet6:
                if ppet2 == ccd1:
                    ppn1 = ccdn1
                if ppet2 == ccd2:
                    ppn2 = ccdn2
                if ppet2 == ccd3:
                    ppn3 = ccdn3
                if ppet2 == ccd4:
                    ppn4 = ccdn4
                if ppet2 == ccd5:
                    ppn5 = ccdn5
                if ppet2 == ccd6:
                    ppn6 = ccdn6
                if ppet2 == ccd6:
                    ppn6 = ccdn6
                if ppet2 == ccd7:
                    ppn7 = ccdn7
            if ppet3 == ppet4 == ppet5 == ppet6 == ppet7:
                if ppet3 == ccd1:
                    ppn1 = ccdn1
                if ppet3 == ccd2:
                    ppn2 = ccdn2
                if ppet3 == ccd3:
                    ppn3 = ccdn3
                if ppet3 == ccd4:
                    ppn4 = ccdn4
                if ppet3 == ccd5:
                    ppn5 = ccdn5
                if ppet3 == ccd6:
                    ppn6 = ccdn6
                if ppet3 == ccd6:
                    ppn6 = ccdn6
                if ppet3 == ccd7:
                    ppn7 = ccdn7


            a = 0

            pnum = [ppn1, ppn2, ppn3, ppn4, ppn5, ppn6, ppn7]

            pnum.sort(reverse=True)

            for b in pnum:
                a = a + 1
                if a == 1:
                    pum1 = b
                if a == 2:
                    pum2 = b
                if a == 3:
                    pum3 = b
                if a == 4:
                    pum4 = b
                if a == 5:
                    pum5 = b
                if a == 6:
                    pum6 = b
                if a == 7:
                    pum7 = b

            if pum1 == 14:
                if pum2 == 5:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if computer > 6:
                                    computer = 6

            if pum1 == 6:
                if pum2 == 5:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if computer > 7:
                                    computer = 17

            if pum1 == 7:
                if pum2 == 6:
                    if pum3 == 5:
                        if pum4 == 4:
                            if pum5 == 3:
                                if computer > 8:
                                    computer = 16

            if pum1 == 8:
                if pum2 == 7:
                    if pum3 == 6:
                        if pum4 == 5:
                            if pum5 == 4:
                                if computer > 9:
                                    computer = 15

            if pum1 == 9:
                if pum2 == 8:
                    if pum3 == 7:
                        if pum4 == 6:
                            if pum5 == 5:
                                if computer > 10:
                                    computer = 14

            if pum1 == 10:
                if pum2 == 9:
                    if pum3 == 8:
                        if pum4 == 7:
                            if pum5 == 6:
                                if computer > 11:
                                    computer = 13

            if pum1 == 11:
                if pum2 == 10:
                    if pum3 == 9:
                        if pum4 == 8:
                            if pum5 == 7:
                                if computer > 12:
                                    computer = 12

            if pum1 == 12:
                if pum2 == 11:
                    if pum3 == 10:
                        if pum4 == 9:
                            if pum5 == 8:
                                if computer > 13:
                                    computer = 11

            if pum1 == 13:
                if pum2 == 12:
                    if pum3 == 11:
                        if pum4 == 10:
                            if pum5 == 9:
                                if computer > 14:
                                    computer = 10

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 12:
                        if pum4 == 11:
                            if pum5 == 2:
                                if computer > 15:
                                    computer = 9

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 12:
                        if pum4 == 3:
                            if pum5 == 2:
                                if computer > 16:
                                    computer = 8

            if pum1 == 14:
                if pum2 == 13:
                    if pum3 == 4:
                        if pum4 == 3:
                            if pum5 == 2:
                                if computer > 17:
                                    computer = 7

            a = 0

            pnum1 = [ccdn1, ccdn2, ccdn3, ccdn4, ccdn5, ccdn6, ccdn7]

            pnum1.sort(reverse=True)

            for b in pnum1:
                a = a + 1
                if a == 1:
                    pum1 = b
                if a == 2:
                    pum2 = b
                if a == 3:
                    pum3 = b
                if a == 4:
                    pum4 = b
                if a == 5:
                    pum5 = b
                if a == 6:
                    pum6 = b
                if a == 7:
                    pum7 = b

            if pum1 == pum2 == pum3 == pum4:
                if pum4 == 14:
                    if computer > 20:
                        computer = 20
                if pum4 == 2:
                    if computer > 32:
                        computer = 32
                if pum4 == 3:
                    if computer > 31:
                        computer = 31
                if pum4 == 4:
                    if computer > 30:
                        computer = 30
                if pum4 == 5:
                    if computer > 29:
                        computer = 29
                if pum4 == 6:
                    if computer > 28:
                        computer = 28
                if pum4 == 7:
                    if computer > 27:
                        computer = 27
                if pum4 == 8:
                    if computer > 26:
                        computer = 26
                if pum4 == 9:
                    if computer > 25:
                        computer = 25
                if pum4 == 10:
                    if computer > 24:
                        computer = 24
                if pum4 == 11:
                    if computer > 23:
                        computer = 23
                if pum4 == 12:
                    if computer > 22:
                        computer = 22
                if pum4 == 13:
                    if computer > 21:
                        computer = 21

            if pum2 == pum3 == pum4 == pum5:
                if pum4 == 14:
                    if computer > 20:
                        computer = 20
                if pum4 == 2:
                    if computer > 32:
                        computer = 32
                if pum4 == 3:
                    if computer > 31:
                        computer = 31
                if pum4 == 4:
                    if computer > 30:
                        computer = 30
                if pum4 == 5:
                    if computer > 29:
                        computer = 29
                if pum4 == 6:
                    if computer > 28:
                        computer = 28
                if pum4 == 7:
                    if computer > 27:
                        computer = 27
                if pum4 == 8:
                    if computer > 26:
                        computer = 26
                if pum4 == 9:
                    if computer > 25:
                        computer = 25
                if pum4 == 10:
                    if computer > 24:
                        computer = 24
                if pum4 == 11:
                    if computer > 23:
                        computer = 23
                if pum4 == 12:
                    if computer > 22:
                        computer = 22
                if pum4 == 13:
                    if computer > 21:
                        computer = 21

            if pum3 == pum4 == pum5 == pum6:
                if pum4 == 14:
                    if computer > 20:
                        computer = 20
                if pum4 == 2:
                    if computer > 32:
                        computer = 32
                if pum4 == 3:
                    if computer > 31:
                        computer = 31
                if pum4 == 4:
                    if computer > 30:
                        computer = 30
                if pum4 == 5:
                    if computer > 29:
                        computer = 29
                if pum4 == 6:
                    if computer > 28:
                        computer = 28
                if pum4 == 7:
                    if computer > 27:
                        computer = 27
                if pum4 == 8:
                    if computer > 26:
                        computer = 26
                if pum4 == 9:
                    if computer > 25:
                        computer = 25
                if pum4 == 10:
                    if computer > 24:
                        computer = 24
                if pum4 == 11:
                    if computer > 23:
                        computer = 23
                if pum4 == 12:
                    if computer > 22:
                        computer = 22
                if pum4 == 13:
                    if computer > 21:
                        computer = 21

            if pum4 == pum5 == pum6 == pum7:
                if pum4 == 14:
                    if computer > 20:
                        computer = 20
                if pum4 == 2:
                    if computer > 32:
                        computer = 32
                if pum4 == 3:
                    if computer > 31:
                        computer = 31
                if pum4 == 4:
                    if computer > 30:
                        computer = 30
                if pum4 == 5:
                    if computer > 29:
                        computer = 29
                if pum4 == 6:
                    if computer > 28:
                        computer = 28
                if pum4 == 7:
                    if computer > 27:
                        computer = 27
                if pum4 == 8:
                    if computer > 26:
                        computer = 26
                if pum4 == 9:
                    if computer > 25:
                        computer = 25
                if pum4 == 10:
                    if computer > 24:
                        computer = 24
                if pum4 == 11:
                    if computer > 23:
                        computer = 23
                if pum4 == 12:
                    if computer > 22:
                        computer = 22
                if pum4 == 13:
                    if computer > 21:
                        computer = 21

            if pum1 == pum2:
                if pum3 == pum4 == pum5:
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum1 == pum2 == pum3:
                if pum4 == pum5:
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum1 == pum2:
                if pum4 == pum5 == pum6:
                    if pum4 == 14:
                        if computer > 35:
                            computer = 35
                    if pum4 == 2:
                        if computer > 47:
                            computer = 47
                    if pum4 == 3:
                        if computer > 46:
                            computer = 46
                    if pum4 == 4:
                        if computer > 45:
                            computer = 45
                    if pum4 == 5:
                        if computer > 44:
                            computer = 44
                    if pum4 == 6:
                        if computer > 43:
                            computer = 43
                    if pum4 == 7:
                        if computer > 42:
                           computer = 42
                    if pum4 == 8:
                        if computer > 41:
                            computer = 41
                    if pum4 == 9:
                        if computer > 40:
                            computer = 40
                    if pum4 == 10:
                        if computer > 39:
                            computer = 39
                    if pum4 == 11:
                        if computer > 38:
                            computer = 38
                    if pum4 == 12:
                        if computer > 37:
                            computer = 37
                    if pum4 == 13:
                        if computer > 36:
                            computer = 36

            if pum2 == pum3 == pum4:
                if pum5 == pum6:
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum2 == pum3:
                if pum4 == pum5 == pum6:
                    if pum4 == 14:
                        if computer > 35:
                            computer = 35
                    if pum4 == 2:
                        if computer > 47:
                            computer = 47
                    if pum4 == 3:
                        if computer > 46:
                            computer = 46
                    if pum4 == 4:
                        if computer > 45:
                            computer = 45
                    if pum4 == 5:
                        if computer > 44:
                            computer = 44
                    if pum4 == 6:
                        if computer > 43:
                            computer = 43
                    if pum4 == 7:
                        if computer > 42:
                           computer = 42
                    if pum4 == 8:
                        if computer > 41:
                            computer = 41
                    if pum4 == 9:
                        if computer > 40:
                            computer = 40
                    if pum4 == 10:
                        if computer > 39:
                            computer = 39
                    if pum4 == 11:
                        if computer > 38:
                            computer = 38
                    if pum4 == 12:
                        if computer > 37:
                            computer = 37
                    if pum4 == 13:
                        if computer > 36:
                            computer = 36

            if pum1 == pum2 == pum3:
                if pum6 == pum7:
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum1 == pum2 == pum3:
                if pum5 == pum6 :
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum1 == pum2:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if computer > 35:
                            computer = 35
                    if pum5 == 2:
                        if computer > 47:
                            computer = 47
                    if pum5 == 3:
                        if computer > 46:
                            computer = 46
                    if pum5 == 4:
                        if computer > 45:
                            computer = 45
                    if pum5 == 5:
                        if computer > 44:
                            computer = 44
                    if pum5 == 6:
                        if computer > 43:
                            computer = 43
                    if pum5 == 7:
                        if computer > 42:
                           computer = 42
                    if pum5 == 8:
                        if computer > 41:
                            computer = 41
                    if pum5 == 9:
                        if computer > 40:
                            computer = 40
                    if pum5 == 10:
                        if computer > 39:
                            computer = 39
                    if pum5 == 11:
                        if computer > 38:
                            computer = 38
                    if pum5 == 12:
                        if computer > 37:
                            computer = 37
                    if pum5 == 13:
                        if computer > 36:
                            computer = 36

            if pum2 == pum3 == pum4:
                if pum6 == pum7:
                    if pum3 == 14:
                        if computer > 35:
                            computer = 35
                    if pum3 == 2:
                        if computer > 47:
                            computer = 47
                    if pum3 == 3:
                        if computer > 46:
                            computer = 46
                    if pum3 == 4:
                        if computer > 45:
                            computer = 45
                    if pum3 == 5:
                        if computer > 44:
                            computer = 44
                    if pum3 == 6:
                        if computer > 43:
                            computer = 43
                    if pum3 == 7:
                        if computer > 42:
                           computer = 42
                    if pum3 == 8:
                        if computer > 41:
                            computer = 41
                    if pum3 == 9:
                        if computer > 40:
                            computer = 40
                    if pum3 == 10:
                        if computer > 39:
                            computer = 39
                    if pum3 == 11:
                        if computer > 38:
                            computer = 38
                    if pum3 == 12:
                        if computer > 37:
                            computer = 37
                    if pum3 == 13:
                        if computer > 36:
                            computer = 36

            if pum2 == pum3:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if computer > 35:
                            computer = 35
                    if pum5 == 2:
                        if computer > 47:
                            computer = 47
                    if pum5 == 3:
                        if computer > 46:
                            computer = 46
                    if pum5 == 4:
                        if computer > 45:
                            computer = 45
                    if pum5 == 5:
                        if computer > 44:
                            computer = 44
                    if pum5 == 6:
                        if computer > 43:
                            computer = 43
                    if pum5 == 7:
                        if computer > 42:
                           computer = 42
                    if pum5 == 8:
                        if computer > 41:
                            computer = 41
                    if pum5 == 9:
                        if computer > 40:
                            computer = 40
                    if pum5 == 10:
                        if computer > 39:
                            computer = 39
                    if pum5 == 11:
                        if computer > 38:
                            computer = 38
                    if pum5 == 12:
                        if computer > 37:
                            computer = 37
                    if pum5 == 13:
                        if computer > 36:
                            computer = 36

            if pum3 == pum4:
                if pum5 == pum6 == pum7:
                    if pum5 == 14:
                        if computer > 35:
                            computer = 35
                    if pum5 == 2:
                        if computer > 47:
                            computer = 47
                    if pum5 == 3:
                        if computer > 46:
                            computer = 46
                    if pum5 == 4:
                        if computer > 45:
                            computer = 45
                    if pum5 == 5:
                        if computer > 44:
                            computer = 44
                    if pum5 == 6:
                        if computer > 43:
                            computer = 43
                    if pum5 == 7:
                        if computer > 42:
                           computer = 42
                    if pum5 == 8:
                        if computer > 41:
                            computer = 41
                    if pum5 == 9:
                        if computer > 40:
                            computer = 40
                    if pum5 == 10:
                        if computer > 39:
                            computer = 39
                    if pum5 == 11:
                        if computer > 38:
                            computer = 38
                    if pum5 == 12:
                        if computer > 37:
                            computer = 37
                    if pum5 == 13:
                        if computer > 36:
                            computer = 36

            if ppet1 == ppet2 == ppet3 == ppet4 == ppet5:
                if ppet1 == ccd1:
                    ppn1 = ccdn1
                if ppet1 == ccd2:
                    ppn2 = ccdn2
                if ppet1 == ccd3:
                    ppn3 = ccdn3
                if ppet1 == ccd4:
                    ppn4 = ccdn4
                if ppet1 == ccd5:
                    ppn5 = ccdn5
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd7:
                    ppn7 = ccdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if computer > 50:
                        computer = 50
                if pum5 == 2:
                    if computer > 62:
                        computer = 62
                if pum5 == 3:
                    if computer > 61:
                        computer = 61
                if pum5 == 4:
                    if computer > 60:
                        computer = 60
                if pum5 == 5:
                    if computer > 59:
                        computer = 59
                if pum5 == 6:
                    if computer > 58:
                        computer = 58
                if pum5 == 7:
                    if computer > 57:
                        computer = 57
                if pum5 == 8:
                    if computer > 56:
                        computer = 56
                if pum5 == 9:
                    if computer > 55:
                        computer = 55
                if pum5 == 10:
                    if computer > 54:
                        computer = 54
                if pum5 == 11:
                    if computer > 53:
                        computer = 53
                if pum5 == 12:
                    if computer > 52:
                        computer = 52
                if pum5 == 13:
                    if computer > 51:
                        computer = 51

            if ppet2 == ppet3 == ppet4 == ppet5 == ppet6:
                if ppet1 == ccd1:
                    ppn1 = ccdn1
                if ppet1 == ccd2:
                    ppn2 = ccdn2
                if ppet1 == ccd3:
                    ppn3 = ccdn3
                if ppet1 == ccd4:
                    ppn4 = ccdn4
                if ppet1 == ccd5:
                    ppn5 = ccdn5
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd7:
                    ppn7 = ccdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if computer > 50:
                        computer = 50
                if pum5 == 2:
                    if computer > 62:
                        computer = 62
                if pum5 == 3:
                    if computer > 61:
                        computer = 61
                if pum5 == 4:
                    if computer > 60:
                        computer = 60
                if pum5 == 5:
                    if computer > 59:
                        computer = 59
                if pum5 == 6:
                    if computer > 58:
                        computer = 58
                if pum5 == 7:
                    if computer > 57:
                        computer = 57
                if pum5 == 8:
                    if computer > 56:
                        computer = 56
                if pum5 == 9:
                    if computer > 55:
                        computer = 55
                if pum5 == 10:
                    if computer > 54:
                        computer = 54
                if pum5 == 11:
                    if computer > 53:
                        computer = 53
                if pum5 == 12:
                    if computer > 52:
                        computer = 52
                if pum5 == 13:
                    if computer > 51:
                        computer = 51
            if ppet3 == ppet4 == ppet5 == ppet6 == ppet7:
                if ppet1 == ccd1:
                    ppn1 = ccdn1
                if ppet1 == ccd2:
                    ppn2 = ccdn2
                if ppet1 == ccd3:
                    ppn3 = ccdn3
                if ppet1 == ccd4:
                    ppn4 = ccdn4
                if ppet1 == ccd5:
                    ppn5 = ccdn5
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd6:
                    ppn6 = ccdn6
                if ppet1 == ccd7:
                    ppn7 = ccdn7

                if ppn1 > ppn2:
                    ppn = ppn1
                else:
                    ppn = ppn2

                if ppn > ppn3:
                    ppn = ppn
                else:
                    ppn = ppn3

                if ppn > ppn4:
                    ppn = ppn
                else:
                    ppn = ppn4

                if ppn > ppn5:
                    ppn = ppn
                else:
                    ppn = ppn5

                if ppn > ppn6:
                    ppn = ppn
                else:
                    ppn = ppn6

                if ppn > ppn7:
                    ppn = ppn
                else:
                    ppn = ppn7

                if pum5 == 14:
                    if computer > 50:
                        computer = 50
                if pum5 == 2:
                    if computer > 62:
                        computer = 62
                if pum5 == 3:
                    if computer > 61:
                        computer = 61
                if pum5 == 4:
                    if computer > 60:
                        computer = 60
                if pum5 == 5:
                    if computer > 59:
                        computer = 59
                if pum5 == 6:
                    if computer > 58:
                        computer = 58
                if pum5 == 7:
                    if computer > 57:
                        computer = 57
                if pum5 == 8:
                    if computer > 56:
                        computer = 56
                if pum5 == 9:
                    if computer > 55:
                        computer = 55
                if pum5 == 10:
                    if computer > 54:
                        computer = 54
                if pum5 == 11:
                    if computer > 53:
                        computer = 53
                if pum5 == 12:
                    if computer > 52:
                        computer = 52
                if pum5 == 13:
                    if computer > 51:
                        computer = 51

            plag8 = 0
            pum = 0

            if pum7 + 1 == pum6:
                plag8 = plag8 + 1

            if pum7 + 1 == pum5:
                plag8 = plag8 + 1
            if pum6 + 1 == pum5:
                plag8 = plag8 + 1

            if pum7 + 1 == pum4:
                plag8 = plag8 + 1
            if pum6 + 1 == pum4:
                plag8 = plag8 + 1
            if pum5 + 1 == pum4:
                plag8 = plag8 + 1

            if pum6 + 1 == pum3:
                plag8 = plag8 + 1
            if pum5 + 1 == pum3:
                plag8 = plag8 + 1
            if pum4 + 1 == pum3:
                plag8 = plag8 + 1

            if pum3 + 1 == pum2:
                plag8 = plag8 + 1
            if pum4 + 1 == pum2:
                plag8 = plag8 + 1
            if pum3 + 1 == pum2:
                plag8 = plag8 + 1

            if pum4 + 1 == pum1:
                plag8 = plag8 + 1
            if pum3 + 1 == pum1:
                plag8 = plag8 + 1
            if pum2 + 1 == pum1:
                plag8 = plag8 + 1

            if plag8 == 6:
                computer = 70


            if pum1 == pum2 == pum3:
                if pum3 == 14:
                    if computer > 80:
                        computer = 80
                if pum3 == 2:
                    if computer > 92:
                        computer = 92
                if pum3 == 3:
                    if computer > 91:
                        computer = 91
                if pum3 == 4:
                    if computer > 90:
                        computer = 90
                if pum3 == 5:
                    if computer > 89:
                        computer = 89
                if pum3 == 6:
                    if computer > 88:
                        computer = 88
                if pum3 == 7:
                    if computer > 87:
                        computer = 87
                if pum3 == 8:
                    if computer > 86:
                        computer = 86
                if pum3 == 9:
                    if computer > 85:
                        computer = 85
                if pum3 == 10:
                    if computer > 84:
                        computer = 84
                if pum3 == 11:
                    if computer > 83:
                        computer = 83
                if pum3 == 12:
                    if computer > 82:
                        computer = 82
                if pum3 == 13:
                    if computer > 81:
                        computer = 81
            if pum2 == pum3 == pum4:
                if pum3 == 14:
                    if computer > 80:
                        computer = 80
                if pum3 == 2:
                    if computer > 92:
                        computer = 92
                if pum3 == 3:
                    if computer > 91:
                        computer = 91
                if pum3 == 4:
                    if computer > 90:
                        computer = 90
                if pum3 == 5:
                    if computer > 89:
                        computer = 89
                if pum3 == 6:
                    if computer > 88:
                        computer = 88
                if pum3 == 7:
                    if computer > 87:
                        computer = 87
                if pum3 == 8:
                    if computer > 86:
                        computer = 86
                if pum3 == 9:
                    if computer > 85:
                        computer = 85
                if pum3 == 10:
                    if computer > 84:
                        computer = 84
                if pum3 == 11:
                    if computer > 83:
                        computer = 83
                if pum3 == 12:
                    if computer > 82:
                        computer = 82
                if pum3 == 13:
                    if computer > 81:
                        computer = 81
            if pum3 == pum4 == pum5:
                if pum3 == 14:
                    if computer > 80:
                        computer = 80
                if pum3 == 2:
                    if computer > 92:
                        computer = 92
                if pum3 == 3:
                    if computer > 91:
                        computer = 91
                if pum3 == 4:
                    if computer > 90:
                        computer = 90
                if pum3 == 5:
                    if computer > 89:
                        computer = 89
                if pum3 == 6:
                    if computer > 88:
                        computer = 88
                if pum3 == 7:
                    if computer > 87:
                        computer = 87
                if pum3 == 8:
                    if computer > 86:
                        computer = 86
                if pum3 == 9:
                    if computer > 85:
                        computer = 85
                if pum3 == 10:
                    if computer > 84:
                        computer = 84
                if pum3 == 11:
                    if computer > 83:
                        computer = 83
                if pum3 == 12:
                    if computer > 82:
                        computer = 82
                if pum3 == 13:
                    if computer > 81:
                        computer = 81
            if pum4 == pum5 == pum6:
                if pum3 == 14:
                    if computer > 80:
                        computer = 80
                if pum3 == 2:
                    if computer > 92:
                        computer = 92
                if pum3 == 3:
                    if computer > 91:
                        computer = 91
                if pum3 == 4:
                    if computer > 90:
                        computer = 90
                if pum3 == 5:
                    if computer > 89:
                        computer = 89
                if pum3 == 6:
                    if computer > 88:
                        computer = 88
                if pum3 == 7:
                    if computer > 87:
                        computer = 87
                if pum3 == 8:
                    if computer > 86:
                        computer = 86
                if pum3 == 9:
                    if computer > 85:
                        computer = 85
                if pum3 == 10:
                    if computer > 84:
                        computer = 84
                if pum3 == 11:
                    if computer > 83:
                        computer = 83
                if pum3 == 12:
                    if computer > 82:
                        computer = 82
                if pum3 == 13:
                    if computer > 81:
                        computer = 81
            if pum5 == pum6 == pum7:
                if pum3 == 14:
                    if computer > 80:
                        computer = 80
                if pum3 == 2:
                    if computer > 92:
                        computer = 92
                if pum3 == 3:
                    if computer > 91:
                        computer = 91
                if pum3 == 4:
                    if computer > 90:
                        computer = 90
                if pum3 == 5:
                    if computer > 89:
                        computer = 89
                if pum3 == 6:
                    if computer > 88:
                        computer = 88
                if pum3 == 7:
                    if computer > 87:
                        computer = 87
                if pum3 == 8:
                    if computer > 86:
                        computer = 86
                if pum3 == 9:
                    if computer > 85:
                        computer = 85
                if pum3 == 10:
                    if computer > 84:
                        computer = 84
                if pum3 == 11:
                    if computer > 83:
                        computer = 83
                if pum3 == 12:
                    if computer > 82:
                        computer = 82
                if pum3 == 13:
                    if computer > 81:
                        computer = 81

            plag8 = 0
            plag9 = 0

            if pum1 == pum2:
                if pum2 == pum3:
                    if pum3 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum3 == 3:
                        if computer > 111:
                            computer = 111
                            
                    if pum3 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum3 == 5:
                        if computer > 109:
                            computer = 109

                    if pum3 == 6:
                        if computer > 108:
                            computer = 108

                    if pum3 == 7:
                        if computer > 107:
                            computer = 107

                    if pum3 == 8:
                        if computer > 106:
                            computer = 106

                    if pum3 == 9:
                        if computer > 105:
                            computer = 105

                    if pum3 == 10:
                        if computer > 104:
                            computer = 104

                    if pum3 == 11:
                        if computer > 103:
                            computer = 103
                    
                    if pum3 == 12:
                        if computer > 102:
                            computer = 102

                    if pum3 == 13:
                        if computer > 101:
                            computer = 101

                    if pum3 == 14:
                        if computer > 100:
                            computer = 100

                if pum3 == pum4:
                    if pum3 == 2:
                        if computer > 112:
                            computer = 112

                    if pum3 == 3:
                        if computer > 111:
                            computer = 111

                    if pum3 == 4:
                        if computer > 110:
                            computer = 110

                    if pum3 == 5:
                        if computer > 109:
                            computer = 109

                    if pum3 == 6:
                        if computer > 108:
                            computer = 108

                    if pum3 == 7:
                        if computer > 107:
                            computer = 107
                    
                    if pum3 == 8:
                        if computer > 106:
                            computer = 106

                    if pum3 == 9:
                        if computer > 105:
                            computer = 105

                    if pum3 == 10:
                        if computer > 104:
                            computer = 104

                    if pum3 == 11:
                        if computer > 103:
                            computer = 103

                    if pum3 == 12:
                        if computer > 102:
                            computer = 102

                    if pum3 == 13:
                        if computer > 101:
                            computer = 101

                    if pum3 == 14:
                        if computer > 100:
                            computer = 100

                if pum4 == pum5:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112

                    if pum5 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum5 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105

                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103

                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum5 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum5 == 4:
                        if computer > 110:
                            computer = 110

                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108
                    
                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106
                    
                    if pum5 == 9:
                        if computer > 105:
                            computer = 105

                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103

                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum7 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum7 == 4:
                        if computer > 110:
                            computer = 110

                    if pum7 == 5:
                        if computer > 109:
                            computer = 109

                    if pum7 == 6:
                        if computer > 108:
                            computer = 108

                    if pum7 == 7:
                        if computer > 107:
                            computer = 107

                    if pum7 == 8:
                        if computer > 106:
                            computer = 106

                    if pum7 == 9:
                        if computer > 105:
                            computer = 105
                    
                    if pum7 == 10:
                        if computer > 104:
                            computer = 104

                    if pum7 == 11:
                        if computer > 103:
                            computer = 103

                    if pum7 == 12:
                        if computer > 102:
                            computer = 102

                    if pum7 == 13:
                        if computer > 101:
                            computer = 101

                    if pum7 == 14:
                        if computer > 100:
                            computer = 100

            if pum2 == pum3:
                if pum3 == pum4:
                    if pum3 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum3 == 3:
                        if computer > 111:
                            computer = 111
                            
                    if pum3 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum3 == 5:
                        if computer > 109:
                            computer = 109

                    if pum3 == 6:
                        if computer > 108:
                            computer = 108

                    if pum3 == 7:
                        if computer > 107:
                            computer = 107
                    
                    if pum3 == 8:
                        if computer > 106:
                            computer = 106
                            
                    if pum3 == 9:
                        if computer > 105:
                            computer = 105

                    if pum3 == 10:
                        if computer > 104:
                            computer = 104

                    if pum3 == 11:
                        if computer > 103:
                            computer = 103

                    if pum3 == 12:
                        if computer > 102:
                            computer = 102
                    
                    if pum3 == 13:
                        if computer > 101:
                            computer = 101

                    if pum3 == 14:
                        if computer > 100:
                            computer = 100

                if pum4 == pum5:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum5 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum5 == 4:
                        if computer > 110:
                            computer = 110

                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105
                    
                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103

                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum5 == 3:
                        if computer > 111:
                            computer = 111

                    if pum5 == 4:
                        if computer > 110:
                            computer = 110

                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105

                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103
                    
                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum7 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum7 == 4:
                        if computer > 110:
                            computer = 110

                    if pum7 == 5:
                        if computer > 109:
                            computer = 109

                    if pum7 == 6:
                        if computer > 108:
                            computer = 108

                    if pum7 == 7:
                        if computer > 107:
                            computer = 107

                    if pum7 == 8:
                        if computer > 106:
                            computer = 106

                    if pum7 == 9:
                        if computer > 105:
                            computer = 105

                    if pum7 == 10:
                        if computer > 104:
                            computer = 104

                    if pum7 == 11:
                        if computer > 103:
                            computer = 103

                    if pum7 == 12:
                        if computer > 102:
                            computer = 102

                    if pum7 == 13:
                        if computer > 101:
                            computer = 101

                    if pum7 == 14:
                        if computer > 100:
                            computer = 100

            if pum3 == pum4:
                if pum4 == pum5:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum5 == 3:
                        if computer > 111:
                            computer = 111
                            
                    if pum5 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105

                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103
                    
                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum5 == pum6:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112

                    if pum5 == 3:
                        if computer > 111:
                            computer = 111

                    if pum5 == 4:
                        if computer > 110:
                            computer = 110

                    if pum5 == 5:
                        if computer > 109:
                            computer = 109
                    
                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105
                    
                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103

                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum7 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum7 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum7 == 5:
                        if computer > 109:
                            computer = 109

                    if pum7 == 6:
                        if computer > 108:
                            computer = 108

                    if pum7 == 7:
                        if computer > 107:
                            computer = 107

                    if pum7 == 8:
                        if computer > 106:
                            computer = 106

                    if pum7 == 9:
                        if computer > 105:
                            computer = 105

                    if pum7 == 10:
                        if computer > 104:
                            computer = 104

                    if pum7 == 11:
                        if computer > 103:
                            computer = 103

                    if pum7 == 12:
                        if computer > 102:
                            computer = 102

                    if pum7 == 13:
                        if computer > 101:
                            computer = 101

                    if pum7 == 14:
                        if computer > 100:
                            computer = 100

            if pum4 == pum5:
                if pum5 == pum6:
                    if pum5 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum5 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum5 == 4:
                        if computer > 110:
                            computer = 110
                            
                    if pum5 == 5:
                        if computer > 109:
                            computer = 109

                    if pum5 == 6:
                        if computer > 108:
                            computer = 108

                    if pum5 == 7:
                        if computer > 107:
                            computer = 107

                    if pum5 == 8:
                        if computer > 106:
                            computer = 106

                    if pum5 == 9:
                        if computer > 105:
                            computer = 105

                    if pum5 == 10:
                        if computer > 104:
                            computer = 104

                    if pum5 == 11:
                        if computer > 103:
                            computer = 103

                    if pum5 == 12:
                        if computer > 102:
                            computer = 102

                    if pum5 == 13:
                        if computer > 101:
                            computer = 101

                    if pum5 == 14:
                        if computer > 100:
                            computer = 100

                if pum6 == pum7:
                    if pum7 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum7 == 3:
                        if computer > 111:
                            computer = 111

                    if pum7 == 4:
                        if computer > 110:
                            computer = 110
                    
                    if pum7 == 5:
                        if computer > 109:
                            computer = 109

                    if pum7 == 6:
                        if computer > 108:
                            computer = 108

                    if pum7 == 7:
                        if computer > 107:
                            computer = 107

                    if pum7 == 8:
                        if computer > 106:
                            computer = 106

                    if pum7 == 9:
                        if computer > 105:
                            computer = 105

                    if pum7 == 10:
                        if computer > 104:
                            computer = 104

                    if pum7 == 11:
                        if computer > 103:
                            computer = 103

                    if pum7 == 12:
                        if computer > 102:
                            computer = 102

                    if pum7 == 13:
                        if computer > 101:
                            computer = 101

                    if pum7 == 14:
                        if computer > 100:
                            computer = 100

            if pum5 == pum6:
                if pum6 == pum7:
                    if pum7 == 2:
                        if computer > 112:
                            computer = 112
                    
                    if pum7 == 3:
                        if computer > 111:
                            computer = 111
                    
                    if pum7 == 4:
                        if computer > 110:
                            computer = 110

                    if pum7 == 5:
                        if computer > 109:
                            computer = 109

                    if pum7 == 6:
                        if computer > 108:
                            computer = 108

                    if pum7 == 7:
                        if computer > 107:
                            computer = 107

                    if pum7 == 8:
                        if computer > 106:
                            computer = 106

                    if pum7 == 9:
                        if computer > 105:
                            computer = 105
                    
                    if pum7 == 10:
                        if computer > 104:
                            computer = 104

                    if pum7 == 11:
                        if computer > 103:
                            computer = 103

                    if pum7 == 12:
                        if computer > 102:
                            computer = 102

                    if pum7 == 13:
                        if computer > 101:
                            computer = 101

                    if pum7 == 14:
                        if computer > 100:
                            computer = 100



            if pum1 == pum2:
                if pum2 == 2:
                    if computer > 127:
                        computer = 127
                
                if pum2 == 3:
                    if computer > 126:
                        computer = 126

                if pum2 == 4:
                    if computer > 125:
                        computer = 125

                if pum2 == 5:
                    if computer > 124:
                        computer = 124

                if pum2 == 6:
                    if computer > 123:
                        computer = 123

                if pum2 == 7:
                    if computer > 122:
                        computer = 122
                
                if pum2 == 8:
                    if computer > 121:
                        computer = 121

                if pum2 == 9:
                    if computer > 120:
                        computer = 120

                if pum2 == 10:
                    if computer > 119:
                        computer = 119

                if pum2 == 11:
                    if computer > 118:
                        computer = 118

                if pum2 == 12:
                    if computer > 117:
                        computer = 117

                if pum2 == 13:
                    if computer > 116:
                        computer = 116

                if pum2 == 14:
                    if computer > 115:
                        computer = 115
                            
            if pum2 == pum3:
                if pum2 == 2:
                    if computer > 127:
                        computer = 127
                
                if pum2 == 3:
                    if computer > 126:
                        computer = 126
                
                if pum2 == 4:
                    if computer > 125:
                        computer = 125

                if pum2 == 5:
                    if computer > 124:
                        computer = 124

                if pum2 == 6:
                    if computer > 123:
                        computer = 123
                
                if pum2 == 7:
                    if computer > 122:
                        computer = 122

                if pum2 == 8:
                    if computer > 121:
                        computer = 121

                if pum2 == 9:
                    if computer > 120:
                        computer = 120

                if pum2 == 10:
                    if computer > 119:
                        computer = 119

                if pum2 == 11:
                    if computer > 118:
                        computer = 118

                if pum2 == 12:
                    if computer > 117:
                        computer = 117

                if pum2 == 13:
                    if computer > 116:
                        computer = 116

                if pum2 == 14:
                    if computer > 115:
                        computer = 115

            if pum3 == pum4:
                if pum4 == 2:
                    if computer > 127:
                        computer = 127
                
                if pum4 == 3:
                    if computer > 126:
                        computer = 126

                if pum4 == 4:
                    if computer > 125:
                        computer = 125
                
                if pum4 == 5:
                    if computer > 124:
                        computer = 124

                if pum4 == 6:
                    if computer > 123:
                        computer = 123

                if pum4 == 7:
                    if computer > 122:
                        computer = 122

                if pum4 == 8:
                    if computer > 121:
                        computer = 121
                
                if pum4 == 9:
                    if computer > 120:
                        computer = 120
                
                if pum4 == 10:
                    if computer > 119:
                        computer = 119

                if pum4 == 11:
                    if computer > 118:
                        computer = 118
                
                if pum4 == 12:
                    if computer > 117:
                        computer = 117

                if pum4 == 13:
                    if computer > 116:
                        computer = 116
                
                if pum4 == 14:
                    if computer > 115:
                        computer = 115

            if pum4 == pum5:
                if pum4 == 2:
                    if computer > 127:
                        computer = 127
                
                if pum4 == 3:
                    if computer > 126:
                        computer = 126

                if pum4 == 4:
                    if computer > 125:
                        computer = 125

                if pum4 == 5:
                    if computer > 124:
                        computer = 124

                if pum4 == 6:
                    if computer > 123:
                        computer = 123
                
                if pum4 == 7:
                    if computer > 122:
                        computer = 122

                if pum4 == 8:
                    if computer > 121:
                        computer = 121

                if pum4 == 9:
                    if computer > 120:
                        computer = 120

                if pum4 == 10:
                    if computer > 119:
                        computer = 119

                if pum4 == 11:
                    if computer > 118:
                        computer = 118

                if pum4 == 12:
                    if computer > 117:
                        computer = 117

                if pum4 == 13:
                    if computer > 116:
                        computer = 116

                if pum4 == 14:
                    if computer > 115:
                        computer = 115

            if pum6 == pum7:
                if pum7 == 2:
                    if computer > 127:
                        computer = 127
                
                if pum7 == 3:
                    if computer > 126:
                        computer = 126
                
                if pum7 == 4:
                    if computer > 125:
                        computer = 125

                if pum7 == 5:
                    if computer > 124:
                        computer = 124

                if pum7 == 6:
                    if computer > 123:
                        computer = 123

                if pum7 == 7:
                    if computer > 122:
                        computer = 122
                
                if pum7 == 8:
                    if computer > 121:
                        computer = 121

                if pum7 == 9:
                    if computer > 120:
                        computer = 120

                if pum7 == 10:
                    if computer > 119:
                        computer = 119

                if pum7 == 11:
                    if computer > 118:
                        computer = 118

                if pum7 == 12:
                    if computer > 117:
                        computer = 117

                if pum7 == 13:
                    if computer > 116:
                        computer = 116

                if pum7 == 14:
                    if computer > 115:
                        computer = 115



            print ("com1 의 족보")
            print ()
            
            if 0 < computer:
                if computer <= 4:
                    print ("!!!! royal straight flush !!!! (0.000153907%)")

            if 6 <= computer:
                if computer <= 17:
                    print ("!!! straight flush !!! (0.001385169%)")

            if 20 <= computer:
                if computer <= 32:
                    print ("!! four of a kind !! (0.024009603%)")

            if 35 <= computer:
                if computer <= 47:
                    print ("! full house ! (0.144057623%)")

            if 50 <=  computer:
                if computer <= 62:
                    print ("$$$$ flush $$$$ (0.196540154%)")

            if 70 == computer:
                print ("$$$ straight $$$ (0.392464678%)")

            if 80 <= computer:
                if computer <= 92:
                    print ("$$ three of a kind $$ (2.112845138%)")

            if 100 <= computer:
                if computer <= 112:
                    print ("$ two pair $ (4.75390156%)")

            if 115 <= computer:
                if computer <= 127:
                    print ("$ one pair $ (42.256902761%)")

            if 128 <= computer:
                print (" high card (no pair) (50.117739403%)")

            print ()
            print ()
            print ()
            
            if player < computer:
                print ("플레이어의 승리!!")
                pm = pm + bet1
            else:
                print ("com1 의 승리!!")
                cm = cm + bet1

                        
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
        

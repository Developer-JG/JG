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
        print ()
        print ("플레이어 돈:",pm,"cm1의 돈:",cm)
        print()
        print ("셔플중")
        print()
        pm = pm - 10
        cm = cm - 10
        bet = 20
        plag = 0
        plag2 = 0
        ans1 = 0
        ans2 = 0
        ans3 = 0
        ans4 = 0

        plag4 = 0
        
        while plag4 != 1:
        
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
                                                                                                                                                                                                                                                                                                                                                                                        plag4 = plag4 + 1
    
    
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
            print ()
            print ()
            print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ] [",ccdp4, ccdn4,"]")
            print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"] [",pcdp4,pcdn4,"]")
            print ()

            plag3 = 0

            if icn1 > icn4:
                icn = icn1
            elif icn1 < icn4:
                icn = icn4

            if ipn1 > ipn4:
                ipn = ipn1
            elif ipn1 < ipn4:
                ipn = ipn4

            if icn1 == icn4:
                if ipn1 == ipn4:
                    
                    if ipp - icp > 0:
                        print ("나의 선공")
                        plag3 = 1
                    if ipp - icp < 0:
                        print ("com1의 선공")
                        plag3 = 2
                elif ipn1 != ipn4:
                    print ("com1의 선공")
                    plag3 = 2
                    
            elif ipn1 == ipn4:
                if icn1 != icn4:
                    print ("나의 선공")
                    plag3 = 1
                    
            if icn < ipn:
                if plag3 == 0:
                    print ("나의 선공")
                    plag3 = 1
            if icn > ipn:
                if plag3 == 0:
                    print ("com1의 선공")
                    plag3 = 2

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
                    print ("판돈 올린것을 받아들입니다. 콜")
                    ans3 = ans2
                    bet = bet + ans3
                    pm = pm - ans3
                    print (ans3,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
                    print ("판돈을 올립니다. 레이즈")
                    print ("얼마나 베팅하시겠습니까? (최대 10)")
                    q = input("=")
                    ans3 = int(q)
                    if ans3 > 10 :
                        ans3 = 10
                    if ans3 < 1 :
                        ans3 = 1
                    ans3 = ans3 + ans2
                    bet = bet + ans3
                    pm = pm - ans3
                    print (ans3,"배팅하셨습니다.")
                
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
                        ans3 = int(q)
                        if ans3 > 10 :
                            ans3 = 10
                        if ans3 < 1 :
                            ans3 = 1
                        ans3 = ans3 + ans2
                        bet = bet + ans3
                        pm = pm - ans3
                        print (ans3,"배팅하셨습니다.")
                    
                if plag2 != 1:
                    print ()
                    print ("com1의 레이즈")
                    icb2 = int(cb2)
                    if ans3 > 0:
                        ans4 = ans3 + icb2
                    else:
                        ans4 = icb2
                    bet = bet + ans4
                    pm = pm - ans3
                    print ("com1이 ",ans4,"배팅 하였습니다. 총 배팅:",bet)
                    
            if plag3 == 2:
                print ()
                print ("com1의 레이즈")
                icb2 = int(cb2)
                ans3 = ans2 + icb2
                print ("com1이 ",ans3,"배팅 하였습니다.")
                bet = bet + ans3
                cm = cm - ans3

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
                        bet = bet + ans3
                        pm = pm - ans3
                        print (ans1,"배팅 하셨습니다. 총 배팅:",bet)
                if ans == 2:
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
                        ans4 = int(q)
                        if ans4 > 10 :
                            ans4 = 10
                        if ans4 < 1 :
                            ans4 = 1
                        ans4 = ans3 + ans4
                        bet = bet + ans4
                        pm = pm - ans4
                        print (ans4,"배팅하셨습니다. 총 배팅:",bet)
                                 
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
        

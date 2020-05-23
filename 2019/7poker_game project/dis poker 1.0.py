pcd1 = 2
pcd2 = 3
pcd3 = 2
pcd4 = 3
pcd5 = 1
pcd6 = 4 
pcd7 = 2

pcdn1 = 2
pcdn2 = 2
pcdn3 = 2
pcdn4 = 11
pcdn5 = 2
pcdn6 = 2
pcdn7 = 6

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
    if player < 1:
        player = 1
if eplag2 >= 5:
    if player < 2:
        player = 2
if eplag3 >= 5:
    if player < 3:
        player = 3
if eplag4 >= 5:
    if player < 4:
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
    if pum2 == 13:
        if pum3 == 12:
            if pum4 == 11:
                if pum5 == 2:
                    player = 6

if pum1 == 14:
    if pum2 == 13:
        if pum3 == 12:
            if pum4 == 3:
                if pum5 == 2:
                    player = 7

if pum1 == 14:
    if pum2 == 13:
        if pum3 == 4:
            if pum4 == 3:
                if pum5 == 2:
                    player = 8

if pum1 == 14:
    if pum2 == 5:
        if pum3 == 4:
            if pum4 == 3:
                if pum5 == 2:
                    player = 9

if pum1 == 6:
    if pum2 == 5:
        if pum3 == 4:
            if pum4 == 3:
                if pum5 == 2:
                    player = 10

if pum1 == 7:
    if pum2 == 6:
        if pum3 == 5:
            if pum4 == 4:
                if pum5 == 3:
                    player = 11

if pum1 == 8:
    if pum2 == 7:
        if pum3 == 6:
            if pum4 == 5:
                if pum5 == 4:
                    player = 12                         

if pum1 == 9:
    if pum2 == 8:
        if pum3 == 7:
            if pum4 == 6:
                if pum5 == 5:
                    player = 13

if pum1 == 10:
    if pum2 == 9:
        if pum3 == 8:
            if pum4 == 7:
                if pum5 == 6:
                    player = 14

if pum1 == 11:
    if pum2 == 10:
        if pum3 == 9:
            if pum4 == 8:
                if pum5 == 7:
                    player = 15

if pum1 == 12:
    if pum2 == 11:
        if pum3 == 10:
            if pum4 == 9:
                if pum5 == 8:
                    player = 16

if pum1 == 13:
    if pum2 == 12:
        if pum3 == 11:
            if pum4 == 10:
                if pum5 == 9:
                    player = 17

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
    if pum1 == 2:
        player = 21
    if pum1 == 3:
        player = 22
    if pum1 == 4:
        player = 23
    if pum1 == 5:
        player = 24
    if pum1 == 6:
        player = 25
    if pum1 == 7:
        player = 26
    if pum1 == 8:
        player = 27
    if pum1 == 9:
        player = 28
    if pum1 == 10:
        player = 29
    if pum1 == 11:
        player = 30
    if pum1 == 12:
        player = 31
    if pum1 == 13:
        player = 32
    if pum1 == 14:
        player = 33
        
if pum2 == pum3 == pum4 == pum5:
    if pum1 == 2:
        player = 21
    if pum1 == 3:
        player = 22
    if pum1 == 4:
        player = 23
    if pum1 == 5:
        player = 24
    if pum1 == 6:
        player = 25
    if pum1 == 7:
        player = 26
    if pum1 == 8:
        player = 27
    if pum1 == 9:
        player = 28
    if pum1 == 10:
        player = 29
    if pum1 == 11:
        player = 30
    if pum1 == 12:
        player = 31
    if pum1 == 13:
        player = 32
    if pum1 == 14:
        player = 33

if pum3 == pum4 == pum5 == pum6:
    if pum1 == 2:
        player = 21
    if pum1 == 3:
        player = 22
    if pum1 == 4:
        player = 23
    if pum1 == 5:
        player = 24
    if pum1 == 6:
        player = 25
    if pum1 == 7:
        player = 26
    if pum1 == 8:
        player = 27
    if pum1 == 9:
        player = 28
    if pum1 == 10:
        player = 29
    if pum1 == 11:
        player = 30
    if pum1 == 12:
        player = 31
    if pum1 == 13:
        player = 32
    if pum1 == 14:
        player = 33
        
if pum4 == pum5 == pum6 == pum7:
    if pum1 == 2:
        player = 21
    if pum1 == 3:
        player = 22
    if pum1 == 4:
        player = 23
    if pum1 == 5:
        player = 24
    if pum1 == 6:
        player = 25
    if pum1 == 7:
        player = 26
    if pum1 == 8:
        player = 27
    if pum1 == 9:
        player = 28
    if pum1 == 10:
        player = 29
    if pum1 == 11:
        player = 30
    if pum1 == 12:
        player = 31
    if pum1 == 13:
        player = 32
    if pum1 == 14:
        player = 33

print ("나의 족보")
    
if 0 < player:
    if player <=4:
        print ("!!! royal flush!!! (0.0032%)")

if 6 <=player:
    if player <= 17:
        print ("!!straight flush!! (0.029%)")

if 20 <=player:
    if player <= 33:
        print ("!four of a kind! (0.16%)")

        

        
        

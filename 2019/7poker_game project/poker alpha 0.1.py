import random

print ("게임 시작")

pm = 2000
cm = 2000

shdc = ['스페이드', '하트', '다이아', '클로버']

pcdn1 = random.randint(1, 13)
pcdn2 = random.randint(1, 13)
pcdn3 = random.randint(1, 13)
pcdn4 = random.randint(1, 13)
pcdn5 = random.randint(1, 13)
pcdn6 = random.randint(1, 13)
pcdn7 = random.randint(1, 13)

pcdp1 = random.choice(shdc)
pcdp2 = random.choice(shdc)
pcdp3 = random.choice(shdc)
pcdp4 = random.choice(shdc)
pcdp5 = random.choice(shdc)
pcdp6 = random.choice(shdc)
pcdp7 = random.choice(shdc)

ccdn1 = random.randint(1, 13)
ccdn2 = random.randint(1, 13)
ccdn3 = random.randint(1, 13)
ccdn4 = random.randint(1, 13)
ccdn5 = random.randint(1, 13)
ccdn6 = random.randint(1, 13)
ccdn7 = random.randint(1, 13)

ccdp1 = random.choice(shdc)
ccdp2 = random.choice(shdc)
ccdp3 = random.choice(shdc)
ccdp4 = random.choice(shdc)
ccdp5 = random.choice(shdc)
ccdp6 = random.choice(shdc)
ccdp7 = random.choice(shdc)

print ("com1의 패: [",ccdp1, ccdn1,"] [ ? ? ] [ ? ? ]")
print ("플래이어의 패: [",pcdp1, pcdn1,"] [",pcdp2, pcdn2,"] [",pcdp3, pcdn3,"]")

iccdn1 = int(ccdn1)
iacdp1 = int(acdn1)

print ("배팅하시겠습니까?")
print ("[ford = 0] [check = 1] [call = 2] [raise = 3] [all in = 4]")

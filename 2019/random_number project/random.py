import random
import time
start_time = time.time()
aa = 0
d = 0
e = 0
while aa != 100000:
    a = 0
    bn1 = 0
    bn2 = 0
    while a != 100000:
        b = random.randint(1,2)
        if b == 1:
            bn1 = bn1 + 1
        if b == 2:
            bn2 = bn2 + 1
        a = a + 1
    bn1 = bn1 / 1000
    bn2 = bn2 / 1000
    if bn1 > bn2:
        d = d + 1
    if bn2 > bn1:
        e = e + 1
    aa = aa + 1
d = d / 1000
e = e / 1000
end_time = time.time()
print()
print(end_time - start_time)
print()
print(d)
print(e)

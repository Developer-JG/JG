# Second / Minute / Hour / Day / Year

print("\nTime converter\n")

print("\n바꾸교쟈 하는 단위를 입력하세요.")
while True:
    unit = input(" = ")
    if unit == 's' or unit == 'm' or unit == 'h' or unit == 'd'  or unit == 'y':
        break
    else:
        print("\n올바른 시간단위를 입력하세요.")

print("\n바꾸교쟈 하는 값을 입력하세요.")
while True:
    value = input(" = ")
    if value.isdigit() == True:
        break
    else:
        print("\n올바른 값을 입력하세요.")

sec, min, hour, day, year = 0, 0, 0, 0, 0

if unit == 's':
    sec = int(value)
if unit == 'm':
    min = int(value)
if unit == 'h':
    hour = int(value)
if unit == 'd':
    day = int(value)
if unit == 'y':
    year = int(value)

print(f"\n\nYear : {year}\nDay : {day}\nHour : {hour}\nMinute : {min}\nSecond : {sec}")

if unit == 'y':
    day = year * 365
if unit == 'd' or unit == 'y':
    hour = day * 24
if unit == 'h' or unit == 'd' or unit == 'y':
    min = hour * 60
if unit == 'm' or unit == 'h' or unit == 'd' or unit == 'y':
    sec = min * 60

print(f"\n\nYear : {year}\nDay : {day}\nHour : {hour}\nMinute : {min}\nSecond : {sec}")

if unit == 's':
    min = sec / 60
if unit == 's' or unit == 'm':
    hour = min / 60
if unit == 's' or unit == 'm' or unit == 'h':
    day = hour / 24
if unit == 's' or unit == 'm' or unit == 'h' or unit == 'd':
    year = day / 365

print(f"\n\nYear : {year}\nDay : {day}\nHour : {hour}\nMinute : {min}\nSecond : {sec}")
input()
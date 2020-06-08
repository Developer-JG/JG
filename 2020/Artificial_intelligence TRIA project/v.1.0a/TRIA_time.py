from pytz import timezone
from datetime import datetime

city = "Asia/Seoul"

year = datetime.now(timezone(str(city))).year #년도
mon = datetime.now(timezone(str(city))).month #월
mday = datetime.now(timezone(str(city))).day #일
hour = datetime.now(timezone(str(city))).hour #시
min = datetime.now(timezone(str(city))).minute #분
wday = datetime.now(timezone(str(city))).weekday #요일

#시간알림
def time(command_result_1, command_result, location_1):
    week_day = wday()

    if week_day == 0:
        week_day = '월요일'
    elif week_day == 1:
        week_day = '화요일'
    elif week_day == 2:
        week_day = '수요일'
    elif week_day == 3:
        week_day = '목요일'
    elif week_day == 4:
        week_day = '금요일'
    elif week_day == 5:
        week_day = '토요일'
    elif week_day == 6:
        week_day = '일요일'

    if command_result == '년':
        print("{0}년 이에요.".format(year))
    elif command_result == '월':
        print("{0}월 이에요.".format(mon))
    elif command_result == '시':
        print("{0}시 이에요.".format(hour))
    elif command_result == '분':
        print("{0}분 이에요.".format(min))
    elif command_result == '월' or command_result == '화' or command_result == '수' or \
        command_result == '목' or command_result == '금' or command_result == '토':
        print("{0} 이에요.".format(week_day))
    elif command_result == '일':
        try:
            int(command_result_1)
            print("{0}일 이에요.".format(mday))
        except:
            print("{0} 이에요.".format(week_day))
    else:
        print("{0} 표준시\n{1}년\n{2}월 {3}일 {4}\n{5}시 {6}분" \
        .format(location_1, year, mon, mday, week_day, hour, min))
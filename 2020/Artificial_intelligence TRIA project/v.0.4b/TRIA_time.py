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
def time(command_result, location_1):
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

    print("{0} 표준시\n{1}년\n{2}월 {3}일 {4}\n{5}시 {6}분" \
          .format(location_1, year, mon, mday, week_day, hour, min))
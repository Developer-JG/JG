from pytz import timezone
from datetime import timedelta
from datetime import datetime

city = "Asia/Seoul"  # 지역별 시간설정
timezone = datetime.now(timezone(city))
mday = timezone.day  # 일

#시간알림
def time(command_result, year, mon, mday, hour, min, sec, wday, location_1):

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
    elif command_result == '일':
        print("{0}일 이에요.".format(mday))
    elif command_result == '시':
        print("{0}시 이에요.".format(hour))
    elif command_result == '분':
        print("{0}분 이에요.".format(min))
    elif command_result == '월' or command_result == '화' or command_result == '수' or \
        command_result == '목' or command_result == '금' or command_result == '토' or \
        command_result == '요':
        print("{0} 이에요.".format(week_day))
    elif command_result == 'op':
        print("{0} 표준시\n{1}년\n{2}월 {3}일 {4}" \
        .format(location_1, year, mon, mday, week_day))
    elif mday == mday_:
        print("{0} 표준시\n{1}년\n{2}월 {3}일 {4}\n{5}시 {6}분 {7}초" \
        .format(location_1, year, mon, mday, week_day, hour, min, sec))


    '''
        int(command_result_1)
        print("{0}일 이에요.".format(mday))
    except:
        print("{0} 이에요.".format(week_day))
    '''
from pytz import timezone
from datetime import datetime

city = "Asia/Seoul"  # 지역별 시간설정
wday = datetime.now(timezone(str(city))).weekday #요일 0~6

class weather_info:
    def __init__(self, time, weather, precipitation, high, low):
        self.time = time
        self.weather = weather
        self.precipitation = precipitation
        self.high = high
        self.low = low

week_day_2 = wday + 1
week_day_3 = wday + 2
week_day_4 = wday + 3
week_day_5 = wday + 4

week_day_list = [week_day_2, week_day_3, week_day_4, week_day_5]

for i in range(len(week_day_list)):
    if week_day_list[i].time > 6:
        week_day_list[i].time -= 6

weather_1 = weather_info()
weather_2 = weather_info()
weather_3 = weather_info()
weather_4 = weather_info()
weather_5 = weather_info()

# 날씨
def weather(location_2, location_3, location_4, mon, mday):
    print("{0} {1} {2} 현재 날씨".format(location_2,location_3,location_4))
    print("{0}월 / {1}일".format(mon, mday))
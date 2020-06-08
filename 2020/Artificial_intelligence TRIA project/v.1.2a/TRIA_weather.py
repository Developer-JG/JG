class weather_info:
    def __init__(self, weather, precipitation_percent, high, low):
        self.weather = weather
        self.precipitation_percent = precipitation_percent
        self.high = high
        self.low = low

weather_1 = weather_info(0, 0, 0, 0)
weather_2 = weather_info(0, 0, 0, 0)
weather_3 = weather_info(0, 0, 0, 0)
weather_4 = weather_info(0, 0, 0, 0)
weather_5 = weather_info(0, 0, 0, 0)

week_day_list = [weather_1, weather_2, weather_3, weather_4, weather_5]

precipitation = 0
humidity = '0'
wind = '0'
bodily_temperature = '0'
UV_index = '0'

# 날씨
def weather(location, mon, mday, wday):
    print("{0}월 / {1}일".format(mon, mday))
    print("{0} 현재 날씨".format(location))
    print('\n강수량: {0}mm  습기: {1}%'.format(precipitation, humidity))
    print('바람: {0}m/s  체감온도: {1}℃'.format(wind, bodily_temperature))
    print('자외선 지수: {0}단계'.format(UV_index))
    print("\n      주간 날씨")
    for i in range(len(week_day_list)):

        week_day = wday + i + 1

        if week_day > 6:
            week_day -= 6

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

        print(" {0}  {1}℃ /{2}℃  {3}%"\
              .format(week_day, week_day_list[i].high, \
                      week_day_list[i].low, week_day_list[i].precipitation_percent))


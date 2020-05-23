from pytz import timezone
from datetime import datetime

city = "Asia/Seoul" #지역별 시간설정

def time_set():
    time_zone = datetime.now(timezone(str(city)))

    print (time_zone)
time_set()
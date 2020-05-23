from pytz import timezone
from datetime import datetime

from TRIA_contact import * #연락처
from TRIA_justchatting import * #일상대화
from TRIA_music import * #노래
from TRIA_operatingsystem import * #운영체제
from TRIA_time import * #시간
from TRIA_weather import * #날씨
from TRIA_websurfing import * #웹검색

print("The artificial intelligence Assistnt Project\n'TRIA'")

# 개인 신상정보
name = '정규'

city = "Asia/Seoul"  # 지역별 시간설정

location_1 = '대한민국' #국가
location_2 = '서울특별시' #특별시, 광역시, 특별자치시, 도, 특별자치도
location_2 = '노원구' #시, 군, 구
location_3 = '공릉2동' #읍, 면,

def time():
    year = datetime.now(timezone(str(city))).year #년도
    mon = datetime.now(timezone(str(city))).month #월
    mday = datetime.now(timezone(str(city))).day #일
    hour = datetime.now(timezone(str(city))).hour #시
    min = datetime.now(timezone(str(city))).min #분
    sec = datetime.now(timezone(str(city))).second #초
    wday = datetime.now(timezone(str(city))).weekday #요일

# 메인
def main():
    command = input("\n:") #"hello python"
    command_result = list(command) #{'h', 'e', 'l', ... 'n']
    command_result = ' '.join(command_result).split()
    command_result = [v for v in command_result if v]

    year = datetime.now(timezone(str(city))).year  # 년도
    mon = datetime.now(timezone(str(city))).month  # 월
    mday = datetime.now(timezone(str(city))).day  # 일
    hour = datetime.now(timezone(str(city))).hour  # 시
    min = datetime.now(timezone(str(city))).min  # 분
    sec = datetime.now(timezone(str(city))).second  # 초
    wday = datetime.now(timezone(str(city))).weekday  # 요일

    print("")

    i = 0
    plag = 0

    while i <= len(command_result):
        try:
            command_result[i] == '안' and command_result[i+1] == '녕'
            hello_1(name,hour)
            plag =+ 1
            break
        except IndexError:
            pass

        try:
            command_result[i] == '반' and command_result[i + 1] == '가' and command_result[i + 2] == '워'

            plag = + 1
            break
        except IndexError:
            pass

        i = i + 1

    if plag == 0:
        print("죄송해요\n잘 이해하지 못했어요.")

    main()

if __name__ == "__main__":
    main()
from pytz import timezone
from datetime import datetime

from TRIA_contact import * #연락처
from TRIA_exchange import * #환전
from TRIA_justchatting import * #일상대화
from TRIA_map import * #지도
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
location_3 = '노원구' #시, 군, 구
location_4 = '공릉2동' #읍, 면,

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

    plag = 0

    for i in range(len(command_result)):
        try:
            if command_result[i] == '안' and command_result[i + 1] == '녕' or \
                command_result[i] == '반' and command_result[i + 1] == '가' and command_result[i + 2] == '워':
                hello(name,hour)
                plag =+ 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '미' and command_result[i + 1] == '안':
                sorry()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '재' and command_result[i + 1] == '미' and command_result[i + 2] == '있':
                injoy()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '재' and command_result[i + 1] == '미' and command_result[i + 2] == '없':
                not_injoy()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '배' and command_result[i + 1] == '고' and command_result[i + 2] == '파' or \
                command_result[i] == '허' and command_result[i + 1] == '기':
                hungry(location_3,location_4)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '성' and command_result[i + 1] == '별':

                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '나' and command_result[i + 1] == '이':

                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '국' and command_result[i + 1] == '적':

                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '행' and command_result[i + 1] == '복' or \
                command_result[i] == '좋':

                plag = + 1
                break
        except IndexError:
            pass

    if plag == 0:
        print("죄송해요\n잘 이해하지 못했어요.")

    main()

if __name__ == "__main__":
    main()
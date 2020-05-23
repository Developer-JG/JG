from pytz import timezone
from datetime import datetime

from TRIA_contact import * #연락처
from TRIA_exchange import * #환전
from TRIA_justchatting import * #일상대화
from TRIA_map import * #지도
from TRIA_music import * #노래
from TRIA_operatingsystem import * #운영체제
from TRIA_time import * #시간
from TRIA_weather import * #날씨 /
from TRIA_websurfing import * #웹검색

print("The artificial intelligence Assistnt Project\n'TRIA'")

# 개인 신상정보
name = '정규'

city = "Asia/Seoul"  # 지역별 시간설정

location_1 = '대한민국' #국가
location_2 = '서울특별시' #특별시, 광역시, 특별자치시, 도, 특별자치도
location_3 = '노원구' #시, 군, 구
location_4 = '공릉2동' #읍, 면,

def time_set():
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
    command_result_1 = list(command) #{'h', 'e', 'l', ... 'n']
    command_result = ' '.join(command_result_1).split()
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
            if command_result[i] == '미' and command_result[i + 1] == '안' or \
                command_result[i] == '죄' and command_result[i + 1] == '':
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
            if command_result[i] == '성' and command_result[i + 1] == '별' or \
                command_result[i] == '남' or command_result[i] == '여':
                gender()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '나' and command_result[i + 1] == '이' or \
                command_result[i] == '몇' and command_result[i + 1] == '':
                age()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '국' and command_result[i + 1] == '적' or \
                command_result[i] == '나' and command_result[i + 1] == '라' :
                contry()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '행' and command_result[i + 1] == '복' or \
                command_result[i] == '좋':
                happy(name)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '감' and command_result[i + 1] == '사' or \
                command_result[i] == '고' and command_result[i + 1] == '마' or \
                command_result[i] == '고' and command_result[i + 1] == '맙':
                Thanks()
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '배' and command_result[i + 1] == '고' and command_result[i + 2] == '파' or \
                command_result[i] == '허' and command_result[i + 1] == '기' or \
                command_result[i] == '맛' and command_result[i + 1] == '집' or \
                command_result[i] == '음' and command_result[i + 1] == '식' and command_result[i + 2] == '점':
                hungry(command_result,location_3,location_4)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '날' and command_result[i + 1] == '씨' or \
                command_result[i] == '해' or command_result[i] == '맑' or command_result[i] == '비' or \
                command_result[i] == '바' and command_result[i + 1] == '람' or \
                command_result[i] == '강' and command_result[i + 1] == '수' or \
                command_result[i] == '습' and command_result[i + 1] == '기' or \
                command_result[i] == '자' and command_result[i + 1] == '외' and command_result[i + 2] == '선' or \
                command_result[i] == '우' and command_result[i + 1] == '산' or \
                command_result[i] == '우' and command_result[i + 1] == '비' or \
                command_result[i] == '온' and command_result[i + 1] == '도' or \
                command_result[i] == '기' and command_result[i + 1] == '온' or \
                command_result[i] == '추' or command_result[i] == '더' or \
                command_result[i] == '따' and command_result[i + 1] == '뜻':
                weather(location_2, location_3, location_4, mon, mday)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '년' or command_result[i] == '월' or \
                command_result[i] == '시' or command_result[i] == '분' or \
                command_result[i] == '분' or command_result[i] == '초' or \
                command_result[i] == '월' or command_result[i] == '화' or \
                command_result[i] == '수' or command_result[i] == '목' or \
                command_result[i] == '금' or command_result[i] == '토' or \
                command_result[i] == '일' or \
                command_result[i] == '시' and command_result[i + 1] == '간' or \
                command_result[i] == '날' and command_result[i + 1] == '자' or \
                command_result[i] == '요' and command_result[i + 1] == '일':
                try:
                    time(command_result[i - 1],command_result[i], location_1)
                except:
                    time(command_result[i], command_result[i], location_1)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '길' and command_result[i + 1] == '안' and command_result[i + 2] == '내'or \
                command_result[i] == '가' and command_result[i + 1] == '고' \
                and command_result[i + 2] == '싶' and command_result[i + 3] == '어':
                navigation(command_result_1, command_result, location_2, location_3, location_4)
                plag = + 1
                break
        except IndexError:
            pass

        try:
            if command_result[i] == '찾' or \
                command_result[i] == '검' and command_result[i + 1] == '색' or \
                command_result[i] == '뭐' and command_result[i + 1] == '야':
                Search(command_result_1, command_result)
                plag = + 1
                break
        except IndexError:
            pass

    if plag == 0:
        print("죄송해요\n잘 이해하지 못했어요.")

    main()

if __name__ == "__main__":
    main()
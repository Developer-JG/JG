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

    app = ''
    naver, google, mango, cacao, trip, code = 0 , 0 , 0 , 0 , 0 , 0

    for i in range(len(command_result)):
        try:
            if command_result[i] == '네' and command_result[i + 1] == '이' and command_result[i + 2] == '버':
                app = '네이버'
                naver = 1
        except IndexError:
            pass

        try:
            if command_result[i] == '구' and command_result[i + 1] == '글':
                app = '구글'
                google = 1
        except IndexError:
            pass

        try:
            if command_result[i] == '망' and command_result[i + 1] == '고' and command_result[i + 2] == '플' and \
                command_result[i + 3] == '레' and command_result[i + 4] == '이' and command_result[i + 5] == '트':
                app = '망고플레이트'
                mango = 1
        except IndexError:
            pass

        try:
            if command_result[i] == '카' and command_result[i + 1] == '카' and command_result[i + 2] == '오' and \
                command_result[i + 3] == '플' and command_result[i + 4] == '레' and command_result[i + 5] == '이' and \
                command_result[i + 5] == '스':
                app = '카카오플레이스'
                cacao = 1
        except IndexError:
            pass

        try:
            if command_result[i] == '트' and command_result[i + 1] == '립' and command_result[i + 2] == '어' and \
                    command_result[i + 3] == '드' and command_result[i + 4] == '바' and command_result[i + 5] == '이' and \
                    command_result[i + 5] == '저':
                app = '트립어드바이저'
                trip = 1
        except IndexError:
            pass

        try:
            if command_result[i] == '다' and command_result[i + 1] == '이' and command_result[i + 2] == '닝' and \
                    command_result[i + 3] == '코' and command_result[i + 4] == '드':
                app = '다이닝코드'
                code = 1
        except IndexError:
            pass

    location_2_ = ''
    location_3_ = ''
    location_4_ = ''
    tree = 0

    for i in range(len(command_result_1)):
        try:
            if command_result_1[i] == '특' and command_result_1[i + 1] == '별' and command_result_1[i + 2] == '시' or \
                command_result_1[i] == '광' and command_result_1[i + 1] == '역' and command_result_1[i + 2] == '시' or \
                command_result_1[i] == '특' and command_result_1[i + 1] == '별' and \
                command_result_1[i + 2] == '자' and command_result_1[i + 3] == '치' and command_result_1[i + 4] == '시' or \
                command_result_1[i] == '시':
                if tree == 0:
                    while command_result_1[i - 1] != ' ' and i > 0:
                        location_2_ = command_result_1[i - 1] + location_2_
                        i = i - 1
                    location_2_ = location_2_ + '시'
                    tree = 1
        except IndexError:
            pass

        try:
            if command_result_1[i] == '특' and command_result_1[i + 1] == '별' and \
                command_result_1[i + 2] == '자' and command_result_1[i + 3] == '치' and command_result_1[i + 4] == '도' or \
                command_result_1[i] == '도':
                if tree == 0:
                    while command_result_1[i - 1] != ' ' and i > 0:
                        location_2_ = command_result_1[i - 1] + location_2_
                        i = i - 1
                        location_2_ = location_2_ + '도'
                        tree = 2
        except IndexError:
            pass

        try:
            if command_result_1[i] == '시':
                if tree != 1:
                    while command_result_1[i - 1] != ' ' and i > 0:
                        location_3_ = command_result_1[i - 1] + location_3_
                        i = i - 1
                    location_3_ = location_3_ + '시'
                    tree = 3
        except IndexError:
            pass

        try:
            if command_result_1[i] == '군':
                while command_result_1[i - 1] != ' ' and i > 0:
                    location_3_ = command_result_1[i - 1] + location_3_
                    i = i - 1
                location_3_ = location_3_ + '시'
                tree = 3
        except IndexError:
            pass

        try:
            if command_result_1[i] == '구':
                if tree != 2:
                    while command_result_1[i - 1] != ' ' and i > 0:
                        location_3_ = command_result_1[i - 1] + location_3_
                        i = i - 1
                    location_3_ = location_3_ + '구'
                    tree = 3
        except IndexError:
            pass

        try:
            if command_result_1[i] == '읍' or command_result_1[i] == '면' or command_result_1[i] == '동' or command_result_1[i] == '리':
                while command_result_1[i - 1] != ' ' and i > 0:
                    location_4_ = command_result_1[i] + location_4_
                    i = i - 1
        except IndexError:
            pass

    plag, count, loof = 0, 0, 0
    command_list = []

    while True:
        for i in range(len(command_result)):
            try:
                if command_result[i] == '미' and command_result[i + 1] == '안' or \
                    command_result[i] == '죄' and command_result[i + 1] == '':
                    for i in range(len(command_list)):
                        if command_list[i] == '_sorry_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_sorry_')
                    elif plag == 1 and loof == 1:
                        sorry()
                        command_list.remove('_sorry_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '재' and command_result[i + 1] == '미' and command_result[i + 2] == '있':
                    for i in range(len(command_list)):
                        if command_list[i] == '_injoy_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_injoy_')
                    elif plag == 1 and loof == 1:
                        injoy()
                        command_list.remove('_injoy_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '재' and command_result[i + 1] == '미' and command_result[i + 2] == '없':
                    for i in range(len(command_list)):
                        if command_list[i] == '_not_injoy_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_not_injoy_')
                    elif plag == 1 and loof == 1:
                        not_injoy()
                        command_list.remove('_not_injoy_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '성' and command_result[i + 1] == '별' or \
                    command_result[i] == '남' or command_result[i] == '여':
                    for i in range(len(command_list)):
                        if command_list[i] == '_gender_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_gender_')
                    elif plag == 1 and loof == 1:
                        gender()
                        command_list.remove('_gender_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '나' and command_result[i + 1] == '이' or \
                    command_result[i] == '몇' and command_result[i + 1] == '살':
                    for i in range(len(command_list)):
                        if command_list[i] == '_age_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_age_')
                    elif plag == 1 and loof == 1:
                        age()
                        command_list.remove('_age_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '국' and command_result[i + 1] == '적' or \
                    command_result[i] == '나' and command_result[i + 1] == '라' :
                    for i in range(len(command_list)):
                        if command_list[i] == '_contry_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_contry_')
                    elif plag == 1 and loof == 1:
                        contry()
                        command_list.remove('_contry_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '행' and command_result[i + 1] == '복' or \
                    command_result[i] == '좋':
                    for i in range(len(command_list)):
                        if command_list[i] == '_happy_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_happy_')
                    elif plag == 1 and loof == 1:
                        happy(name)
                        command_list.remove('_happy_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '감' and command_result[i + 1] == '사' or \
                    command_result[i] == '고' and command_result[i + 1] == '마' or \
                    command_result[i] == '고' and command_result[i + 1] == '맙':
                    for i in range(len(command_list)):
                        if command_list[i] == '_thanks_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_thanks_')
                    elif plag == 1 and loof == 1:
                        thanks()
                        command_list.remove('_thanks_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '친' and command_result[i + 1] == '구':
                    for i in range(len(command_list)):
                        if command_list[i] == '_friend_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        if app != '':
                            count = count + 2
                        else:
                            count = count + 1
                            if loof != 1:
                                command_list.append('_friend_')
                    elif plag == 1 and loof == 1:
                        friend(name, hour)
                        command_list.remove('_friend_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '배' and command_result[i + 1] == '고' and command_result[i + 2] == '파' or \
                    command_result[i] == '허' and command_result[i + 1] == '기' or \
                    command_result[i] == '맛' and command_result[i + 1] == '집' or \
                    command_result[i] == '음' and command_result[i + 1] == '식' and command_result[i + 2] == '점':
                    for i in range(len(command_list)):
                        if command_list[i] == '_hungry_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        count = count + 1
                        if loof != 1:
                            command_list.append('_hungry_')
                    elif plag == 1 and loof == 1:
                        hungry(command_result,location_3,location_4)
                        command_list.remove('_hungry_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '날' and command_result[i + 1] == '씨' or \
                    command_result[i] == '맑' or command_result[i] == '비' or \
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
                    for i in range(len(command_list)):
                        if command_list[i] == '_weather_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        count = count + 1
                        if loof != 1:
                            command_list.append('_weather_')
                    elif plag == 1 and loof == 1:
                        weather(location_4, mon, mday)
                        command_list.remove('_weather_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '몇' and command_result[i + 1] == '년' or \
                    command_result[i] == '몇' and command_result[i + 1] == '월' or \
                    command_result[i] == '몇' and command_result[i + 1] == '시' or \
                    command_result[i] == '몇' and command_result[i + 1] == '분' or \
                    command_result[i] == '몇' and command_result[i + 1] == '분' or \
                    command_result[i] == '몇' and command_result[i + 1] == '초' or \
                    command_result[i] == '월' or \
                    command_result[i] == '화' or command_result[i] == '수' or \
                    command_result[i] == '목' or command_result[i] == '금' or \
                    command_result[i] == '토' or command_result[i] == '일' or \
                    command_result[i] == '시' and command_result[i + 1] == '간' or \
                    command_result[i] == '날' and command_result[i + 1] == '자' or \
                    command_result[i] == '요' and command_result[i + 1] == '일':
                    for i in range(len(command_list)):
                        if command_list[i] == '_time_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        count = count + 1
                        if loof != 1:
                            command_list.append('_time_')
                    elif plag == 1 and loof == 1:
                        try:
                            time(command_result[i - 1], command_result[i], location_1)
                        except:
                            time(command_result[i], command_result[i], location_1)
                        command_list.remove('_time_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '길' and command_result[i + 1] == '안' and command_result[i + 2] == '내'or \
                    command_result[i] == '가' and command_result[i + 1] == '고' and \
                    command_result[i + 2] == '싶' and command_result[i + 3] == '어':
                    for i in range(len(command_list)):
                        if command_list[i] == '_navigation_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        count = count + 1
                        if loof != 1:
                            command_list.append('_navigation_')
                    elif plag == 1 and loof == 1:
                        navigation(command_result_1, command_result, location_2, location_3, location_4)
                        command_list.remove('_navigation_')
                    loof = 0
            except IndexError:
                pass

            try:
                if command_result[i] == '찾' or \
                    command_result[i] == '검' and command_result[i + 1] == '색' or \
                    command_result[i] == '뭐' and command_result[i + 1] == '야':
                    for i in range(len(command_list)):
                        if command_list[i] == '_Search_':
                            loof = 1
                    if plag == 0 and loof == 0:
                        count = count + 1
                        if loof != 1:
                            command_list.append('_Search_')
                    elif plag == 1 and loof == 1:
                        search(command_result_1, command_result)
                        command_list.remove('_search_')
                    loof = 0
            except IndexError:
                pass

        if plag == 0:
            if count == 1:
                plag = 1
            elif count == 0:
                for i in range(len(command_result)):
                    try:
                        if command_result[i] == '안' and command_result[i + 1] == '녕' or \
                            command_result[i] == '반' and command_result[i + 1] == '가' and command_result[i + 2] == '워' or \
                            command_result[i] == '방' and command_result[i + 1] == '가':
                            hello(name, hour)
                            count = 1
                    except IndexError:
                        pass
                if count != 1:
                    print("죄송해요\n잘 이해하지 못했어요.")
                    main()
            elif count >= 2:
                print("죄송해요\n잘 이해하지 못했어요.")
                main()
        elif plag == 1:
             main()

if __name__ == "__main__":
    main()
import time

from TRIA_justchatting import * #일상대화
from TRIA_music import * #노래
from TRIA_operatingsystem import * #운영체제
from TRIA_time import * #시간
from TRIA_weather import * #날씨
from TRIA_websurfing import * #웹검색

from Main_Command_cleanup import * #명령어 정리

print("The artificial intelligence Assistnt Project\n'TRIA'")

# 개인 신상정보
name = '정규'
location_1 = '대한민국' #국가
location_2 = '서울특별시' #특별시, 광역시, 특별자치시, 도, 특별자치도
location_2 = '노원구' #시, 군, 구
location_3 = '공릉2동' #읍, 면,

# 메인
def main():
    command = input("\n:") #"hello python"
    command_result = list(command) #{'h', 'e', 'l', ... 'n']
    command_result = ' '.join(command_result).split()
    command_result = [v for v in command_result if v]

    i = 1

    while i <= len(command_result):
        if command_result[i] == '안' and command_result[i+1] == '녕':
            hello_1(set_name)
        if command_result[i] == '반' and command_result[i + 1] == '가' and command_result[i + 2] == '워':
            pass

        i =+ 1

    print("죄송해요\n잘 이해하지 못했어요.")

    main()

if __name__ == "__main__":
    main()
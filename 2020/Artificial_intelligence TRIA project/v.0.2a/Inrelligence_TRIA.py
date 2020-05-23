import time

from TRIA_justchatting import * #일상대화
from TRIA_music import * #노래
from TRIA_operatingsystem import * #운영체제
from TRIA_time import * #시간
from TRIA_weather import * #날씨
from TRIA_websurfing import * #웹검색

from Main_Command_cleanup import * #명령어 정리

print("The artificial intelligence Assistnt\nname'ENA'")

# 개인 신상정보
name = '정규'
location_1 = '대한민국' #국가
location_2 = '서울특별시' #특별시, 광역시, 특별자치시, 도, 특별자치도
location_2 = '노원구' #시, 군, 구
location_3 = '공릉2동' #읍, 면,

# 메인
def main():
    command = input("\n\n:") #"hello python"
    command_result_1 = command.split() #['hello', "python"]
    command_result_2 = list(command) #{'h', 'e', 'l', ... 'n']

    Main_Command_cleanup.Command_cleanup(command_result_2)

    for command_result_1[i] in len(command_result_1):
        pass

    for command_result_2[i] in len(command_result_2):
        if command_result_2[i] == '안' and command_result_2[i+1] == '녕':
            ENA_justchatting.hello_1(set_name,time)
        if command_result_2[i] == '반' and command_result_2[i + 1] == '가' and command_result_2[i + 2] == '워':

    main()

if __name__ == "__main__":
    main()
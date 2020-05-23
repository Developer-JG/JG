import time

from ENA_justchatting import * #일상대화
from ENA_music import * #노래
from ENA_operatingsystem import * #운영체제
from ENA_time import * #시간
from ENA_weather import * #날씨
from ENA_websurfing import * #웹검색

from Main_Command_cleanup import * #명령어 정리

print("The artificial intelligence Assistnt\nname'ENA'")

# 개인 신상정보
name = '정규'
Region_time = 9 #UTC(협정세계시) 기준 시간대

def time_set():
    if
    year = time.gmtime(time.time()).tm_year + Region_time
    mon = time.gmtime(time.time()).tm_mon + Region_time
    mday = time.gmtime(time.time()).tm_mday + Region_time
    hour = time.gmtime(time.time()).tm_hour + Region_time
    min = time.gmtime(time.time()).tm_min + Region_time
    sec = time.gmtime(time.time()).tm_sec + Region_time
    wday = time.gmtime(time.time()).tm_wday + Region_time #0~6 (0:월요일)

# 메인
def main():
    command = input("\n\n:") #"hello python"
    command_result_1 = command.split() #['hello', "python"]
    command_result_2 = list(command) #{'h', 'e', 'l', ... 'n']

    time_set()
    Main_Command_cleanup.Command_cleanup(command_result_2)

    #for command_result_1[i] in len(command_result_1):
        #if command_result_1[i] ==

    for command_result_2[i] in len(command_result_2):
        if command_result_2[i] == '안' and command_result_2[i+1] == '녕':
            ENA_justchatting.hello_1(set_name,time)
        if command_result_2[i] == '반' and command_result_2[i + 1] == '가' and command_result_2[i + 2] == '워':

    main()

if __name__ == "__main__":
    main()
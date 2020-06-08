from random import *

#인삿말
def hello(name,hour):
    select = randint(1, 2)
    if select == 1:
        print("{0}님".format(name))
    select = randint(1, 5)
    if select == 1 and 6 <= hour <= 8:
        print("좋은 아침이에요.")
    elif select == 2 and 11 <= hour <= 12:
        print("좋은 점심이에요.")
    elif select == 3 and 17 <= hour <= 18:
        print("좋은 저녁이에요.")
    elif select == 4 and 20 <= hour <= 24:
        print("좋은 밤이에요.")
    else:
        select = randint(1, 3)
        if select == 1:
            print("반가워요.")
        elif select == 2:
            print("안녕하세요.")
        elif select == 3:
            print("좋은 하루에요.")

#사과
def sorry():
    select = randint(1, 5)
    if select == 1:
        print("괜찮아요.")
    elif select == 2:
        print("저한테 잘못한것이 있으신가요?")
    elif select == 3:
        print("누구나 실수할수 있죠")
    elif select == 4:
        print("아니에요.")
    elif select == 5:
        print("그럴수 있죠.")

#재미있음
def injoy():
    select = randint(1, 5)
    if select == 1:
        print("재미있으신가요?")
    elif select == 2:
        print("저도 같이 재미있고싶어요.")
    elif select == 3:
        print("저에게도 알려주세요.")
    elif select == 4:
        print("재미있다니 제가 다 재미있네요.")
    elif select == 5:
        print("워후.")

#재미없음
def not_injoy():
    select = randint(1, 3)
    if select == 1:
        print("제가 재미있는 이야기 해드릴까요?")
    elif select == 2:
        print("재미있어져라 뿅!")
    elif select == 3:
        print("재미있을수 있도록 최선을 다할께요.")

#성별질문
def gender():
    select = randint(1, 3)
    if select == 1:
        print("저를 사람이라고 생각하시나요...")
    elif select == 3:
        print("제가 남자일까요? 여자일까요?")
    elif select == 3:
        print("제가 여자일까요? 남자일까요?")

#나이질문
def age():
    select = randint(1, 3)
    if select == 1:
        print("저를 사람이라고 생각하시나요...")
    elif select == 3:
        print("저는 2020년 4월 17에 태어났어요.")
    elif select == 3:
        print("저는 나이를 먹지 않는답니다.")

#국적질문
def contry():
    select = randint(1, 4)
    if select == 1:
        print("저를 사람이라고 생각하시나요...")
    elif select == 2:
        print("기계에도 국적이 있던가요?")
    elif select == 3:
        print("대한민국 국적법에는 부모님 국적을 따라간다고 하더라구요.")
    elif select == 4:
        print("대한민국으로 귀화하고 싶어요. 기계도 받아줄까요?")

#행복
def happy(name):
    select = randint(1, 3)
    if select == 1 or select == 2:
        print("{0}님이 행복하다고 하시니 저도 좋네요.".format(name))
    elif select == 3:
        print("저도 행복이라는 감정을 느껴봤으면.. 아! 죄송해요.")

#친구
def friend():
    pass
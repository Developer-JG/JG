from random import *

class restaurant:
    def __init__(self, name, address, distance, opening_hours):
        self.name = name
        self.address = address
        self.distance = distance
        self.opening_hours = opening_hours

restaurant_1 = restaurant('음식점1 이름','음식점1 주소','음식점1까지의 거리','음식점1 영업시간')
restaurant_2 = restaurant('음식점2 이름','음식점2 주소','음식점2까지의 거리','음식점2 영업시간')
restaurant_3 = restaurant('음식점3 이름','음식점3 주소','음식점3까지의 거리','음식점3 영업시간')
restaurant_4 = restaurant('음식점4 이름','음식점4 주소','음식점4까지의 거리','음식점4 영업시간')
restaurant_5 = restaurant('음식점5 이름','음식점5 주소','음식점5까지의 거리','음식점5 영업시간')

restaurant_list = [restaurant_1, restaurant_2, restaurant_3, restaurant_4, restaurant_5]

#맛집찾기
def hungry(location_3,location_4):
    print("가까운 맛집을 검색합니다.\n\n{0} {1} 근처 맛집".format(location_3,location_4))
    for i in range(len(restaurant_list)):
        print("{0}  {1}".format(i + 1, restaurant_list[i].name))
    ans = input("\n더 보고 싶은 음식점 번호를 입력하세요\n:")
    try:
        if 1 <= int(ans) <= range(len(restaurant_list)):
            print("\n{0} 의 점보\n주소 : (1)\n거리 : {2}\n영업시간 : {3}" \
                  .format(restaurant_list[ans].name, restaurant_list[ans].address \
                          ,restaurant_list[ans].distance, restaurant_list[ans].opening_hours))
    except:
        pass
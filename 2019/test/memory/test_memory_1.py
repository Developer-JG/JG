import pickle

class player:
    def __init__(self, name, equipment, inven, health, money, damage, defense, hunger, liv, exp):
        self.name = name
        self.equipment = {"atk" : ["없음"], "def" : ["없음"]}
        self.inven = {"atk" : [], "def" : [], "re" : [], "food" : [], "drop" : [], "item" : []}
        self.health = health
        self.damage = damage
        self.money = money
        self.defense = defense
        self.hunger = hunger
        self.liv = liv
        self.exp = exp

    # 현재 상태 확인
    def showinfo(self):
        print("{0:=^25}".format("현재 상태"))
        if len(self.equipment['atk']) == 2 and len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        elif len(self.equipment['atk']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][1].name}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
        elif len(self.equipment['def']) == 2:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][1].name} \n레벨 : {self.liv}")
        else:
            print(f"이름 : {self.name}\n체력 : {self.health}\n돈 : {self.money} \n공격력 : {self.damage} \
                    \n방어력 : {self.defense}\n허기 : {self.hunger} \
                    \n무기 : {self.equipment['atk'][0]}\n갑옷 : {self.equipment['def'][0]} \n레벨 : {self.liv}")
p_1 = player(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
self = p_1
        
with open("test",'rb') as f:
    self.name = pickle.load(f)
    self.equipment["atk"] = pickle.load(f)
    self.equipment["def"] = pickle.load(f)
    self.inven["atk"] = pickle.load(f)
    self.inven["def"] = pickle.load(f)
    self.inven["re"] = pickle.load(f)
    self.inven["food"] = pickle.load(f)
    self.inven["drop"] = pickle.load(f)
    self.inven["item"] = pickle.load(f)
    self.health = pickle.load(f)
    self.damage = pickle.load(f)
    self.money = pickle.load(f)
    self.defense = pickle.load(f)
    self.hunger= pickle.load(f)
    self.liv = pickle.load(f)
    self.exp = pickle.load(f)

p_1.showinfo()

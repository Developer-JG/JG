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

p_1 = player("in_name", [], [], 100, 10, 0, 0, 10, 1, 0)
self = p_1

with open("test",'wb') as f:
    pickle.dump(self.name,f)
    pickle.dump(self.equipment["atk"],f)
    pickle.dump(self.equipment["def"],f)
    pickle.dump(self.inven["atk"],f)
    pickle.dump(self.inven["def"],f)
    pickle.dump(self.inven["re"],f)
    pickle.dump(self.inven["food"],f)
    pickle.dump(self.inven["drop"],f)
    pickle.dump(self.inven["item"],f)
    pickle.dump(self.health,f)
    pickle.dump(self.damage,f)
    pickle.dump(self.money,f)
    pickle.dump(self.defense,f)
    pickle.dump(self.hunger,f)
    pickle.dump(self.liv,f)
    pickle.dump(self.exp,f)

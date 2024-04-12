class Characters():
    def __init__(self,name,hp,attack,defense,lvl,race):
        self.hp = hp
        self.name = name
        self.attack = attack
        self.defense = defense
        self.lvl = lvl
        self.race = race

    def imprime(self):
        print(f"Name = {self.name} | race = {self.race} | HP {self.hp} | attack {self.attack} | defense {self.defense}!")

barb = Characters("Zork Juarez","20","4","3","0","human")
monster = Characters("Monster Wandeley","10","6","4","1","realtor")
slime = Characters("Slime","6","5","1","2","Slime")


barb.imprime()
monster.imprime()
slime.imprime()
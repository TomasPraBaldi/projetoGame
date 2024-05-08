#====================================================================
#   SPELLS IDEAS
# destroi a de baixo mas cria um bloco
# enquanto a carta ta no grid quem jogou ganha um buff ate ela sair
# equipamento que adiciona coisa pra alguma carta
#====================================================================

import random

print('Welcome to the connect four unleashed!')

class Cards():
    def __init__(self,name,hp,attack,description):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.description = description

    def imprime(self):
        print(f"Name = {self.name} | HP {self.hp} | attack {self.attack}")
    
    def vida(self):
        if self.hp == 0:
            pass # local da carta fica vazio !!!!ARRUMAR!!!!
    
    def spells_self_attack(self):
        self.hp - self.attack


player1_hand = []
player2_hand = []

assassin = Cards("Assassin","1","1", "Deals one damage to the adjacent card below.")
knight = Cards("Knight","2","0", "Defends 2 damage from above.")
peaseant = Cards("Peaseant","1","0", "Just trying to live his life in peace.")

lightning = Cards("Lightning","1","10", "Kill cards from the chosen column" ) # pensei em dar o dano da spell nela mesma para matar a carta spell
volcano = Cards("Volcano","1","10","Kill adjacent cards" )
earthquake = Cards("Earthquake","1","10", "Kill diagonals cards" )


basic_cards = [peaseant, assassin, knight]
spell_cards = [lightning, volcano, earthquake]

# giving cards

player1_hand.append(random.choice(basic_cards))
player1_hand.append(random.choice(basic_cards))
player1_hand.append(random.choice(basic_cards))

player2_hand.append(random.choice(basic_cards))
player2_hand.append(random.choice(basic_cards))
player2_hand.append(random.choice(basic_cards))

# creating the grid

grid = [['_' for x in range(7)] for _ in range(7)]
for l in grid:
    print(l)




p1_chosen_card = input("Player 1 - wich card you want to place?")
p1_column = int(input("Player 1 - wich column you want to place your card?"))
p1_row = int(input("Player 1 - wich row you want to place your card?"))

grid[p1_column - 1][p1_row - 1] = p1_chosen_card

for l in grid:
    print(l)
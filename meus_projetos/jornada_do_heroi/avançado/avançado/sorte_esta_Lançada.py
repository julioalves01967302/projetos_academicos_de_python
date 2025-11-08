import random

class Dado:
    def __init__(self, lados=6):

        self.lados = lados

    def rolar(self):
    
        return random.randint(1, self.lados)


d6 = Dado()  
d20 = Dado(20)    

print("🎲 Rolando um D6:", d6.rolar())
print("🎲 Rolando um D20:", d20.rolar())

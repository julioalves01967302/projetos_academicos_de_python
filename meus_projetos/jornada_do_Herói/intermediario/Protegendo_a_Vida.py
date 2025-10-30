class personagem:
    def __init__(self,nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
    def vida(self):
        return self.vida
    def vida(self,novo_valor):
        if novo_valor <0:
            self.vida=0
        else :
            self.vida = novo_valor   

heroi =personagem("Julio", 100, 20)
print(heroi.vida)  

heroi.vida -= 120
print(heroi.vida)   

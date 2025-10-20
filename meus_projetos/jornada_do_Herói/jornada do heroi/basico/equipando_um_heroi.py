class arma:
    def __init__(self,nome,dano):
        self.nome=nome
        self.dano=dano

class Guerreiro:
    def __init__(self,nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
        self.arma=None

    def equipar_arma(self,arma):
        self.arma=arma
        print(f"{self.nome} equipou a arma: {arma.nome}!") 

espada_longa= arma('espada longa',30) 
Julio= Guerreiro ('Julio',100,19)   
Julio.equipar_arma(espada_longa)
                
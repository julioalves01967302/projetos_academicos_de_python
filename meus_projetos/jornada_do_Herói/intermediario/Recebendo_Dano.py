class personagem:
    def __init__(self,nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
    def vida(self):
        return self.vida
    def vida (self,novo_valor):
        if novo_valor <0:
            self.vida=0  
        else:
            self.vida=novo_valor
    def receber_dano(self,dano):
        self.vida -= dano
        print(f'{self.nome} recebeu {dano} de dano! vida restante: {self.vida}')  
gerreiro=personagem("Julio",500,600)
gerreiro.receber_dano(50)
gerreiro.receber_dano(90)         
            
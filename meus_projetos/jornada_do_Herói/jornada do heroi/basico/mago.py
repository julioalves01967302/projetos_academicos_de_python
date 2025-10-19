class mago:
    def __init__(self, nome,pontos_de_vida,fonte_de_ataque,poder_magico):
        self.nome=nome
        self.vida=pontos_de_vida
        self.ataque=fonte_de_ataque
        self.poder_magico=poder_magico

mago1=mago('harry',500,120,600)
print(f'nome do mago {mago1.nome}')

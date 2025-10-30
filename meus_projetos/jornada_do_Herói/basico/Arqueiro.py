class arqueiro:
    def __init__(self, nome,pontos_de_vida,fonte_de_ataque,precisão):
        self.nome=nome
        self.vida=pontos_de_vida
        self.ataque=fonte_de_ataque
        self.precisão=precisão 

arqueiro1=arqueiro('arqueiro_verde',115,125,135)
print(f'nome do arqueiro : {arqueiro1.nome}')

class guerreiro:
    def __init__(self, nome,pontos_de_vida,fonte_de_ataque):
        self.nome=nome
        self.vida=pontos_de_vida
        self.ataque=fonte_de_ataque

guerreiro1=guerreiro('julio',100,19)
print(f'nome do guerreiro: {guerreiro1.nome}\n vida: {guerreiro1.vida} \n ataque: {guerreiro1.ataque}')
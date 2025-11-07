class primeiro_inimigo:
    def __init__(self, nome,pontos_de_vida,fonte_de_ataque):
        self.nome=nome
        self.vida=pontos_de_vida
        self.ataque=fonte_de_ataque

goblin=primeiro_inimigo('cratos',500,200)        
print(f'o primeiro desafio: {goblin.nome}\n vida: {goblin.vida}\n ataque: {goblin.ataque}')        
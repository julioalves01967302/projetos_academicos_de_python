class Guerreiro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

class PrimeiroInimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

def atacar(quem_ataca, alvo):
    print(f"{quem_ataca.nome} atacou {alvo.nome} causando {quem_ataca.ataque} de dano!")


guerreiro1 = Guerreiro("Julio", 100, 500)
goblin = PrimeiroInimigo("Cratos", 500, 200)

atacar(guerreiro1, goblin)
atacar(goblin, guerreiro1)

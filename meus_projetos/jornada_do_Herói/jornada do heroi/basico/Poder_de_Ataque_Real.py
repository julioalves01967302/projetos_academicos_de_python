class Arma:
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano


class Guerreiro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.arma = None

    def equipar(self, arma):
        self.arma = arma
        print(f"{self.nome} equipou a arma: {arma.nome}!")

    def atacar(self, inimigo):
        dano = self.ataque + (self.arma.dano if self.arma else 0)
        print(f"{self.nome} atacou {inimigo.nome} causando {dano} de dano!")


class Inimigo:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

espada = Arma("Espada Longa", 25)
julio = Guerreiro("Julio", 100, 19)
goblin = Inimigo("Cratos", 500, 200)

julio.equipar(espada)
julio.atacar(goblin)

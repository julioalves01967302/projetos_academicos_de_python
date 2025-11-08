import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")


class Monstro:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome} causando {self.ataque} de dano!")
        alvo.receber_dano(self.ataque)

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")


class Orc(Monstro):
    def atacar(self, alvo):
        chance_critico = random.random()
        dano = self.ataque

        if chance_critico <= 0.3:
            dano *= 2
            print(f"💥 {self.nome} desferiu um GOLPE CRÍTICO! Causou {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

        alvo.receber_dano(dano)



heroi = Personagem("Meliodas", 100, 25)
orc = Orc("Orc Guerreiro", 150, 30)

print("\n--- Batalha contra o ORC ---")
orc.atacar(heroi)
orc.atacar(heroi)
orc.atacar(heroi)

import random

class Dado:
    def __init__(self, lados=6):
        self.lados = lados

    def rolar(self):
        return random.randint(1, self.lados)


class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        dado = Dado(6)
        sorte = dado.rolar()
        dano = self.ataque + (sorte - 3)
        dano = max(0, dano)

        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano! (Rolou {sorte} no dado)")

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")


heroi = Personagem("Meliodas", 100, 20)
inimigo = Personagem("Cratos", 120, 15)

print("\n--- Batalha com Fator Sorte ---")
heroi.atacar(inimigo)
inimigo.atacar(heroi)

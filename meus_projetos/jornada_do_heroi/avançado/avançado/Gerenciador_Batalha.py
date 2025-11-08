import random

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, alvo):
        dano = self.ataque
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
        alvo.receber_dano(dano)

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")


class Orc(Personagem):
    def atacar(self, alvo):
        chance_critico = random.random()
        dano = self.ataque

        if chance_critico <= 0.3:
            dano *= 2
            print(f"💥 {self.nome} desferiu um GOLPE CRÍTICO! Causou {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

        alvo.receber_dano(dano)



class Batalha:
    def __init__(self, combatente1, combatente2):
        self.combatente1 = combatente1
        self.combatente2 = combatente2

    def iniciar(self):
        print(f"\n🏁 A batalha começou entre {self.combatente1.nome} e {self.combatente2.nome}!\n")

        while self.combatente1.vida > 0 and self.combatente2.vida > 0:
            self.combatente1.atacar(self.combatente2)
            if self.combatente2.vida <= 0:
                print(f"\n🏆 {self.combatente1.nome} venceu a batalha!")
                break

            self.combatente2.atacar(self.combatente1)
            if self.combatente1.vida <= 0:
                print(f"\n🏆 {self.combatente2.nome} venceu a batalha!")
                break



heroi = Personagem("Meliodas", 100, 20)
orc = Orc("Orc Guerreiro", 150, 25)

batalha = Batalha(heroi, orc)
batalha.iniciar()

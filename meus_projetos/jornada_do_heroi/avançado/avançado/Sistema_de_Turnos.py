import random
from abc import ABC, abstractmethod


class Dado:
    @staticmethod
    def rolar(lados=6):
        return random.randint(1, lados)


class Habilidade(ABC):
    def __init__(self, nome):
        self.nome = nome

    @abstractmethod
    def usar(self, usuario, alvo):
        pass


class AtaqueForte(Habilidade):
    def __init__(self):
        super().__init__("Ataque Forte")

    def usar(self, usuario, alvo):
        dado = Dado.rolar(6)
        dano = usuario.ataque * 2 + dado
        alvo.receber_dano(dano)
        print(f"{usuario.nome} usou {self.nome} e causou {dano} de dano em {alvo.nome}!")

class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__("Bola de Fogo")

    def usar(self, usuario, alvo):
        dado = Dado.rolar(10)
        dano = usuario.ataque + dado + 10
        alvo.receber_dano(dano)
        print(f"{usuario.nome} lançou {self.nome} e causou {dano} de dano em {alvo.nome}!")

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.habilidades = []

    def esta_vivo(self):
        return self.vida > 0

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano. Vida atual: {self.vida}")

    def aprender_habilidade(self, habilidade):
        self.habilidades.append(habilidade)
        print(f"{self.nome} aprendeu a habilidade: {habilidade.nome}")

    def usar_habilidade(self, indice, alvo):
        if indice < len(self.habilidades):
            habilidade = self.habilidades[indice]
            habilidade.usar(self, alvo)
        else:
            print(f"{self.nome} tentou usar uma habilidade inexistente!")


class Orc(Personagem):
    def atacar(self, alvo):
        critico = random.random() < 0.3 
        dano = self.ataque * (2 if critico else 1)
        alvo.receber_dano(dano)
        if critico:
            print(f"💥 {self.nome} desferiu um GOLPE CRÍTICO em {alvo.nome} causando {dano} de dano!")
        else:
            print(f"{self.nome} atacou {alvo.nome}, causando {dano} de dano.")

class Batalha:
    def __init__(self, combatente1, combatente2):
        self.combatente1 = combatente1
        self.combatente2 = combatente2

    def iniciar(self):
        print(f"\n🏁 A batalha entre {self.combatente1.nome} e {self.combatente2.nome} começou!\n")

        turno = 1
        while self.combatente1.esta_vivo() and self.combatente2.esta_vivo():
            print(f"\n🔄 --- Turno {turno} ---")


            print(f"\n👉 {self.combatente1.nome} ataca!")
            self.combatente1.usar_habilidade(0, self.combatente2)

            if not self.combatente2.esta_vivo():
                print(f"\n💀 {self.combatente2.nome} foi derrotado! {self.combatente1.nome} venceu!")
                break

            print(f"\n⚔️ {self.combatente2.nome} contra-ataca!")
            if isinstance(self.combatente2, Orc):
                self.combatente2.atacar(self.combatente1)
            else:
                self.combatente2.usar_habilidade(0, self.combatente1)

            if not self.combatente1.esta_vivo():
                print(f"\n💀 {self.combatente1.nome} foi derrotado! {self.combatente2.nome} venceu!")
                break

            turno += 1


heroi = Personagem("Meliodas", 150, 40)
heroi.aprender_habilidade(AtaqueForte())

orc = Orc("Orc Guerreiro", 180, 35)

batalha = Batalha(heroi, orc)
batalha.iniciar()

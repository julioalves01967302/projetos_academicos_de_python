class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self._vida = vida
        self.ataque = ataque

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"⚔️ {self.nome} recebeu {dano} de dano! Vida: {self._vida}")

    def mostrar_status(self):
        print(f"👤 {self.nome} | ❤️ Vida: {self._vida}")



class Monstro(Personagem):
    def __init__(self, nome, vida, ataque):
        super().__init__(nome, vida, ataque)


    @classmethod
    def goblin_padrao(cls):
        return cls("Goblin", 300, 325)  


g1 = Monstro.goblin_padrao()
g2 = Monstro.goblin_padrao()
g3 = Monstro.goblin_padrao()

g1.mostrar_status()
g2.mostrar_status()
g3.mostrar_status()

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

    def atacar(self, alvo):
        print(f"{self.nome} atacou {alvo.nome} causando {self.ataque} de dano!")
        alvo.receber_dano(self.ataque)



class Guerreiro(Personagem):
    def atacar(self, alvo):
        print(f"🗡️ {self.nome} atacou com sua espada causando {self.ataque} de dano!")
        alvo.receber_dano(self.ataque)



class Mago(Personagem):
    def atacar(self, alvo):
        print(f"✨ {self.nome} lançou uma magia em {alvo.nome}, causando {self.ataque} de dano mágico!")
        alvo.receber_dano(self.ataque)



class Arqueiro(Personagem):
    def atacar(self, alvo):
        print(f"🏹 {self.nome} disparou uma flecha com precisão em {alvo.nome}, causando {self.ataque} de dano!")
        alvo.receber_dano(self.ataque)



guerreiro = Guerreiro("meliodas", 100, 115)
mago = Mago("harry", 125, 135)
arqueiro = Arqueiro("arqueiro_verde", 115, 125)

inimigo = Personagem("cratos", 300, 325)

guerreiro.atacar(inimigo)
mago.atacar(inimigo)
arqueiro.atacar(inimigo)

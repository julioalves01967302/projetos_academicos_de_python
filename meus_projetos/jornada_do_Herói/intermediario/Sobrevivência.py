class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self._vida = vida 

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self._vida}")

    def esta_vivo(self):
        """
        Retorna True se o personagem ainda está com vida acima de 0.
        Retorna False se estiver com 0 (derrotado).
        """
        return self._vida > 0


class Monstro(Personagem):
    pass


guerreiro = Personagem("Meliodas", 100)
goblin = Monstro("Goblin", 50)

guerreiro.receber_dano(30)
print(guerreiro.esta_vivo())

goblin.receber_dano(60)
print(goblin.esta_vivo()) 

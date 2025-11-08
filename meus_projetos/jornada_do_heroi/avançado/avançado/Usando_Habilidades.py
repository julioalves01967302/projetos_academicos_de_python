class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.habilidades = []

    def receber_dano(self, dano):
        self.vida = max(0, self.vida - dano)
        print(f"{self.nome} recebeu {dano} de dano! Vida atual: {self.vida}")

    def aprender_habilidade(self, habilidade):
        self.habilidades.append(habilidade)
        print(f"{self.nome} aprendeu a habilidade: {habilidade.nome}")

    def usar_habilidade(self, indice, alvo):
        if 0 <= indice < len(self.habilidades):
            habilidade = self.habilidades[indice]
            habilidade.usar(self, alvo)
        else:
            print("Essa habilidade não existe!")

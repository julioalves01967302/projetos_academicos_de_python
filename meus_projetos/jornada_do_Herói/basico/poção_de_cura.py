class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    def __str__(self):
        return f"{self.nome} (Cura: {self.cura})"


pocao_vida = Pocao("Poção de Vida", 100)


print(pocao_vida)

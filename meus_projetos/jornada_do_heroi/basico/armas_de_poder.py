
class Arma:
    def __init__(self, nome, poder):
        self.nome = nome          
        self.poder = poder        

    def __str__(self):
        return f"{self.nome} Dano: {self.poder}"


espada_longa = Arma("Espada Longa", 250)
cajado_magico = Arma("Cajado Mágico", 300)


print(espada_longa)
print(cajado_magico)

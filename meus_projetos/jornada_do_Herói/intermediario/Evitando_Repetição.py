class personagem:
    def __init__(self, nome,vida,ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque

    def atacar (self,alvo):
         print(f"{self.nome} atacou {alvo.nome} causando {self.ataque} de dano!")     
class gerreiro (personagem):
    pass
class  mago(personagem):
    def soltar_magia(self):
         print(f"{self.nome} lançou uma bola de fogo!")
class arqueiro(personagem):
    def mira_precisa(self):
         print(f"{self.nome} atirou na cabeça do inimigo!")        
julio=gerreiro('juilo',500,600)
Harry=mago('harry',550,722)

julio.atacar(Harry)
Harry.soltar_magia()
from abc import ABC, abstractmethod

class habilidades(ABC):
    def __init__(self, nome):
        self.nome=nome
    @abstractmethod    
    def usar(self, usuario, alvo):
        pass    
class AtaqueForte(habilidades):
    def __init__(self):
        super().__init__('ataque forte')

    def usar(self, usuario, alvo):
        dano = usuario.ataque * 2  
        alvo.receber_dano(dano)
        print(f"{usuario.nome} usou {self.nome} em {alvo.nome}, causando {dano} de dano!")

class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome=nome
        self.vida=vida
        self.ataque=ataque
        self.habilidades=[] 

    def receber_dano(self, dano):
        self._vida = max(0,self.vida - dano)          
        print(f'{self.nome} recebeu {dano} de dano!  vida atual:{self._vida}') 

    def aprender_habilidade(self, habilidade):
        self.habilidades.append(habilidade)  
        print(f'{self.nome} aprendeu a haabilidade: {habilidade.nome}')  

    def usar_habilidade(self,indice,alvo):
        if indice < len(self.habilidades):
            habilidade = self.habilidades[indice]
            habilidade.usar(self, alvo)

        else:
            print('essa habilidade não existe!') 


heroi = Personagem("Meliodas", 100, 115)
inimigo = Personagem("Demônio_goblin", 120, 112)

ataque_forte = AtaqueForte()

heroi.aprender_habilidade(ataque_forte)

print("\n--- Habilidades do Herói ---")
for i, habilidade in enumerate(heroi.habilidades):
    print(f"{i} - {habilidade.nome}")

print("\n--- Batalha ---")
heroi.usar_habilidade(0, inimigo)

print(f"\nVida do inimigo após o ataque: {inimigo.vida}")

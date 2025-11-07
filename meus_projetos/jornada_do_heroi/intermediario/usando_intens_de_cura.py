class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"✅ Item '{item}' foi adicionado ao inventário.")

    def mostrar_itens(self):
        if not self.itens:
            print("📦 O inventário está vazio.")
        else:
            print("🎒 Inventário:")
            for item in self.itens:
                print(f"- {item}")

class Pocao:
    def __init__(self, nome, cura):
        self.nome = nome
        self.cura = cura

    def __str__(self):
        return f"{self.nome} (+{self.cura} vida)"


class Personagem:
    def __init__(self, nome, vida_maxima):
        self.nome = nome
        self._vida = vida_maxima       
        self._vida_maxima = vida_maxima 
        self.inventario = Inventario()  

    def mostrar_status(self):
        print(f"👤 {self.nome} | ❤️ Vida: {self._vida}/{self._vida_maxima}")

    def receber_dano(self, dano):
        self._vida -= dano
        if self._vida < 0:
            self._vida = 0
        print(f"⚔️ {self.nome} recebeu {dano} de dano! Vida agora: {self._vida}/{self._vida_maxima}")

    def usar_pocao(self):
        for item in self.inventario.itens:
            if isinstance(item, Pocao):  
                vida_antes = self._vida
                self._vida = min(self._vida + item.cura, self._vida_maxima) 
                self.inventario.itens.remove(item)  
                print(f"🧪 {self.nome} usou {item.nome} e curou {self._vida - vida_antes} de vida!")
                return
        print("❌ Nenhuma poção disponível no inventário!")


heroi = Personagem("meliodas", 100)

pocao_vida = Pocao("Poção de Vida", 30)

heroi.inventario.adicionar_item(pocao_vida)

heroi.mostrar_status()

heroi.receber_dano(50)

heroi.usar_pocao()

heroi.mostrar_status()

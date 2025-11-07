class Inventario:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)
        print(f"✅ Item '{item}' foi adicionado ao inventário.")

    def remover_item(self, item):
        if item in self.itens:
            self.itens.remove(item)
            print(f"❌ Item '{item}' foi removido do inventário.")
        else:
            print(f"⚠️ Item '{item}' não está no inventário.")

    def mostrar_itens(self):
        if not self.itens:
            print("📦 O inventário está vazio.")
        else:
            print("🎒 Itens no inventário:")
            for item in self.itens:
                print(f"- {item}")

class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome        
        self._vida = vida       
        self.inventario = Inventario() 

    def mostrar_status(self):
        print(f"👤 Nome: {self.nome} | ❤️ Vida: {self._vida}")



heroi = Personagem("Arthur", 100)

heroi.mostrar_status()

heroi.inventario.adicionar_item("Espada Longa")
heroi.inventario.adicionar_item("Poção de Vida")

heroi.inventario.mostrar_itens()

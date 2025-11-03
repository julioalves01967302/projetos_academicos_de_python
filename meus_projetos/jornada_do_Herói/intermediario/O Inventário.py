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
            print(f"⚠️ Item '{item}' não existe no inventário.")

    def mostrar_itens(self):
        if not self.itens:
            print("📦 O inventário está vazio.")
        else:
            print("🎒 Itens no inventário:")
            for item in self.itens:
                print(f"- {item}")
meu_inventario = Inventario()

meu_inventario.adicionar_item("Espada de Ferro")
meu_inventario.adicionar_item("Poção de Vida")
meu_inventario.adicionar_item("Arco Longo")

meu_inventario.mostrar_itens()

meu_inventario.remover_item("Poção de Vida")

meu_inventario.mostrar_itens()


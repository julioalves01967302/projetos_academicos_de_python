class Batalha:
    def __init__(self, combatente1, combatente2):
        self.combatente1 = combatente1
        self.combatente2 = combatente2

    def iniciar(self):
        print(f"\n🏁 A batalha entre {self.combatente1.nome} e {self.combatente2.nome} começou!\n")

        turno = 1
        while self.combatente1.esta_vivo() and self.combatente2.esta_vivo():
            print(f"\n--- Turno {turno} ---")

           
            print(f"\n👉 {self.combatente1.nome} ataca!")
            self.combatente1.usar_habilidade(0, self.combatente2)

            if not self.combatente2.esta_vivo():
                break

            print(f"\n⚔️ {self.combatente2.nome} ataca!")
            self.combatente2.usar_habilidade(0, self.combatente1)

            turno += 1


        if self.combatente1.esta_vivo():
            print(f"\n🏆 {self.combatente1.nome} venceu a batalha!")
        elif self.combatente2.esta_vivo():
            print(f"\n🏆 {self.combatente2.nome} venceu a batalha!")
        else:
            print("\n🤝 Ambos foram derrotados — empate!")

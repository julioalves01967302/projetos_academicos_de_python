class Batalha:
    def __init__(self, equipe1, equipe2):
        self.equipe1 = equipe1
        self.equipe2 = equipe2

    def equipe_viva(self, equipe):
       
        return any(personagem.esta_vivo() for personagem in equipe)

    def iniciar(self):
        print("\n🏁 A batalha entre as duas equipes começou!\n")

        turno = 1
        while self.equipe_viva(self.equipe1) and self.equipe_viva(self.equipe2):
            print(f"\n--- Turno {turno} ---")

            
            for heroi in self.equipe1:
                if heroi.esta_vivo():
                    alvo = next((m for m in self.equipe2 if m.esta_vivo()), None)
                    if alvo:
                        heroi.usar_habilidade(0, alvo)

            
            for monstro in self.equipe2:
                if monstro.esta_vivo():
                    alvo = next((h for h in self.equipe1 if h.esta_vivo()), None)
                    if alvo:
                        monstro.usar_habilidade(0, alvo)

            turno += 1

        
        if self.equipe_viva(self.equipe1):
            print("\n🏆 A equipe 1 venceu a batalha!")
        elif self.equipe_viva(self.equipe2):
            print("\n🏆 A equipe 2 venceu a batalha!")
        else:
            print("\n🤝 Ambas as equipes foram derrotadas — empate!")

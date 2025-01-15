class Bok:
    def __init__(self, titel, författare, utlånad=False):
        self.titel = titel
        self.författare = författare
        self.utlånad = utlånad

    def läs(self):
        print("Du läser", self.titel)

    def __str__(self):
        status = "utlånad" if self.utlånad else "tillgänglig"
        return f"Boken {self.titel}, skriven av {self.författare}, är {status}."


class Bibliotek:
    def __init__(self, bookList):
        self.books = bookList

    def spara(self, filename):
        with open(filename, "w") as f:
            for bok in self.books:
                f.write(f"{bok.titel},{bok.författare},{int(bok.utlånad)}\n")

    def hittaTitel(self, titel):
        for bok in self.books:
            if bok.titel.lower() == titel.lower():
                return bok
        return None

    def hittaFörfattare(self, författare):
        return [bok for bok in self.books if bok.författare.lower() == författare.lower()]

    def lånaBok(self, titel):
        bok = self.hittaTitel(titel)
        if bok and not bok.utlånad:
            bok.utlånad = True
            print(f"Boken {bok.titel} är nu utlånad.")
        else:
            print("Boken är antingen inte tillgänglig eller redan utlånad.")

    def lämnaTillbaka(self, titel):
        bok = self.hittaTitel(titel)
        if bok and bok.utlånad:
            bok.utlånad = False
            print(f"Boken {bok.titel} har återlämnats.")
        else:
            print("Boken är inte utlånad.")

    def läggTill(self, bok):
        self.books.append(bok)
        print(f"Boken {bok.titel} har lagts till i biblioteket.")

    def taBort(self, titel):
        bok = self.hittaTitel(titel)
        if bok:
            self.books.remove(bok)
            print(f"Boken {bok.titel} har tagits bort från biblioteket.")
        else:
            print("Boken finns inte i biblioteket.")

    def listaBöcker(self):
        if self.books:
            print("Lista över alla böcker i biblioteket:")
            for bok in self.books:
                print(bok)
        else:
            print("Inga böcker finns i biblioteket.")

    def sorteraBöcker(self):
        self.books.sort(key=lambda bok: bok.titel)
        print("Böckerna har sorterats.")


# Funktioner för menyvalen
def sökTitel(bibliotek):
    titel = input("Ange titeln på boken du söker efter: ")
    bok = bibliotek.hittaTitel(titel)
    if bok:
        print(f"Bok hittad: {bok}")
    else:
        print("Boken kunde inte hittas.")

def sökFörfattare(bibliotek):
    författare = input("Ange författaren du söker efter: ")
    böcker = bibliotek.hittaFörfattare(författare)
    if böcker:
        print(f"Böcker av {författare}:")
        for bok in böcker:
            print(bok)
    else:
        print("Inga böcker av denna författare hittades.")

def lånaBok(bibliotek):
    titel = input("Ange titeln på boken du vill låna: ")
    bibliotek.lånaBok(titel)

def återlämnaBok(bibliotek):
    titel = input("Ange titeln på boken du vill återlämna: ")
    bibliotek.lämnaTillbaka(titel)

def läggTillBok(bibliotek):
    titel = input("Ange titeln på den nya boken: ")
    författare = input("Ange författaren på den nya boken: ")
    bok = Bok(titel, författare)
    bibliotek.läggTill(bok)
    bibliotek.spara("biblotek.txt")  # Spara till fil efter att en bok lagts till

def taBortBok(bibliotek):
    titel = input("Ange titeln på boken du vill ta bort: ")
    bibliotek.taBort(titel)
    bibliotek.spara("biblotek.txt")  # Spara till fil efter att en bok tagits bort

def listaBöcker(bibliotek):
    bibliotek.listaBöcker()

def sorteraBöcker(bibliotek):
    bibliotek.sorteraBöcker()
    bibliotek.spara("biblotek.txt")  # Spara till fil efter att böckerna sorterats

def avsluta(bibliotek):
    print("Programmet avslutas.")
    exit()


# Läs in böcker från fil och skapa Bibliotek
def läsBöckerFrånFil(filename):
    with open(filename, "r") as f:
        bok_data = f.read().splitlines()
    böcker = []
    for rad in bok_data:
        titel, författare, utlånad = rad.split(",")
        böcker.append(Bok(titel.strip(), författare.strip(), bool(int(utlånad.strip()))))
    return böcker


# Huvudprogram
def main():
    böcker = läsBöckerFrånFil("biblotek.txt")
    bibliotek = Bibliotek(böcker)

    menyVal = ""
    while menyVal != "q":
        print("""
                                   .--.                   .---.
                               .---|__|           .-.     |~~~|
                            .--|===|--|_          |_|     |~~~|--.--.
                            |  |===|  |'\     .---!~|  .--|   |--|--|
                            |%%|   |  |.'\    |===| |--|%%|   |  |  |
                            |%%|   |  |\.'\   |   | |__|  |   |  |  |
                            |B | I |B | \L \  |=I=|O|T=|E | K |E |T |
                            |  |   |__|  \.'\ |   |_|__|  |~~~|__|__|
                            |  |===|--|   \.'\|===|~|--|%%|~~~|--|--|
                            ^--^---'--^    `-'`---^-^--^--^---'--'--'
""")

        print("""
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:
            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            5. Lägg till ny bok                                 6. Ta bort bok
            7. Lista alla böcker                                8. Sortera böcker
            q. Avsluta
        """)
        
        menyVal = input("Välj ett alternativ: ")

        if menyVal == "1":
            sökTitel(bibliotek)
        elif menyVal == "2":
            sökFörfattare(bibliotek)
        elif menyVal == "3":
            lånaBok(bibliotek)
        elif menyVal == "4":
            återlämnaBok(bibliotek)
        elif menyVal == "5":
            läggTillBok(bibliotek)
        elif menyVal == "6":
            taBortBok(bibliotek)
        elif menyVal == "7":
            listaBöcker(bibliotek)
        elif menyVal == "8":
            sorteraBöcker(bibliotek)
        elif menyVal == "q":
            avsluta(bibliotek)
        else:
            print("Pogiltigt val, försök igen!")


# Kör programmet
if __name__ == "__main__":
    main()

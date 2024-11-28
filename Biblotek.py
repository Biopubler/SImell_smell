# ------------------------------- Information --------------------------------- #


f = open("biblioteket.txt", "rt")
data = f.read()
data = data.splitlines()
posts = []
for d in data:
    post = d.split(",")
    posts.append(post)
print(posts)

#söka i datan
search = input("Sök något:")
for post in posts:
    for p in post:
        if search in p:
            print("Hittade sökresultat:")
            print("Författare:", post[1], ", Titel:", post[0])
            if post[2] == "0":
                print("Boken är utlånad")
            else:
                print("Boken är inte utlånad")
"""
Titel: Biblioteket
Författare:
Datum:
Det här är ett program för hantering av enklare biblioteksrutiner.
Programmet lagrar böckerna i en fil med namnet "bibliotek.txt" mellan körningarna.
"""
# ------------------------- Biblioteksimportering ----------------------------- #
import random as rand

# ---------------------------- Klassdefinitioner ------------------------------ #

class Bok:
    """ Bok är en klass som representerar en bok i biblioteket. Varje objekt
    som skapas ur klassen har en titel, författare och en variabel som håller
    reda på om boken är utlånad eller inte. """
    def __init__(self, författare, titel):
        self.titel = titel
        self.författare = författare
        self.utlånad = False
      

    # Strängrepresentation av objektet.
    def __str__(self):
        return f"Boken {self.titel}, skriven av {self.författare}."

class Bibliotek:
    """ Bibliotek är en klass som representerar en bibliotekskatalog. Ett objekt
    ur klassen har en lista över böcker som attribut, samt metoder för att
    modifiera katalogen. """
    def __init__(self, bookList):
        self.books = bookList

    # Sparar hela bibliotekskatalogen i en fil.
    def spara(self, filename):
        return

    # Söker på en titel.
    def hittaTitel(self, titel):
        return

    # Söker på en författare.
    def hittaFörfattare(self, författare):
        return

    # Lånar en bok.
    def lånaBok(self, bok):
        return

    # Återlämnar en bok.
    def lämnaTillbaka(self, bok):
        return

    # Lägger till en ny bok:
    def läggTill(self, bok):
        return

    # Tar bort en bok:
    def taBort(self, bok):
        return

    # Returnerar en lista över alla böcker:
    def listaBöcker(self):
        return

# ------------------------------ Huvudprogram --------------------------------- #
def main():
    menyVal = ""

    while menyVal != "q":

        print(
        """
                                          --- MENY ---
                Välkommen till biblioteks-simulatorn. Välj ett av alternativen nedan:
            1. Sök efter titel                                  2. Sök efter författare
            3. Låna bok                                         4. Återlämna bok
            4. Lägg till ny bok                                 5. Ta bort bok
            6. Ta bort bok                                      7. Lista alla böcker
            8. Sortera böcker                                   q. Avsluta
        ---------------------------------------------------------------------------------------
        """)

        menyVal = input("-> ")

        if menyVal == "1":
            pass
        elif menyVal == "2":
            pass
        elif menyVal == "3":
            pass
        elif menyVal == "4":
            pass
        elif menyVal == "5":
            pass
        elif menyVal == "6":
            pass
        elif menyVal == "7":
            pass
        elif menyVal == "8":
            pass

print(
"""
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

main() 
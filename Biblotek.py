#Förråd

varukorg = []
användare_förråd = []
bibliotek_förråd = []

# ------------------------------- Information --------------------------------- #



#söka i datan

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
    mitt_bibliotek = Bibliotek(["Emil i Lönneberga","Barnen i Bullerbyn","A tale of two cities"])
    
    menyVal = ""

    while menyVal != "q":

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

        menyVal = input("Sök -> ") 

        #Hittade lösningen på problemet med output.
        #Problemet var att när användaren skrev in Emil i Lönneberga så 
        #fick det booksheet att skriva ut print("Är tillgänglig. Boken är skriven av Astrid Lindgren") 
        #2 gånger.
        #Problemet åtgärdades genom att lägga till:(or booksheet ==) Min logik var för språk driven.
        


        if menyVal == "1":
            booksheet = input("Ange titeln som du vill söka efter: ") 
        if booksheet == "Emil i Lönneberga" or booksheet == "emil i lönneberga":
            print("Är tillgänglig. Boken är skriven av Astrid Lindgren")



        if booksheet == "Barnen i Bullerbyn" or booksheet == "Barnen i bullerbyn":
            print("Är tillgänglig. Boken är skriven av Astrid Lindgren")

     #Försök att implementera en text fil i koden den här veckan samt 
     #skapa koden som gör att vi kan få till en lista av alla böcker. 
     #Rad 17 till 75 kommer troligen att ha mycket att göra med att få till det.

        elif menyVal == "2":
            print(
            """
                                --- 2. Sök efter författare ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "3":
            print(
            """
                                --- 3. Låna bok ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "4":
            print(
            """
                                --- 4. Lägg till ny bok ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "5":
            print(
            """
                                --- 5. Ta bort bok ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "6":
            print(
            """
                                --- 6. Ta bort bok ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "7":
            print(
            """
                                --- 7. Lista alla böcker ---

        ------------------------------------------------------------------------------
            """)
            pass
        elif menyVal == "8":
            print(
            """
                                --- 8. Sortera böcker ---

        ------------------------------------------------------------------------------
            """)
            pass



main() 

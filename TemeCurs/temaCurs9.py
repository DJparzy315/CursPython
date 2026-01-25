class Carte:
    def __init__(self, titlu, autor, isbn):
        self.titlu = titlu
        self.autor = autor
        self.isbn = isbn
        self.este_imprumutata = False


class MembruBiblioteca:
    def __init__(self, nume):
        self.nume = nume
        self.carti_imprumutate = []

    def imprumuta_carte(self, carte):
        if not carte.este_imprumutata:
            self.carti_imprumutate.append(carte)
            carte.este_imprumutata = True
            print(self.nume, "a imprumutat", carte.titlu)
        else:
            print(carte.titlu, "este deja imprumutata")

    def returneaza_carte(self, carte):
        if carte in self.carti_imprumutate:
            self.carti_imprumutate.remove(carte)
            carte.este_imprumutata = False
            print(self.nume, "a returnat", carte.titlu)


class Biblioteca:
    def __init__(self):
        self.carti = []

    def adauga_carte(self, carte):
        self.carti.append(carte)

    def listeaza_carti_disponibile(self):
        print("Carti disponibile:")
        for c in self.carti:
            if not c.este_imprumutata:
                print("-", c.titlu)


# carti
c1 = Carte("1984", "Orwell", "1")
c2 = Carte("Mythology", "Steven", "2")
c3 = Carte("The Perks Of Being a Wallflower", "Jane", "3")
c4 = Carte("Hobbitul", "Tolkien", "4")
c5 = Carte("Harry Potter", "Rowling", "5")

# biblioteca
biblioteca = Biblioteca()
for c in [c1, c2, c3, c4, c5]:
    biblioteca.adauga_carte(c)

# membri
m1 = MembruBiblioteca("Ana")
m2 = MembruBiblioteca("Mihai")
m3 = MembruBiblioteca("Elena")

# simulare
m1.imprumuta_carte(c1)
m2.imprumuta_carte(c1)
m2.imprumuta_carte(c2)
m3.imprumuta_carte(c3)

biblioteca.listeaza_carti_disponibile()

m1.returneaza_carte(c1)
m2.imprumuta_carte(c1)

biblioteca.listeaza_carti_disponibile()

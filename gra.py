import random

typ_lokacji = 0


class Gracz:

    def __init__(self):
        self.imie = ""
        self.zdrowie = 20
        self.stamina = 100
        self.glod = 50
        self.pragnienie = 100
        self.atak = 2

    def get_info(self):
        print(f"zdrowie: {self.zdrowie}")
        print(f"stamina: {self.stamina}")
        print(f"głód: {self.glod}")
        print(f"pragnienie: {self.pragnienie}")
        print(f"moc ataku: {self.atak}")

    def get_imie(self):
        print(f"mam na imie {self.imie}")

    @staticmethod
    def eksploracja():
        gracz.pragnienie -= lokacja.trudnosc
        gracz.stamina -= lokacja.koszt_eksploracji

    def eksploracja_benefit(self, z, s, g, p, a):
        self.zdrowie += z
        if self.zdrowie > 100:
            self.zdrowie = 100
        self.stamina += s
        if self.stamina > 100:
            self.stamina = 100
        self.glod += g
        if self.glod > 100:
            self.glod = 100
        self.pragnienie += p
        if self.pragnienie > 100:
            self.pragnienie = 100
        self.atak += a


class Lokacja:

    def __init__(self, nr):
        self.nr_lokacji = nr
        self.obszar = 0
        self.trudnosc = 0
        self.nazwa = ""
        self.koszt_eksploracji = self.obszar*self.trudnosc

    def get_nazwa(self):
        return self.nazwa

    def get_info(self):
       return f"aby przeszukać lokację musisz poświęćić: {self.trudnosc} pragnienia oraz: {self.koszt_eksploracji} staminy"


class Lonka(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 1
        self.nazwa = "łąka"
        self.koszt_eksploracji = self.obszar*self.trudnosc

    @staticmethod
    def eksploruj():
        print("znalazłeś maliny!!!(głód+10)")
        z = 0
        s = 0
        g = 10
        p = 0
        a = 0

        return z, s, g, p, a


class Las(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 2
        self.nazwa = "las"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    @staticmethod
    def eksploruj():
        print("znalazłeś wodę!!!(pragnienie = 100)")
        z = 0
        s = 0
        g = 0
        p = 100
        a = 0

        return z, s, g, p, a


class MrocznyLas(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 4
        self.nazwa = "mroczny las"
        self.koszt_eksploracji = self.obszar * self.trudnosc


class Pustkowie(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 6
        self.nazwa = "pustkowie"
        self.koszt_eksploracji = self.obszar * self.trudnosc


class Gory(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 8
        self.nazwa = "góry"
        self.koszt_eksploracji = self.obszar * self.trudnosc


gracz = Gracz()
print("Aby rozpocząć gre wpisz swoje imię:")
gra = "on"
nr_lokacji = 0
gracz.imie = input()
print(f"Witaj {gracz.imie} obudziłeś się w lesie, nie pamiętasz co się stało. Ale wiesz jedno, musisz wrucić do swojej wioski")
print("aby dowiedzieć się na temat sterowania wpsz 'pomoc'")

while gra == "on":
    x = input()

    match x:
        case "pomoc":
            print("aby wyświetlić swoje aktualne statystyji wpisz 'status'")
            print("aby znależć nową lokację wpisz 'szukaj' (pragnienie-5, stamina-10) ")
            print("aby przeszukać lokacje wpisz 'eksploruj' (pragnienie-?, stamina-?)")
            print("aby odpocząć wpisz'odpoczynek'(głód-10,stamina+30,zdrowie+5)")
        case "status":
            gracz.get_info()
        case "szukaj":
            gracz.stamina -= 10
            gracz.pragnienie -= 10
            if gracz.pragnienie <= 0:
                print("umarłeś z pragnienia")
                gra = "off"
            elif gracz.stamina <= 0:
                print("umarłeś z wycieńczenia")
                gra = "off"
            else:
                los_lokacji = random.randrange(0, 101)
                if (los_lokacji == 0) or (los_lokacji == 100):
                    typ_lokacji = 1
                elif (los_lokacji > 0) and (los_lokacji < 20):
                    typ_lokacji = 2
                elif (los_lokacji >= 20) and (los_lokacji < 40):
                    typ_lokacji = 3
                elif (los_lokacji >= 40) and (los_lokacji < 60):
                    typ_lokacji = 4
                elif (los_lokacji >= 60) and los_lokacji < 80:
                    typ_lokacji = 5
                elif (los_lokacji >= 80) and los_lokacji < 100:
                    typ_lokacji = 6

                match typ_lokacji:
                    case 1:
                        print(f"gratulacje wróciłeś do wioski po przejściu {nr_lokacji} lokacji")
                        game = "off"
                    case 2:
                        nr_lokacji += 1
                        lokacja = Lonka(nr_lokacji)

                    case 3:
                        nr_lokacji += 1
                        lokacja = Las(nr_lokacji)

                    case 4:
                        nr_lokacji += 1
                        lokacja = MrocznyLas(nr_lokacji)

                    case 5:
                        nr_lokacji += 1
                        lokacja = Pustkowie(nr_lokacji)

                    case 6:
                        nr_lokacji += 1
                        lokacja = Gory(nr_lokacji)

                print(nr_lokacji)
                print(lokacja.get_nazwa())
                print(lokacja.get_info())
        case "eksploruj":
            gracz.eksploracja()
            bonus = lokacja.eksploruj()
            gracz.eksploracja_benefit(*bonus)

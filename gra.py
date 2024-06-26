import abc
import random
from abc import abstractmethod


class Gra:
    stan = "on"


class Gracz:

    @staticmethod
    def czy_zyje():
        if gracz.zdrowie <= 0:
            print("umarłeś w wyniku odniesionych ran")
            Gra.stan = "off"
        if gracz.pragnienie <= 0:
            print("umarłeś z pragnienia")
            Gra.stan = "off"
        if gracz.glod <= 0:
            print("umarłeś z głodu")
            Gra.stan = "off"
        if gracz.stamina <= 0:
            print("umarłeś z wycieńczenia")
            Gra.stan = "off"

    def __init__(self):
        self.__imie = ""
        self.zdrowie = 20
        self.stamina = 100
        self.glod = 50
        self.pragnienie = 100
        self.atak = 2

    def ustaw(self):
        wartosc = input("wybierz poziom trudnosci (łatwy = 1, normalny = 2, trudny = 3)")
        match wartosc:
            case "1":
                self.zdrowie = 80
                self.stamina = 100
                self.glod = 50
                self.pragnienie = 100
                self.atak = 20
            case "2":
                self.zdrowie = 20
                self.stamina = 70
                self.glod = 40
                self.pragnienie = 70
                self.atak = 10
            case "3":
                self.zdrowie = 20
                self.stamina = 50
                self.glod = 30
                self.pragnienie = 50
                self.atak = 5
            case "test":
                self.zdrowie = 100
                self.stamina = 100
                self.glod = 100
                self.pragnienie = 100
                self.atak = 100
            case _:
                self.ustaw()

    def get_info(self):
        print(f"zdrowie: {self.zdrowie}")
        print(f"stamina: {self.stamina}")
        print(f"głód: {self.glod}")
        print(f"pragnienie: {self.pragnienie}")
        print(f"moc ataku: {self.atak}")

    def get_imie(self):
        print(f"mam na imie {self.__imie}")

    @staticmethod
    def eksploracja():
        gracz.pragnienie -= lokacja.trudnosc
        gracz.stamina -= lokacja.koszt_eksploracji

    def wyrownaj_statystyki(self):
        if self.zdrowie > 100:
            self.zdrowie = 100
        if self.stamina > 100:
            self.stamina = 100
        if self.glod > 100:
            self.glod = 100
        if self.pragnienie > 100:
            self.pragnienie = 100

    def eksploracja_benefit(self, z, g, p, a):
        self.zdrowie += z
        self.glod += g
        self.pragnienie += p
        self.atak += a
        self.wyrownaj_statystyki()

    def odpoczynek(self):
        try:
            czas = int(input("ile godzin zamierzasz odpocząć? "))
        except ValueError:  # POPRAWKA: Obsługa niepoprawnego wejścia.
            print("Podaj poprawną liczbę godzin.")
            return
        r_glod = 5*czas
        r_stamina = 15*czas
        r_zdrowie = 2*czas
        if czas == 0:
            print("nie odpocząłeś")
        else:
            self.glod -= r_glod
            self.stamina += r_stamina
            self.zdrowie += r_zdrowie
            if czas == 1:
                print("po godzinie odpoczynku zyskałeś 15 staminy oraz 2 zdrowia")
            else:
                print(f"po {czas} godzinach odpoczynku zyskałeś {r_stamina} staminy oraz {r_zdrowie} zdrowia")
                self.wyrownaj_statystyki()

    def walcz(self, wrog):
        self.zdrowie -= wrog.atak * (wrog.zdrowie / gracz.atak)
        self.stamina -= wrog.zdrowie - (wrog.atak*1.5)
        if self.zdrowie <= 0:
            print(f"{wrog.nazwa} cię pokonał")
            self.czy_zyje()
        else:
            print(
                f"udało ci się zabić {wrog.nazwa}!(zdrowie - {wrog.atak * (wrog.zdrowie / gracz.atak)}, stamina - {3 * (wrog.zdrowie / gracz.atak)} )")

    def uciekaj(self, wrog):
        los = random.randrange(0, 101)
        if los <= wrog.szansa:
            self.stamina -= wrog.zdrowie
            self.czy_zyje()
            print(f"udało ci się uciec(stamina-{wrog.zdrowie})")
        else:
            self.zdrowie = 0
            print(f"{wrog.nazwa} cie dopadł")
            self.czy_zyje()

    @staticmethod
    def spotkanie(wrog):
        print(f"napotkałeś na swojej drodze wilka(zdrowie: {wrog.zdrowie}, siła: {wrog.atak}) !!!")
        decyzja = input("czy chcesz walczyć?(walcz/uciekaj)")
        match decyzja:
            case "walcz":
                gracz.walcz(wrog)
            case "uciekaj":
                gracz.uciekaj(wrog)
            case _:
                print("podejmij właściwą decyzję! (walcz/uciekaj)")


class Wrog(abc.ABC):
    def __init__(self):
        self.nazwa = ""
        self.zdrowie = 0
        self.atak = 0
        self.szansa = 0


class Wilk(Wrog):
    def __init__(self):
        super().__init__()
        self.nazwa = "wilk"
        self.zdrowie = random.randrange(2, 11)
        self.atak = random.randrange(1, 4)
        self.szansa = random.randrange(0, 101)


class Niedzwiedz(Wrog):
    def __init__(self):
        super().__init__()
        self.nazwa = "niedźwiedź"
        self.zdrowie = 80
        self.atak = 20
        self.szansa = random.randrange(0, 60)


class Lokacja(abc.ABC):

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

    @abstractmethod
    def eksploruj(self):
        pass


class Lonka(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 1
        self.nazwa = "łąka"
        self.koszt_eksploracji = self.obszar*self.trudnosc

    @staticmethod
    def jadalne_los():
        ilosc = random.randrange(1, 3)
        jedzenie = {
            'maliny': 2,
            'mniszek lekarski': 1,
            'mak polny': 4
        }
        losowe_jedzenie = random.choice(list(jedzenie.keys()))
        nazwa, sytosc = losowe_jedzenie, jedzenie[losowe_jedzenie]
        return nazwa, sytosc, ilosc

    @staticmethod
    def nie_jadalne_los():
        ilosc = random.randrange(1, 3)
        jedzenie = {
            'czarny bez': 2,
            'dzika róża': 2,
            'Chaber bławatek': 2
        }
        losowe_jedzenie = random.choice(list(jedzenie.keys()))
        nazwa, sytosc = losowe_jedzenie, jedzenie[losowe_jedzenie]
        return nazwa, sytosc, ilosc

    def eksploruj(self):
        znal = random.randrange(1, 3)
        if znal == 1:
            typ = self.jadalne_los()
            jedzenie = Jadalne(*typ)
        else:
            typ = self.nie_jadalne_los()
            jedzenie = NieJadalne(*typ)

        wybor = ""
        while wybor != "t" and wybor != "n":
            wybor = input(f"znalazłeś {jedzenie.nazwa}, czy chcesz zjeść? wpisz 't' lub 'n'")
            match wybor:
                case "t":
                    if isinstance(jedzenie, Jadalne):
                        gracz.eksploracja_benefit(jedzenie.sytosc * jedzenie.ilosc, (jedzenie.sytosc * 2) * jedzenie.ilosc, 0, 0)
                        print(f"zjadłeś '{jedzenie.nazwa}'")
                    else:
                        gracz.eksploracja_benefit(-1 * (jedzenie.sytosc * jedzenie.ilosc), -1 * ((jedzenie.sytosc * 2) * jedzenie.ilosc), 0, 0)
                        print(f"zjadłeś '{jedzenie.nazwa}' nie był to dobry pomysł")
                case "n":
                    print(f"postanowiłeś nie ruszać '{jedzenie.nazwa}'")
                case _:
                    print("wybierz poprawną wartość 't' lub 'n' !!!")


class Las(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 2
        self.nazwa = "las"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        los = random.randrange(0, 101)
        if los <= 70:
            print("znalazłeś wodę!!!(pragnienie = 100)")
            p = 100
            gracz.eksploracja_benefit(0, 0, p, 0)
        else:
            wilk = Wilk()
            gracz.spotkanie(wilk)


class MrocznyLas(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 4
        self.nazwa = "mroczny las"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        pass


class Pustkowie(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 6
        self.nazwa = "pustkowie"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        pass


class Gory(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 8
        self.nazwa = "góry"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        los = random.randrange(1, 11)
        if los < 9:
            niedzwiedz = Niedzwiedz()
            gracz.spotkanie(niedzwiedz)
        los2 = random.randrange(1, 11)
        if los2 <= 5:
            print(f"znalazłeś swoją wioskę!!! wróciłeś do domu po przejściu {nr_lokacji} lokacji")
        else:
            print("eksploruj góry dalej w poszukiwaniu domu lub idź do innej lokacji")


class Jedzenie(abc.ABC):
    def __init__(self, nazwa, sytosc, ilosc):
        self.nazwa = nazwa
        self.ilosc = ilosc
        self.sytosc = sytosc


class Jadalne(Jedzenie):
    def __init__(self, nazwa, sytosc, ilosc):
        super().__init__(nazwa, sytosc, ilosc)
        self.nazwa = nazwa
        self.sytosc = sytosc
        self.ilosc = ilosc


class NieJadalne(Jedzenie):
    def __init__(self, nazwa, sytosc, ilosc):
        super().__init__(nazwa, sytosc, ilosc)
        self.nazwa = nazwa
        self.sytosc = sytosc
        self.ilosc = ilosc


gracz = Gracz()
gracz.ustaw()

print("Aby rozpocząć gre wpisz swoje imię:")
gracz.imie = input()
nr_lokacji = 0
lokacja = Las(nr_lokacji)
print(f"Witaj {gracz.imie} obudziłeś się w lesie, nie pamiętasz co się stało. Ale wiesz jedno, musisz wrucić do swojej wioski, która znajduje się w górach")
print("aby dowiedzieć się na temat sterowania wpsz 'pomoc'")

while Gra.stan == "on":
    try:
        gracz.czy_zyje()
        x = input()
        nr_lokacji = 1
        match x:
            case "pomoc":
                print("aby wyświetlić swoje aktualne statystyji wpisz 'status'")
                print("aby szukać drogi do domu wpsz 'szukaj' (pragnienie-5, stamina-10) ")
                print("aby przeszukać lokacje wpisz 'eksploruj' (pragnienie-?, stamina-?)")
                print("aby odpocząć wpisz'odpocznij'(głód-5,stamina+15,zdrowie+2 za każdą godzinę)")
            case "status":
                gracz.get_info()
            case "szukaj":
                gracz.stamina -= 10
                gracz.pragnienie -= 10

                typ_lokacji = 6

                # los_lokacji = random.randrange(0, 101)
                # if (los_lokacji >= 0) and (los_lokacji < 35):
                #     typ_lokacji = 2                             #jedzenie           ----
                # elif (los_lokacji > 35) and (los_lokacji < 65):
                #     typ_lokacji = 3                             #woda, wilk         ----
                # elif (los_lokacji > 65) and (los_lokacji < 80):
                #     typ_lokacji = 4                             #szkielet, broń
                # elif (los_lokacji > 80) and los_lokacji < 95:
                #     typ_lokacji = 5                             #wąż, zbroja, oaza
                # elif (los_lokacji >= 95) and los_lokacji < 100:
                #     typ_lokacji = 6                             #niedźwiedź, win
                # typ_lokacji = 2
                match typ_lokacji:
                    case 1:
                        print(f"gratulacje wróciłeś do wioski po przejściu {nr_lokacji} lokacji")
                        game = "off"
                        continue
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
                print(f"zawędrowałeś do: {lokacja.get_nazwa()}")
                print(lokacja.get_info())
            case "eksploruj":
                gracz.eksploracja()
                lokacja.eksploruj()
            case "odpocznij":
                gracz.odpoczynek()
            case _:
                print("wpisz poprawne polecenie(jeśli nie pamiętasz poleceń wpisz'pomoc')!")
    except Exception as e:
        print(f"wystąpił błąd {e}")

import abc
import copy
import random
from abc import abstractmethod
from enum import Enum
#                                    Dzień dobry Panie doktorze poproszę o informację zwrotną czy się Panu spododała moja gra.
#
#                                                                                                Pozdrawiam: Dawid Biegański


class Gra:
    stan = "on"


class PoziomTrudnosci(Enum):
    LATWY = 1
    NORMALNY = 2
    TRUDNY = 3
    TESTOWY = 4


class Gracz:

    def __init__(self):
        self.__imie = ""
        self.zdrowie = 20
        self.stamina = 100
        self.glod = 50
        self.pragnienie = 100
        self.atak = 2
        self.pancerz = 0
        self.szanse = 3

    def czy_zyje(self):
        if gracz.zdrowie <= 0:
            print("umarłeś w wyniku odniesionych ran")
            Gra.stan = "off"
        elif gracz.pragnienie <= 0:
            print("umarłeś z odwodnienia")
            Gra.stan = "off"
        elif gracz.glod <= 0:
            print("umarłeś z głodu")
            Gra.stan = "off"
        elif gracz.stamina <= 0:
            print("umarłeś z wycieńczenia")
            Gra.stan = "off"
        if Gra.stan == "off":
            decyzja = input("czy chcesz kontynuować??(t/n)")
            match decyzja:
                case "t":
                    if self.szanse != 0:
                        self.szanse -= 1
                        print("wczytano wcześniejsze statystyki")
                        print(f"liczba pozostałych wskrzeszeń = {self.szanse}")
                        gracz.zdrowie = kopia.zdrowie
                        self.stamina = kopia.stamina
                        self.glod = kopia.glod
                        self.pragnienie = kopia.pragnienie
                        self.atak = kopia.atak
                        self.pancerz = kopia.pancerz
                        Gra.stan = "on"
                    else:
                        print("niestety ale to już koniec!")
                case "n":
                    print("dzięki za gre!!!")
                case _:
                    self.czy_zyje()
        if gra.stan == "off":
            exit()

    def ustaw(self):
        wartosc = input("wybierz poziom trudnosci (łatwy = 1, normalny = 2, trudny = 3, testowy = 4): ")
        try:
            poziom = PoziomTrudnosci(int(wartosc))
        except ValueError:
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            self.ustaw()
            return

        match poziom:
            case PoziomTrudnosci.LATWY:
                self.zdrowie = 80
                self.stamina = 100
                self.glod = 50
                self.pragnienie = 100
                self.atak = 20
                self.pancerz = 10
                self.szanse = 2
            case PoziomTrudnosci.NORMALNY:
                self.zdrowie = 20
                self.stamina = 70
                self.glod = 40
                self.pragnienie = 70
                self.atak = 10
                self.pancerz = 5
                self.szanse = 1
            case PoziomTrudnosci.TRUDNY:
                self.zdrowie = 20
                self.stamina = 50
                self.glod = 30
                self.pragnienie = 50
                self.atak = 5
                self.pancerz = 2
                self.szanse = 0
            case PoziomTrudnosci.TESTOWY:
                self.zdrowie = 100
                self.stamina = 100
                self.glod = 100
                self.pragnienie = 100
                self.atak = 100
                self.pancerz = 50
                self.szanse = 10

    def get_info(self):
        print(f"zdrowie: {self.zdrowie}")
        print(f"stamina: {self.stamina}")
        print(f"głód: {self.glod}")
        print(f"pragnienie: {self.pragnienie}")
        print(f"moc ataku: {self.atak}")
        print(f"pancerz: {self.pancerz}")

    def set_imie(self):
        self.__imie = str(input("Aby rozpocząć gre wpisz swoje imię:"))

    def get_imie(self):
        return self.__imie

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
        if self.pancerz > 50:
            self.pancerz = 50

    def eksploracja_benefit(self, z, g, p, a, pa):
        self.zdrowie += z
        self.glod += g
        self.pragnienie += p
        self.atak += a
        self.pancerz += pa
        self.wyrownaj_statystyki()

    def odpoczynek(self):
        try:
            czas = int(input("ile godzin zamierzasz odpocząć? "))
        except ValueError:  # POPRAWKA: Obsługa niepoprawnego wejścia.
            print("Podaj poprawną liczbę godzin.")
            return
        r_glod = 5*czas
        r_stamina = 15*czas
        r_zdrowie = 5*czas
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
        obrazenia = max(wrog.atak - self.pancerz, 0)
        self.zdrowie -= obrazenia * (wrog.zdrowie / gracz.atak)
        self.stamina -= wrog.zdrowie/2
        if self.zdrowie <= 0:
            print(f"{wrog.nazwa} cię pokonał")
            self.czy_zyje()
        else:
            print(
                f"udało ci się zabić {wrog.nazwa}!(zdrowie - {wrog.atak * (wrog.zdrowie / gracz.atak)}, stamina - {wrog.zdrowie/2} )")

    def uciekaj(self, wrog):
        los = random.randrange(0, 101)
        if los <= wrog.szansa:
            self.stamina -= wrog.zdrowie
            self.pragnienie -= wrog.zdrowie*0.8
            self.czy_zyje()
            print(f"udało ci się uciec(stamina-{wrog.zdrowie*0.6})")
        else:
            self.zdrowie = 0
            print(f"{wrog.nazwa} cie dopadł")
            self.czy_zyje()

    @staticmethod
    def spotkanie(wrog):
        print(f"napotkałeś na swojej drodze {wrog.nazwa}(zdrowie: {wrog.zdrowie}, siła: {wrog.atak}) !!!")
        decyzja = input("czy chcesz walczyć?(walcz/uciekaj)")
        match decyzja:
            case "walcz":
                gracz.walcz(wrog)
            case "uciekaj":
                gracz.uciekaj(wrog)
            case _:
                gracz.spotkanie(wrog)


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


class Nieumarly(Wrog):
    def __init__(self):
        super().__init__()
        self.nazwa = "nieumarły"
        self.zdrowie = random.randrange(20, 60)
        self.atak = random.randrange(5, 10)
        self.szansa = 100

    def interakcja(self):
        wybor = input(
            "natrafiasz na dawno już nieżyjące zwłoki, widzisz że nieszczęśnik posiadał miecz czy chcesz go zabrać?(t/n)")
        match wybor:
            case "t":
                print("zabierasz miecz lecz, ku twojemu zdumieniu zwłoki wracają do życia !!! (atak = 30)")
                gracz.atak = 30
                gracz.spotkanie(self)


class Zmija(Wrog):
    def __init__(self):
        super().__init__()
        self.nazwa = "żmija"
        self.atak = random.randrange(3, 7)
        self.szansa = 100


class Niedzwiedz(Wrog):
    def __init__(self):
        super().__init__()
        self.nazwa = "niedźwiedź"
        self.zdrowie = 80
        self.atak = 20
        self.szansa = random.randrange(0, 61)


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
            'jagody': 4,
            'maliny': 4,
            'mniszek lekarski': 1,
            'mak polny': 2
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
                        gracz.eksploracja_benefit(jedzenie.sytosc * jedzenie.ilosc, (jedzenie.sytosc * 2) * jedzenie.ilosc, 0, 0, 0)
                        print(f"zjadłeś '{jedzenie.nazwa}'(zdrowie+{jedzenie.sytosc * jedzenie.ilosc}, głód+{(jedzenie.sytosc * 2) * jedzenie.ilosc})")
                    else:
                        gracz.eksploracja_benefit(-1 * (jedzenie.sytosc * jedzenie.ilosc), -1 * ((jedzenie.sytosc * 2) * jedzenie.ilosc), 0, 0, 0)
                        print(f"zjadłeś '{jedzenie.nazwa}' nie był to dobry pomysł(zdrowie-{jedzenie.sytosc * jedzenie.ilosc}, głód-{(jedzenie.sytosc * 2) * jedzenie.ilosc})")
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
            gracz.eksploracja_benefit(0, 0, p, 0, 0)
        else:
            wilk = Wilk()
            gracz.spotkanie(wilk)
            del wilk


class Rzeka(Lokacja):
    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = 5
        self.trudnosc = 1
        self.nazwa = "rzeka"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        wynik = random.randrange(1, 101)
        if wynik <= 50:
            print("napiłeś się wody, zaspokoiłeś pragnienie(pragnienie = 100)")
            gracz.eksploracja_benefit(0, 0, 100, 0, 0)
        elif wynik <= 75:
            print("złowiłeś rybę(głód +30)")
            gracz.eksploracja_benefit(0, 30, 0, 0, 0)
        elif wynik <= 85:
            print("znalazłeś żmiję")
            wrog = Zmija()
            gracz.spotkanie(wrog)


class MrocznyLas(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 4
        self.nazwa = "mroczny las"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def eksploruj(self):
        los = random.randrange(0, 2)
        if los == 0:
            wybor = input("znalazłeś wodę ale dziwnie pachnie chcesz ją wypić?(t/n)")
            match wybor:
                case "t":
                    print("napiłeś się jednak woda była zanieczyszczona!!!(pragnienie + 50, zdrowie -10)")
                    gracz.eksploracja_benefit(-10, 0, 50, 0, 0)
                case "n":
                    print("postanowiłeś nie pić")
                case _:
                    lokacja.eksploruj()
        else:
            nieumarly = Nieumarly()
            nieumarly.interakcja()
            del nieumarly


class Ruiny(Lokacja):

    def __init__(self, nr):
        super().__init__(nr)
        self.obszar = random.randrange(1, 5)
        self.trudnosc = 6
        self.nazwa = "pustkowie"
        self.koszt_eksploracji = self.obszar * self.trudnosc

    def zbrojownia(self):
        wybor = input("natrafiłeś na opuszczoną zbrojownie cz chcesz się rozjejrzeć?(t/n)")
        match wybor:
            case "t":
                print("przeszukując zbrojownie znalazłeś fragmęt zbroi(pancerz +10)")
                los = random.randrange(0, 3)
                gracz.pancerz += 10
                if los != 0:
                    zmija = Zmija()
                    print(f"ukąsiła cię żmija na szczęście nie była jadowita(zdrowie -{zmija.atak})")
                    gracz.zdrowie -= zmija.atak
            case "n":
                print("postanowiłeś nie wchodzić do środka")
            case _:
                self.zbrojownia()

    def eksploruj(self):
        los = random.randrange(0, 4)
        if los == 0:
            print("nic nie znalazłeś, czy chcesz eksplorować ruiny dalej?(eksploruj)")
        else:
            self.zbrojownia()


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
            del niedzwiedz

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


gra = Gra()
gracz = Gracz()
gracz.ustaw()
gracz.set_imie()
nr_lokacji = 0
typ_lokacji = 3
lokacja = Las(nr_lokacji)
print(f"Witaj {gracz.get_imie()} obudziłeś się w lesie, nie pamiętasz co się stało. Ale wiesz jedno, musisz wrucić do swojej wioski, która znajduje się w górach")
print("aby dowiedzieć się na temat sterowania wpsz 'pomoc'")

while Gra.stan == "on":
    kopia = copy.copy(gracz)
    try:
        x = input()
        nr_lokacji = 1
        gracz.czy_zyje()
        match x:
            case "pomoc":
                print("aby wyświetlić swoje aktualne statystyji wpisz 'status'")
                print("aby szukać drogi do domu wpsz 'szukaj' (pragnienie-10, stamina-10) ")
                print("aby przeszukać lokacje wpisz 'eksploruj' (pragnienie-?, stamina-?)")
                print("aby odpocząć wpisz 'odpocznij' (głód-5,stamina+15,zdrowie+5 za każdą godzinę)")
            case "status":
                gracz.get_info()
            case "szukaj":
                gracz.stamina -= 10
                gracz.pragnienie -= 10
                los_lokacji = random.randrange(0, 101)
                if (los_lokacji >= 0) and (los_lokacji < 20):
                    typ_lokacji = 1
                elif (los_lokacji >= 20) and (los_lokacji < 45):
                    typ_lokacji = 2
                elif (los_lokacji > 45) and (los_lokacji < 65):
                    typ_lokacji = 3
                elif (los_lokacji > 65) and (los_lokacji < 80):
                    typ_lokacji = 4
                elif (los_lokacji > 80) and los_lokacji < 95:
                    typ_lokacji = 5
                elif (los_lokacji >= 95) and los_lokacji < 100:
                    typ_lokacji = 6
                match typ_lokacji:
                    case 1:
                        nr_lokacji += 1
                        lokacja = Rzeka(nr_lokacji)
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
                        lokacja = Ruiny(nr_lokacji)

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
        gracz.czy_zyje()
    except Exception as e:
        print(f"wystąpił błąd {e}")

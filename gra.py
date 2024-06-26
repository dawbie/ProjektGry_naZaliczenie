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
        if gracz.pragnienie <= 0:
            print("umarłeś z wycieńczenia")
            Gra.stan = "off"

    def __init__(self):
        self.__imie = ""
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
            print(f"napotkałeś na swojej drodze wilka(zdrowie: {wilk.zdrowie}, siła: {wilk.atak}) !!!")
            decyzja = input("czy chcesz walczyć?(walcz/uciekaj)")
            match decyzja:
                case "walcz":
                    gracz.zdrowie -= wilk.atak*(wilk.zdrowie/gracz.atak)
                    gracz.stamina -= 3*(wilk.zdrowie/gracz.atak)
                    gracz.czy_zyje()
                    print(f"udało ci się zabić wilka!(zdrowie - {wilk.atak*(wilk.zdrowie/gracz.atak)}, stamina - {3*(wilk.zdrowie/gracz.atak)} )")
                case "uciekaj":
                    powodzenie = random.randrange(0, 101)
                    if powodzenie < 20:
                        print("niestety wilk cię dopadł")
                        gracz.zdrowie = 0
                    else:
                        gracz.stamina -= 30
                        gracz.czy_zyje()
                        print("udało ci się uciec(stamina - 30)")
                case _:
                    print("podejmij właściwą decyzję! (walcz/uciekaj)")


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


class Zwierze(abc.ABC):
    def __init__(self):
        self.zdrowie = 0
        self.atak = 0


class Wilk(Zwierze):
    def __init__(self):
        super().__init__()
        self.zdrowie = random.randrange(2, 11)
        self.atak = random.randrange(1, 4)


gracz = Gracz()

print("Aby rozpocząć gre wpisz swoje imię:")
nr_lokacji = 0
gracz.imie = input()
lokacja = Las(nr_lokacji)
print(f"Witaj {gracz.imie} obudziłeś się w lesie, nie pamiętasz co się stało. Ale wiesz jedno, musisz wrucić do swojej wioski")
print("aby dowiedzieć się na temat sterowania wpsz 'pomoc'")

while Gra.stan == "on":
    try:
        gracz.czy_zyje()
        x = input()
        nr_lokacji = 0
        match x:
            case "pomoc":
                print("aby wyświetlić swoje aktualne statystyji wpisz 'status'")
                print("aby szukać drogi do domu wpsz 'szukaj' (pragnienie-5, stamina-10) ")
                print("aby przeszukać lokacje wpisz 'eksploruj' (pragnienie-?, stamina-?)")
                print("aby odpocząć wpisz'odpocznij'(głód-5,stamina+15,zdrowie+2 za każdą godzinę)")
            case "status":
                gracz.get_info()
            case "szukaj":
                # gracz.stamina -= 10
                # gracz.pragnienie -= 10
                # los_lokacji = random.randrange(0, 101)
                # if (los_lokacji == 0) or (los_lokacji == 100) or (los_lokacji == 21):
                #     typ_lokacji = 1
                # elif (los_lokacji > 0) and (los_lokacji < 21):
                #     typ_lokacji = 2
                # elif (los_lokacji > 21) and (los_lokacji < 40):
                #     typ_lokacji = 3
                # elif (los_lokacji >= 40) and (los_lokacji < 60):
                #     typ_lokacji = 4
                # elif (los_lokacji >= 60) and los_lokacji < 80:
                #     typ_lokacji = 5
                # elif (los_lokacji >= 80) and los_lokacji < 100:
                #     typ_lokacji = 6
                typ_lokacji = 2
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
                print(nr_lokacji)
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

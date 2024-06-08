import random
from math import sqrt
WspHetmanow=[]
WspSkoczkow=[]


def Figury(ile):
    for a in range(ile):

        typ_figury = random.randrange(0, 2)  # 0 to hetman, 1 to skoczek
        x = random.randrange(1, 9)
        y = random.randrange(1, 9)
        wszystkie_figury = WspHetmanow + WspSkoczkow

        if typ_figury == 0:
            while czy_duplikat([x, y], wszystkie_figury):
                x = random.randrange(1, 9)
                y = random.randrange(1, 9)
            WspHetmanow.append([x, y])

        else:
            while czy_duplikat([x, y], wszystkie_figury):
                x = random.randrange(1, 9)
                y = random.randrange(1, 9)
            WspSkoczkow.append([x, y])
    return (WspHetmanow, WspSkoczkow)

def czy_duplikat(nowa_figura, inne_figury):
    for figura in inne_figury:
        if figura == nowa_figura:
            return True
    return False

def Pawn():
    wszystkie_figury = WspHetmanow + WspSkoczkow
    x = random.randrange(1, 9)
    y = random.randrange(1, 9)
    while czy_duplikat([x, y], wszystkie_figury) == True:
        x = random.randrange(1, 9)
        y = random.randrange(1, 9)
    return ([x, y])

ile = int(input('Ile Figur (Nie licząc pionka) znajduje sie na planszy:  '))
Figury(ile)
Pionek = Pawn()


def plansza():

    row1 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row0 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    rows = [row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy()]

    for wsp in WspHetmanow:
        rows[8-  wsp[1]][wsp[0] - 1] = ' H '  # dodawanie pozycji hetmanow na plansze
    for wsp in WspSkoczkow:
        rows[8 - wsp[1]][wsp[0] - 1] = ' S '
    rows[8 - Pionek[1]][Pionek[0] - 1] = ' P '  # dodawanie pozycji pionka na plansze

    gora = ' +------------------------+\n'
    plansza = '\n' + gora
    for lista in range(len(rows)):
        plansza += (str(8 - lista) + '|')
        for element in range(len(row0)):
            plansza += rows[lista][element]
        plansza += '|\n'
    plansza += gora
    plansza += '   1  2  3  4  5  6  7  8\n\n'  # tworzenie planszy
    return (plansza)

def Pitagoras(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def CzyPomiedzy(a,c,b): #c to punkt ktorego przynaleznosc do odcinka sie sprawdza
    return Pitagoras(a, c) + Pitagoras(c, b) == Pitagoras(a, b)



def czy_hetman_zbije(Hetman):
    wszystkie_figury = WspHetmanow + WspSkoczkow
    if abs(Hetman[0]-Pionek[0])==abs(Hetman[1]-Pionek[1])or Hetman[0]==Pionek[0] or Hetman[1]==Pionek[1]:
        for inne in wszystkie_figury:
            if inne!=Hetman:
                if CzyPomiedzy(Hetman,inne,Pionek)==True:
                    return False
        return True
    return False

def czy_skoczek_zbije(Figura):
    if Figura[0]+2 == Pionek[0] and Figura[1]+1 == Pionek[1] or Figura[0]+2 == Pionek[0] and Figura[1]-1 == Pionek[1]:
        return True
    elif Figura[0]+1 == Pionek[0] and Figura[1]+2 == Pionek[1] or Figura[0]-1 == Pionek[0] and Figura[1]+2 == Pionek[1]:
        return True
    elif Figura[0]-2 == Pionek[0] and Figura[1]+1 == Pionek[1] or Figura[0]-2 == Pionek[0] and Figura[1]-1 == Pionek[1]:
        return True
    elif Figura[0]+1 == Pionek[0] and Figura[1]-2 == Pionek[1] or Figura[0]-1 == Pionek[0] and Figura[1]-2 == Pionek[1]:
        return True
    else:
        return False

def wyswietlanie_zbicia():
    zbijajace = []
    for hetman in WspHetmanow:
        if czy_hetman_zbije(hetman)==True:
            zbijajace.append(hetman)
    for skoczek in WspSkoczkow:
        if czy_skoczek_zbije(skoczek)==True:
            zbijajace.append(skoczek)
    if len(zbijajace)==0:
        return(plansza() + "Żadna figura nie ma opcji zbicia pionka\n")
    else:
        return(plansza() + 'Figury o tych współrzędnych mogą zbić pionka: ' + str(zbijajace) + '\n')

print(wyswietlanie_zbicia())

while 0==0:
    akcja=int(input('Co chcesz zrobić?\n\n 1) Wylosować nową pozycję dla pionka\n 2) Usunięcie dowolnej figury\n 3) Dodanie nowej, losowej figury\n 4) Zakończyć program\n:  '))

    if akcja == 4:
        break

    elif akcja == 1:
        Pionek = Pawn()
        print('\nNowa pozycja to: ' + str(Pionek) + '\n' + wyswietlanie_zbicia())

    elif akcja == 2:
        indeks = int(input(str(WspHetmanow + WspSkoczkow) + '\nPodaj index figury do Usunięcia: '))
        print('\nUsunieto figure o wspolrzednych ' + str((WspHetmanow+WspSkoczkow).pop(indeks)) + '\n' + wyswietlanie_zbicia())

    elif akcja == 3:
        Figury(1)
        print('Dodano nowa figure.\n' + wyswietlanie_zbicia())

    else:
        print('\nPodano niepoprawną wartość\n')
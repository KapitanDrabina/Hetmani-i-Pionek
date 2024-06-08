import random
from math import sqrt

WspHetmanow = []
WspSkoczkow = []
#zwraca tablice z wygenerowanymi pozycjami (odrazu uzyte do wygenerowania pozycji pionka)
def Figury(ile):
    for a in range(ile+1):

        x = random.randrange(1, 9)
        y = random.randrange(1, 9)

        while czy_duplikat([x, y], WspHetmanow):
            x = random.randrange(1, 9)
            y = random.randrange(1, 9)
        if a == ile:
            Pawn = [x, y]
        else:
            WspHetmanow.append([x, y])
    return (Pawn)

def czy_duplikat(nowa_figura, inne_figury):
    for figura in inne_figury:
        if figura == nowa_figura:
            return True
    return False

Pionek = Figury(int(input('Ile Figur (Nie licząc pionka) znajduje sie na planszy:  ')))


#tworzenie hetmanow i pionka po raz pierwszy

#funkcja tworzy pusta plansze i potem doklada na nia pozycje figur
def plansza():

    row1 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row0 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    rows = [row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy()]

    for wsp in WspHetmanow:
        rows[8 - wsp[1]][wsp[0] - 1] = ' H '  # dodawanie pozycji hetmanow na plansze
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

def CzyZbije(Hetman):
    if abs(Hetman[0]-Pionek[0])==abs(Hetman[1]-Pionek[1])or Hetman[0]==Pionek[0] or Hetman[1]==Pionek[1]:
        for inne in WspHetmanow:
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
        if CzyZbije(hetman)==True:
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
    akcja=int(input("Co chcesz zrobić (1,2 lub 3)\n\n1) Wylosowac nowa pozycje dla pionka\n2) Usuniecie dowolnego hetmana\n3) Dodanie skoczka na planszę (o losowej pozycji)\n4) Zakonczyc program\n\n:  "))
    if akcja==4:
        break

    elif akcja==1:
        Pionek=Figury(0)[0]
        print('\nNowa pozycja to: ' + str(Pionek) + '\n' + wyswietlanie_zbicia())

    elif akcja==2:
        indeks=int(input(str(WspHetmanow)+'\nPodaj index hetmana do Usuniecia: '))
        print('\nUsunieto hetmana o wspolrzednych ' + str(WspHetmanow.pop(indeks)) + '\n' + wyswietlanie_zbicia())

    elif akcja == 3:
        WspSkoczkow.append(Figury(0))
        print('Dodano skoczka na plansze.\n' + wyswietlanie_zbicia() + '\n')

#koniec :)
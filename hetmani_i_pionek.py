import random
from math import sqrt

#zwraca tablice z wygenerowanymi pozycjami (odrazu uzyte do wygenerowania pozycji pionka)
def Figury(ile):
    WspHetmanow = []
    while len(WspHetmanow) != ile+1:
        if len(WspHetmanow) == 6:
            break
        JestDuplikat = 0
        x = random.randrange(1, 8)
        y = random.randrange(1, 8)
        for figura in range(len(WspHetmanow)):
            if WspHetmanow[figura] == [x,y]:
                JestDuplikat = 1
        if JestDuplikat == 0:
            WspHetmanow.append([x,y])
    return(WspHetmanow)

WspHetmanow = Figury(int(input('Ile hetmanow znajduje sie na planszy? (Maksymalnie 5):  ')))
Pionek = WspHetmanow.pop()
#tworzenie hetmanow i pionka po raz pierwszy

#funkcja tworzy pusta plansze i potem doklada na nia pozycje figur
def plansza():

    row1 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row0 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    rows = [row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy(), row1.copy(), row0.copy()]

    for wsp in WspHetmanow:
        rows[8-  wsp[1]][wsp[0] - 1] = ' H '  # dodawanie pozycji hetmanow na plansze
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

def Wyswietlenie_zbicia():
    Zbijajace=[]
    for hetman in WspHetmanow:
        if CzyZbije(hetman)==True:
            Zbijajace.append(hetman)
    if len(Zbijajace)==0:
        wynik=('Zaden hetman nie moze zbic pionka')
    elif len(Zbijajace)==1:
        wynik=('Hetman o tych wspolrzednych moze zbic pionka: '+str(Zbijajace)+'\n')
    else:
        wynik=("Hetmany o tych wspolrzednych moga zbic pionek: " + str(Zbijajace)+'\n')
    return(plansza()+wynik)

print(Wyswietlenie_zbicia())


while 0==0:
    akcja=int(input("Co chcesz zrobić (1,2 lub 3)\n\n1) Wylosowac nowa pozycje dla pionka\n2) Usuniecie dowolnego hetmana\n3) Zakonczyc program\n\n:  "))
    if akcja==3:
        break

    elif akcja==1:
        Pionek=Figury(0)[0]
        print('\nNowa pozycja to: ' + str(Pionek) + '\n' + Wyswietlenie_zbicia())

    elif akcja==2:
        indeks=int(input(str(WspHetmanow)+'\nPodaj index hetmana do Usuniecia: '))
        print('\nUsunieto hetmana o wspolrzednych ' + str(WspHetmanow.pop(indeks)) + '\n' + Wyswietlenie_zbicia())
#koniec :)
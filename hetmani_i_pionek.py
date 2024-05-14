import random
from math import sqrt

def Hetmani(ile):
    WspHetmanow=[]
    while len(WspHetmanow)!=ile+1:
        JestDuplikat=0
        x = random.randrange(1, 8)
        y = random.randrange(1, 8)
        for a in range(len(WspHetmanow)):
            if WspHetmanow[a]==[x,y]:
                JestDuplikat=1
        if JestDuplikat==0:
            WspHetmanow.append([x,y])
    return(WspHetmanow)

WspHetmanow=Hetmani(int(input('Ile hetmanow znajduje sie na planszy?:  ')))
Pionek=WspHetmanow[len(WspHetmanow)-1]
WspHetmanow.pop()
#tworzenie hetmanow i pionka po raz pierwszy

def plansza():
    row7 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row6 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    row5 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row4 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    row3 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row2 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    row1 = ['   ', ' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ']
    row0 = [' * ', '   ', ' * ', '   ', ' * ', '   ', ' * ', '   ']
    rows = [row7, row6, row5, row4, row3, row2, row1, row0]

    for a in WspHetmanow:
        rows[8 - a[1]][a[0] - 1] = ' H '  # wyswietlanie pozycji hetmanow
    rows[8 - Pionek[1]][Pionek[0] - 1] = ' P '  # wyswietlanie pozycji pionka

    gora = ' |------------------------|\n'
    plansza = '\n' + gora
    for lista in range(len(rows)):
        plansza += (str(8 - lista) + '|')
        for element in range(len(row0)):
            plansza += rows[lista][element]
        plansza += '|\n'
    plansza += gora
    plansza += '   1  2  3  4  5  6  7  8'  # tworzenie planszy
    return (plansza)

def Pitagoras(a,b):
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)
def CzyPomiedzy(a,c,b):
    return Pitagoras(a, c) + Pitagoras(c, b) == Pitagoras(a, b)

def zbicie(H):  #H - wspolrzedne 1 hetmana
    if abs(H[0]-Pionek[0])==abs(H[1]-Pionek[1])or H[0]==Pionek[0] or H[1]==Pionek[1]:
        for a in range(len(WspHetmanow)):
            if WspHetmanow[a]!=H:
                if CzyPomiedzy(H,WspHetmanow[a],Pionek)==True:
                    return False
        return True
    return False
def Wyswietlenie_zbicia():
    Zbijajace=[]
    for a in WspHetmanow:
        if zbicie(a)==True:
            Zbijajace.append(a)
    if len(Zbijajace)==0:
        return('Zaden hetman nie moze zbic pionka')
    elif len(Zbijajace)==1:
        return('Hetman o tych wspolrzednych moze zbic pionka: '+str(Zbijajace)+'\n')
    else:
        return("Hetmany o tych wspolrzednych moga zbic pionek: " + str(Zbijajace)+'\n')
#te 2 funkcje to wsumie jedna ale latwiej mi bylo to zrobic dwoma funkcjami

print(plansza())
print(Wyswietlenie_zbicia())

while 0==0:
    akcja=int(input("Co chcesz zrobić (1,2,3 lub 4)\n\n1) Wylosowac nowa pozycje dla pionka\n2) Usuniecie dowolnego hetmana\n3) Ponowna weryfikacja bicia\n4) Zakonczyc program\n:  "))
    if akcja==4:
        break
    elif akcja==1:
        Pionek=Hetmani(0)[0]
        print(plansza())
    elif akcja==2:
        print(WspHetmanow)
        indeks=int(input('Podaj index hetmana do Usuniecia: '))
        WspHetmanow.pop(indeks)
        print(plansza())
    elif akcja==3:
        print(plansza())
        print(Wyswietlenie_zbicia())
import random
from math import sqrt

print('Ile hetmanow znajduje sie na planszy?')
k=int(input('(Od 1 do 5)\n:   '))
def Hetmani():
    WspHetmanow=[]
    while len(WspHetmanow)!=k+1:
        JestDuplikat=0
        x = random.randrange(1, 8)
        y = random.randrange(1, 8)
        for a in range(len(WspHetmanow)):
            if WspHetmanow[a]==[x,y]:
                JestDuplikat=1
        if JestDuplikat==0:
            WspHetmanow.append([x,y])
    return(WspHetmanow)

WspHetmanow=Hetmani()
Pionek=WspHetmanow[len(WspHetmanow)-1]
WspHetmanow.pop()
print(WspHetmanow, Pionek)

row7=['   ',' * ','   ',' * ','   ',' * ','   ',' * ']
row6=[' * ','   ',' * ','   ',' * ','   ',' * ','   ']
row5=['   ',' * ','   ',' * ','   ',' * ','   ',' * ']
row4=[' * ','   ',' * ','   ',' * ','   ',' * ','   ']
row3=['   ',' * ','   ',' * ','   ',' * ','   ',' * ']
row2=[' * ','   ',' * ','   ',' * ','   ',' * ','   ']
row1=['   ',' * ','   ',' * ','   ',' * ','   ',' * ']
row0=[' * ','   ',' * ','   ',' * ','   ',' * ','   ']
rows=[row7,row6,row5,row4,row3,row2,row1,row0]

for a in WspHetmanow:
    rows[8 - a[1]][a[0]-1] = ' H '  #wyswietlanie pozycji hetmanow
rows[8-Pionek[1]][Pionek[0]-1] = ' P '    #wyswietlanie pozycji pionka

gora=' |------------------------|\n'
plansza='\n'+gora
for lista in range(len(rows)):
    plansza+=(str(8-lista)+'|')
    for element in range(len(row0)):
        plansza+=rows[lista][element]
    plansza+='|\n'
plansza+=gora
plansza+='   1  2  3  4  5  6  7  8'    #tworzenie planszy
print(plansza)

#Zrobione:Generowanie planszy i pozycji pionka i hetmanow
#Do zrobienia: Sprawdzanie czy sie zbija, pozycje zbijajace i dodatkowe funkcje
#jak bedzie wstawianie nowych, niezbijajacych hetmanow to:
#wywalic te ktore zbijaja,  uzyc def Hetmani i usunac ostatni element
def Pitagoras(a,b):
    return sqrt((a[0]-b[0])**2) + sqrt((a[1]-b[1])**2)
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


Zbijajace=[]
for a in WspHetmanow:
    if zbicie(a)==True:
        Zbijajace.append(a)
print(Zbijajace)
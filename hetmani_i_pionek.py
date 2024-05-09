import random

def CzyHetmanZbije(xH, yH, xP, yP):     #xH, yH - wspolrzedne hetmana,     xP, yP - wspolrzedne pionka
    if abs(xH-xP)==abs(yH-yP):
        return True
    else:
        return False

print('Ile hetmanow znajduje sie na planszy?')
k=int(input('(Od 1 do 5)\n:   '))
def Hetmani():
    JestDuplikat=0
    WspHetmanow=[]
    while len(WspHetmanow)!=k+1:
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
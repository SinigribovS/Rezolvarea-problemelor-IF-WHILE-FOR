#Conform calendarului japonez, fiecare an poartă numele unui animal. Fiecare denumire sc repetă exact o dată la 12 ani. Deci, un ciclu este format din 12 ani cu următoarele denumiri de animale in această ordine sobolan, bou, tigru, iepure, dragon, şarpe, cal. oaie, maimuță, cocos, ciine, pore. Stiind că anul 2000 a fost anul Dragonului, să sescrie un algoritm care va citi de la tastatură anul (numär de patru cifre) şi va afisa denumirea lui conform calendarului japonez.
a=int(input('Introduceti anul = '))
if a%12==1:
    print('Sobolan')
if a%12==2:
    print('Bou')
if a%12==3:
    print('Tigru')
if a%12==4:
    print('Iepure')
if a%12==5:
    print('Dragon')
if a%12==6:
    print('Sarpe')
if a%12==7:
    print('Cal')
if a%12==8:
    print('Oaie')
if a%12==9:
    print('Maimuta')
if a%12==10:
    print('Cocos')
if a%12==11:
    print('Caine')
if a%12==12:
    print('Porc')
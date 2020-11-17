#Conform calendarului japonez, fiecare an poartă numele unui animal. Fiecare denumire sc repetă exact o dată la 12 ani. Deci, un ciclu este format din 12 ani cu următoarele denumiri de animale in această ordine sobolan, bou, tigru, iepure, dragon, şarpe, cal. oaie, maimuță, cocos, ciine, pore. Stiind că anul 2000 a fost anul Dragonului, să sescrie un algoritm care va citi de la tastatură anul (numär de patru cifre) şi va afisa denumirea lui conform calendarului japonez.
n=int(input('Introduceti anul(numar de patru cifre):'))

h=input('Inainte sau dupa Hristos(introduceti "i" sau "d")')

if h=='d':
    if n>=1996:
        l=['sobolan','bou','tigru','iepure','dragon','sarpe','cal','oaie','maimuta','cocos','caine','porc']
        i=(n-1996)%12
        print(l[i])
    elif n<1996 and n>=0:
        l=['porc','caine','cocos','maimuta','oaie','cal','sarpe','dragon','iepure','tigru','bou','sobolan']
        i=(1995-n)%12
        print(l[i])
elif h=='i':
    l=['maimuta','oaie','cal','sarpe','dragon','iepure','tigru','bou','sobolan','porc','caine','cocos']
    i=n%12
    print(l[i])

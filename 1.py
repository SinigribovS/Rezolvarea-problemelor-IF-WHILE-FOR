#Se dă numărul natural n. n apartine {28, 29, 30, 31). Să se afişeze denumirile lunilor cu numărul de zile n. De exemplu, pentru n= 30, se va afişa:aprilie, iunie, septembrie, noiembrie.
n=int(input('Dati numarul natural n: '))
if ((n<28) or (n>31)):
    print ('Nu exista o luna cu asemenea numar de zile')
else:
    if (n==30):
        print('Aprilie, Iunie, Septembrie, Noiembrie')
    if (n==31):
        print('Ianuarie, Martie, Mai, Iulie, August, Octombrie, Decembrie')
    if ((n==28) or (n==29)):
        print ('Februarie')
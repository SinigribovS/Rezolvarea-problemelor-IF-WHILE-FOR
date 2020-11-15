#Se dau numerele naturale m şi n, unde m <n. Să se verifice dacă n este o putere a lui m.
m=int(input('Dati numarul natural m (baza): '))
n=int(input('Dati numarul natural n (puterea): '))
if (n<m):
    print('Eroare: n<m')
else:
    a=True
    for i in range(1,n+1):
        if(m**i==n):
            print('Da,',n,' este putere a lui ',m)
            a=False
    if a:
        print('Nu,',n,' nu este putere a lui ',m)
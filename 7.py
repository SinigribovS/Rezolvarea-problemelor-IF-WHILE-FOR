#Mihai are un unchi bogat care i-a dăruit în ziua cînd s-a născut un dolar, iar in fiecare an următor el dubla cadoul şi mai adăuga atîția dolari cîți ani împlinea Mihai. a) Să se calculeze cîți dolari a primit Mihai atunci cînd a împlinit n ani (n <20). b) La ce vîrstă cadoul lui Mihai a fost mai mare de 100$?
import sys
n=int(input('Introduceti varsta lui Mihai  = '))
d=1
if (n>20):
    print ('Eroare (n>20)')
    sys.exit()
elif ((n<=20) and (n>=1)):
    for i in range(1,n+1):
        if (i==1):
            d=d+2
        else:
            d=(d*2)+i
print ('Mihai are = ',d,' dolari')
print ('Cadoul lui Mihai va trece de 100 de dolari la 6 ani')
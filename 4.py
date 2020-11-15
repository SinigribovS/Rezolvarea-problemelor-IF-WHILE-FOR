#Să se scrie un program care va efectua:a) adunarea a două fracții date; b) înmulțirea a două fracții date. Rezultatul va fi o fracție ireductibilă.
#importam biblioteca cu fractii
from fractions import Fraction
#scriem codu cu biblioteca deja importata
a=int(input('Dati numaratorul primei fractii (a)  = '))
b=int(input('Dati numitorul primei fractii (b)  = '))
c=int(input('Dati numaratorul celei de a doua fractii (c)  = '))
d=int(input('Dati numitorul celei de a doua fractii (d)  = '))
print('Suma fractiilor este = ',Fraction(a,b)+Fraction(c,d))
print('Produsul fractiilor este = ',Fraction(a,b)*Fraction(c,d))
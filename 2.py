#Să se calculeze 1! + 2! + 3! + ... + n! (n>1).
import math
n=int(input('Dati numarul natural nenegativ n: '))
s=0
for i in range (1,n+1):
    s+=(math.factorial(i))
print ("Suma 1!+2!+...+",n,"!= ",s)
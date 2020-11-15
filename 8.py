#Se dau numerele reale pozitive a, b, c. Să se verifice dacă există un triunghi ale cărui laturi au lungimile (in aceeaşi unitate de măsură) egale cu a, c. In caz tiv, se determine tipul triunghiului echilateral, isoscel, scalen.
a = eval(input("Dati nr 1: "))
b = eval(input("Dati nr 2: "))
c = eval(input("Dati nr 3: "))
if ((a<c+b)and(b<c+a)and(c<a+b)): 
    if ((a==b)and(a==c)and(b==c)):
         print("triunghiul e echilateral")

    if ((a==b)and(a+b>c)):
         print("tringhiul e isoscel")

    else:
         print("triungiul e scalen")
else :
    print("nu poate fi format un triunghi")  
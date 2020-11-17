#Un număr natural se numeşte număr perfect dacă este egal cu suma divizorilor lui, in afară de el însuşi. De exemplu, 6 este număr perfect, deoarece 6 = 1 + 2 + 3. Să se afle numerele perfecte mai mici decit numărul natural dat n.
p=int(input('Introduceti un numar intreg:'))
print(f'Numerele perfecte mai mici ca {p} sunt: ', end='')
for n in range(1,p):
    s=0 
    for i in range(1,n):
        
        if n%i==0:
            s+=i
    if s==n:
        print(n, end=';')
print()
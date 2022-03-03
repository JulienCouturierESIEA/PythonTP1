n = int(input())
compteur = 0
while(n != 1):
    if(n%2 == 0):
        n = n//2
    else:
        n = (3*n + 1)
    compteur += 1
    print(n)
print("Au bout de {0} itérations".format(compteur))
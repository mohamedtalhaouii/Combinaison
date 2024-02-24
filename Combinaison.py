#Mohamed Talhaoui
#La fonction factoriel
def factoriel(N : int):
    if N == 0:
        return 1
    elif N > 0:
        F = 1
        for i in range(1,N+1):
            F = F * i
        return F

#Combinaison
N = int(input("n? : "))
P = int(input("p? : "))
if N > P:
  C = int(factoriel(N)/(factoriel(P) * factoriel(N - P)))
  print("La Combinaison est : ",C)
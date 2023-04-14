L = [8,24,27,48,2,16,9,7,84,91]
long = len(L)
sommme_paire = 0
for i in range (long) :
     if L[i] %2 == 0 :
          sommme_paire = sommme_paire + L[i]
print ("Somme valeurs paires : ", sommme_paire)
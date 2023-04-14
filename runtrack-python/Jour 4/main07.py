L = [8, 24, 48, 2, 16]
long = len(L)

mult3=0
for i in range (long) :
     if L[i] %3 == 0 :
          mult3 = mult3 + 1
print ("Nombre multiples 3 : ", mult3)
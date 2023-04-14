for nombre in range (1,1000):
    if nombre > 1:
        for i in range (2,nombre):
            if (nombre % i ) == 0:
                break
        else:
                print(nombre)
                




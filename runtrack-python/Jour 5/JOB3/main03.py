def tapis(n):
    print("+"+"-"*(n+1)+"+")
    for i in range(n+1):
      print("|"+"#"*(n-i)+" "+"#"*i+"|")  
    print("+"+"-"*(n+1)+"+")
tapis(10)
    



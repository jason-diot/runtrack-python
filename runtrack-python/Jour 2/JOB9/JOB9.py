def triangle(a,b,c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            print("triangle equilateral")

        elif a == b or a == c or b == c:
            if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("triangle isocele et rectangle")
            else:
                print("triangle isocele")
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
                print("triangle rectangle")
        else:
             print("triangle quelconque")


triangle(5,5,5)
triangle(4,4,6)
triangle(50,50,100)
triangle(3,4,5)


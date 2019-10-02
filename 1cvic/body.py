import turtle
import math



def lol(a):
    b = a
    for i in range(5):
        #def kresli(i)
        turtle.forward(a)
        turtle.left(90)
        turtle.forward(b)
        turtle.left(90)
    #print(math.radians(math.tan(1)))
        uhol = math.degrees( math.atan(b/a))
        uhol =  90 - uhol
       # deg = uhol
        print(str(uhol) +" " +  str(a))# + "  " + a + " " + b )

        turtle.left(90 - uhol)
    #print(math.sqrt(100*100+100*100))
        c = math.sqrt(a**2+b**2)
        turtle.forward(c)
        a = c
        turtle.left(180)
        
    return;
lol(100)

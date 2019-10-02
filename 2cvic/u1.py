import math

def priemer_troch( a,b,c):
        return((a+b+c)/3)
def pis(n):
    for i in range(n):
            print(i+1)
    return
def sto(n):
    for i in range(n):
        print(i+101)
    return
def par(n):
    
    for i in range(n):
        print( i * 2  + 2)

    return

def opak(n):
    for i  in range(n  ):
        print( n - i )

    return
def suc(n):
    su = 0
    for i in range(n):
            su +=  (i+1)**2
    return su

def grid(n):
   #print('*' , end=' ')
    # stlce
    r = n * 5
    for a in range (r + 1):
        if( a % 5 == 0):
            for x in range(n):
                print('* - - - -' , end=' ')
            print('*')
        else:
            for x in range(n):
                print('|        ' , end=' ')
            print('|')
                
##    print('*' , end=' ')
##    print('-')

    
    return

grid(3)
grid(4)


#print(suc(3))

#opak(5)
#par(10)
#sto(3)
#pis(10)
#print(priemer_troch(5,6,7))

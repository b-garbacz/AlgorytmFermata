import math
## Te wartości w komentarzach opierają się na wcześniejszym przeliczeniu faktoryzacji n=  92843
#pozostawiam printy dla lepszej widoczności co się dzieje w funkcjiS
def fermat(n):
    t = math.floor(math.sqrt(n)) + 1 # =305
    print(t)
    x = (t**2) -n # = 182
    print(x)
    y=math.sqrt(x) #=13.73 nie jest calkowite
    print(y)
    while not y.is_integer():
        t = t + 1 #306
        print(t)
        x = (t ** 2) - n # =793
        y=math.sqrt(x) # 13 iteracja  daje 8281 ktore sie pierwiastuje w liczbe calkowita czyli to s^2
        print(y)
    print(t)
    print(y)
    p = (t + y)
    q = (t - y)
    return t,y,p,q

n=int(input("Podaj liczbe do Faktoryzacji:")) #92843
x,y,p,q=fermat(n)
print('$$$$$$$$$$$$$$$$$$$Algorytm fermata$$$$$$$$$$$$$$$$$$$$$$$$')
print('t=',x)
print('s=',y)
print('p=(t+s)=',p)
print('q=(x-y)=',q)
pq=int(p*q)
print('p*q=',pq)
print('$$$$$$$$$$$$$$$$$$$Algorytm fermata$$$$$$$$$$$$$$$$$$$$$$$$')

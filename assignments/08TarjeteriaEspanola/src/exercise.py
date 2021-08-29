def func (a,b):
    x= a*12
    y= b*35
    if x > y:
        return y
    if y > x:
        return x
def main():
    #escribe tu código abajo de esta línea
    x=int(input("Dame la cantidad de pliegos de papel albanene: "))
    y= int(input("Dame el numero de plumones: "))
    num = func(x,y)
    print("El numero maximo de tarjetas que se pueden hacer es: " + str(num))
    
    pass

if __name__=='__main__':
    main()

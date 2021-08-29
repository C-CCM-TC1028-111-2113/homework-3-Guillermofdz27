def area (x,y):
    w= x*y
    return w
def main():
    #escribe tu código abajo de esta línea
    x=float(input("Dame la base: "))
    y= float(input("Dame la altura: "))
    area= area(x,y)
    print("El area del rectangulo es: " + str(area))
           
    pass

if __name__=='__main__':
    main()

def area1(x,y):
    area = (x)*(y)
    return area
def vol (x,y,z):
    area= area1(x,y)
    volumen = (z)*(area)
    return volumen
def main():
    #escribe tu código abajo de esta línea
    x= (float(input("Dame la base: ")))
    y= (float(input("Dame la altura: ")))
    z= (float(input("Dame la profundidad: ")))
    v= vol(x,y,z)
    print("El volumen del prisma es: " + str (v))
    pass

if __name__=='__main__':
    main()

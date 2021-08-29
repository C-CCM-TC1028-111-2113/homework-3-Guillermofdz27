def es_bisiesto (x):
    if x%4==0:
        return "True"
    elif x%100==0:
        return "False"
    elif x%400==0:
        return "True"
    else:
        return "False"
def main():
    #escribe tu código abajo de esta línea
    x= int(input("Dame el año: "))
    y= es_bisiesto (x)
    print(str(y))


    pass

if __name__=='__main__':
    main()

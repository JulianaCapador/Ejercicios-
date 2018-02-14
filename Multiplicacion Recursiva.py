def multiplicacion(fact1,fact2):
    if(fact1 ==0 or fact2 ==0):
        return 0
    else:
        return fact1+multiplicacion(fact1,fact2-1)

print(multiplicacion(5,12))

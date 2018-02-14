def potencia(num,pot):

    if(pot == 0):
        return 1
    else:
        return num*potencia(num,pot-1)

print(potencia(3,4))

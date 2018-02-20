def invertir(num,inver):
    if num == 0:
        return inver
    else:
        return invertir(num//10,inver*10+num % 10)
    

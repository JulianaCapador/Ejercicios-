
# 9 Longitud
def longitud(num):
    if num/10<1:
        return    1
    else:
        return 1+longitud(num/10)


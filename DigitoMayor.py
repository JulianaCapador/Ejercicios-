def DigitoMayor( Num):
    if Num < 10:
        return Num;
    elif (Num%10)<=DigitoMayor(Num//10):
        return DigitoMayor(Num//10);
    else:
        return Num%10


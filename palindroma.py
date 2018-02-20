def palindromo(n):
    if len(str(n))<=1:
       return True
    elif str(n)[0]==str(n)[len(str(n))-1]:
    	  return palindromo(str(n)[1:len(str(n))-1])
    else:
        return False

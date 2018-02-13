def fibonacci(n):

    if(n==0 or n==1):
        return 1
    else: 
        return fibonacci(n-1)+fibonacci(n-2)


fibonacci(3)

print(fibonacci(1))

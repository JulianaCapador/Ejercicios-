def div(num1,num2):
    
    if(num1 == num2):
        return 1
    else:
        return 1+ div(num1-num2,num2)

print(div(16,4))

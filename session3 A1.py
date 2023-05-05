import math
num1=float(input(" enter num1:"))
num2=float(input("enter num2 :"))
    
    # num3=int(input("enter num3:"))
    # op= +,-,*,/
op= input("enter op(+,-<*,/,√,sin,cos,!,tan,cot,exit):")
while True:
    if op== "+":
            result= num1+num2
            
    if op=="-":
            result= num1-num2
    if op=="*":
            result= num1*num2
    if op== "/":
        if num2==0:
                result=("error")
        else:
            result= num1/ num2
    if op=="√" :
        result=math.sqrt(num1)
    if op=="sin" :
        result=math.sin(num1)
    if op=="cos" :
        result=math.cos(num1)
    if op=="!" :
        result=math.factorial(int(num1))
    if op=="tan" :
        result= math.tan(num1)
        
   # if op=="cot" :
       # couldn't find the formula 
    if op=="exit":    
        result= "run again"
        break
        
        
    print("result",result)
    break
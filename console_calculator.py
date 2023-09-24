select = " 1) Addition 2) Substraction 3) Multiplication"
print(select)

choose = input("Which Operation Do You Want To Perform?")

firstNumber = int(input("Input first number: "))

secondNumber = int(input("Input second number: "))


symbols = ["+","-","x","/"]

isRunning = False
while not isRunning:
    for x in symbols:
        if choose == x:
            if x == "+":
                    result = firstNumber + secondNumber
                    print(result)    
            if x == "-":
                result = firstNumber - secondNumber
                print(result)
                
            if x == "*":
                result = firstNumber * secondNumber
                print(result)
                
            if x == "/":
                result = firstNumber / secondNumber
                print(result)
       
    break



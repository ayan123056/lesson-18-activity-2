try:
    num1, num2 = eval(input("enter two numbers, seperated by a coma :"))
    result = num1 / num2
    print('result is',result)
except ZeroDivisionError:
    print("division by zero is error ")
except SyntaxError:
    print('comma is missing. Enter numbers seperated by comma like this 1,2')
except:
    print("wrong input")
else:
    print("no exception")
finally:
    print('THIS WILL EXECUTE NO MATTER WHAT. I PROMISE U')
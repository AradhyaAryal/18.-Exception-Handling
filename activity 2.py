try:
    num1, num2 = eval(input("Enter a two numbers with a comma between them: "))
    result =   num1 / num2
    print(result)
except ZeroDivisionError:
    print("An Error of dividing a number with a zero!!")
except SyntaxError:
    print("No comma added.")
except:
    print("Wrong input")
else:
    print("No exeptions")
finally:
    print("This will execute the program no matter what.")
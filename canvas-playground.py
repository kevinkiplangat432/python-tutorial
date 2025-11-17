def divide (num1, num2):
    try:
        quotient = num1 /num2
        print(quotient)
    except:
        print("an error occurred")
divide(20, "")
divide(20,4)


def divide1(num1, num2):
    try:
        quotient = num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error: num2 cannot be equal to 0")
    except TypeError:
        print("Error: input must be of type int or float")
    finally:
        print("Isn't division fun?")

divide1(20,4)




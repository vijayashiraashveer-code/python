try:
    a, b= eval(input("Enter two numbers"))
    print(a/b)
except ZeroDivisionError:
    print("cant divide by 0 ")
except SyntaxError:
    print("use comma")
except:
    print("invalid")
finally:
    print("done")

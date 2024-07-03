def main():
    a=int(input("a: "))
    op=input("operation: ")
    b=int(input("b: "))
    while a and b and b:
        if op =="+":
            print(add(a,b))
            break
        elif op =="-":
            print(sub(a,b))
            break
        elif op =="*":
            print(multi(a,b))
            break
        elif op=="/":
            print(div(a,b))
            break
        else:
            print("Invalid operation!")
            break
def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def multi(a,b):
    return a*b

def div(a,b):
    if b ==0:
        return "Error: Division by zero"
    elif a==0:
        return 0
    return a/b

main()
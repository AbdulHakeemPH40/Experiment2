text = "  Hello, World!  "
cleaned_text = text.strip()
print(cleaned_text)


def greet(name):
    print("Hello,"+name+"!")

greet("John")


def calclulate(a,b):
    sum = a + b
    sum2 = a - b
    sum3 = a * b
    sum4 = a / b 
    return sum,sum2,sum3,


result = calclulate(5,3)

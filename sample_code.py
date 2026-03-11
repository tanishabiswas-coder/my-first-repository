#sample code in python
def greet(name):
    return f"Hello, {name}!"
if __name__ == "__main__":
    name = input("Enter your name: ")
    print(greet(name))
def add(a, b):
    return a + b
if __name__ == "__main__":
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    print(f"The sum is: {add(num1, num2)}")
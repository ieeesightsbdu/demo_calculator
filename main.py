#this is the main python folder
from add import addition
from multiply import mult
from sub import sub


def main():
    num1 = int(input("Enter the number:"))
    num2 = int(input("Enter the second number:"))

    results = [addition(num1, num2), sub(num1, num2), mult(num1, num2)]

    for i in results:
        print(i)

if __name__ == "__main__":
    main()

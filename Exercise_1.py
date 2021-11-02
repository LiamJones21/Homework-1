# Write a program that receives an input from the terminal (using input()).
# This input needs to be an integer. Assign it to a variable named "n". The program will 
# compute the product n*nn*nnn and print it on the screen.
# example: n = 5 output = 5*55*555 = 152625

def output(n):
    index = 1
    multiplication_Output = 1
    while index < 4:
        num = int(str(n)*index)
        multiplication_Output = multiplication_Output * num
        index = index + 1
        

    print (multiplication_Output)


def enter_Value():
    n = int(input("Please enter a integer"))
    output(n)

try:
    enter_Value()
except:
    print('That was not a integer,')
    enter_Value()

#Brandon Dickson
#04.12.14
#Functions revision exercise 2


def enter_number():
    number=int(input("Please enter an odd number:"))
    if number % 2 != 0:
        print("Number is odd.")
    else:
        print("This number is even.")
        enter_number()
    return number

def pyramid(number):
    rows = number
    for i in range(rows):
        print (" " *(rows-i-1) + "*" *(2*i+1))
    return ""
    







#main program
number= enter_number()
stars=pyramid(number)
print (stars)
  


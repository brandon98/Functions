#Brandon Dickson
#02/12/2014
#Functions revision ex 1

def input_details():
    number=int(input("Please enter any whole number:"))
    symbol=input("Please enter a character symbol:")
    return number,symbol

def program(number,symbol):
    for count in range(number):
       print(symbol, end=" ")
    return ""
       


#Main program
number,symbol=input_details()
final_message=program(number,symbol)
print (final_message)
       

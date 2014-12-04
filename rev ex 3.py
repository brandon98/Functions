#Brandon Dickson
#04.12.14
#Revision exercise 3

def ask():
    integer1=int(input("Please enter a number:"))
    integer2=int(input("Please enter another number:"))
    return integer1,integer2


def sort(integer1,integer2):
    if integer1 > integer2:
        print(integer1,integer2)
    else:
        print(integer2, integer1)
    return ""


#Main program

integer1,integer2=ask()
answer=sort(integer1,integer2)
print(answer)

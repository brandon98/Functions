#Brandon Dickson
#04.12.14
#Revision exercise 4

def input_temp():
    tempFahrenheit=int(input("Please enter temperature in fahrenheit:"))
    return tempFahrenheit

def conversion(tempFahrenheit):
    celcius= (tempFahrenheit -32) * (5/9)
    print("Temperature in celsius is:", tempFahrenheit)
    return ""


#Main Program

tempFahrenheit=input_temp()
answer=conversion(tempFahrenheit)
print(answer)

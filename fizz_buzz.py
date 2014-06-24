
import sys


with open ('fizz_buzz.txt', 'r') as data_file:
    input_file = data_file.read().splitlines()


for aline in input_file:
    values = aline.split()
    number1 = int(values[0])
    number2 = int(values[1])
    rangeval = int(values[2])
    a = range(1,rangeval+1)

    for number in a:
        if number%number1==0 and number%(number1*number2)!=0:
            sys.stdout.write("F")
            sys.stdout.write(" ")
        elif number%number2==0 and number%(number1*number2)!=0:
            sys.stdout.write("B")
            sys.stdout.write(" ")
        elif number%(number1*number2)==0:
            sys.stdout.write("FB")
            sys.stdout.write(" ")
        else:
            sys.stdout.write (str(number))
            sys.stdout.write(" ")
    sys.stdout.write('\n')
    

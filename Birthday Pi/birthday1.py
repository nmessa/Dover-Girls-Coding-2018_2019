## Finding your birthday in Pi
## Author: nmessa
## This program will find the location of a birthday in the first
## million/billion digits of Pi

filename = 'pi_million_digits.txt'
#filename = 'pi-billion.txt'

with open(filename) as file_object:
    pi_string = file_object.read()

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    index = pi_string.find(birthday)
    print("Your birthday appears in the first million digits of pi!")
    print ('At location', index)
else:
    print("Your birthday does not appear in the first million digits of pi.")

## Output
## Enter your birthday, in the form mmddyy: 090852
## Your birthday appears in the first billion digits of pi!
## At location 1222420

import random
import string

#Prompt user to enter length of the password.
l = int(input("Enter Length: "))

char = string.ascii_letters
char += string.digits
char += string.punctuation

random_password = ""

#Run the loop l number of times.
for i in range(l):
    next_char = random.choice(char)
    random_password += next_char
    
print("Your password is: ", random_password)
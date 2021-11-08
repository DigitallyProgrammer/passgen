from random import randint
from random import *

# Password generation


def passgen():
    password = ""
    for i in range(5):  # repeats the loop 5 times
        i = chr(randint(65, 90))  # gets the uppercase letters
        for j in range(5):  # repeats 5 times along with the main loop
            j = chr(randint(65, 90)).lower()  # picks the random letters
        for k in range(5):  # same as the first nested loop
            # picks a random number from the range 0 - 100
            k = str(randint(0, 100))
        # concatenates the different values from the loop
        password = str(password) + i + j + k
    print(password)


passgen()

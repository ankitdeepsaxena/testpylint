'''
This is a test code
'''
# Program to check if a NUMber is prime or not

def sum():
    a=20
    b=30
    return a+b

NUM = 29

# To take input from the user
# NUM = int(input("Enter a NUMber: "))

# define a FLAG variable
FLAG = False

# prime NUMbers are greater than 1
if NUM > 1:
    # check for factors
    for i in range(2, NUM):
        if (NUM % i) == 0:
            # if factor is found, set FLAG to True
            FLAG = True
            # break out of loop
            break

# check if FLAG is True
if FLAG:
    print(NUM, "is not a prime NUMber")
else:
    print(NUM, "is a prime numberss")

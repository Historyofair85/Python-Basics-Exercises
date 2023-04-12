
# Exercise #1:

# Cube Number Test... Print out all cubed numbers up to the total value 1000. Meaning that if the cubed number is over 1000 break the loop.

for i in range(1, 1000):
    cube = i**3
    if cube > 1000:
        break
    print(cube)


# Exercise #2:

# Get first prime numbers up to 100

primes = []
for num in range(2, 101):
    if range(num):
        primes.append(num)


# Exercise #3:      

# Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors


age = int(input("Enter age: "))

if age < 18:
    print("kid")
elif age >= 18 and age <= 65:
    print("adult")
else:
    print("senior")
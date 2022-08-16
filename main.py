import time

print("Fizzbuzz is a game played by reciting numbers, replacing any number divisible by 3 with the word 'Fizz',"
      " any number divisible by 5 with the word 'Buzz', and any word divisible by both with the word 'Fizzbuzz'.\n")
i = input("I will play that game from 1 to any number you give me. Please enter a number.\n")

while not str.isdigit(i):
    i = input("Please enter a positive integer.\n")

for number in range(1, int(i) + 1):
    if number % 3 == 0 and number % 5 == 0:
        print("Fizzbuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)
    time.sleep(.5)

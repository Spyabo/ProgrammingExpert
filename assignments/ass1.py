import random
# while loop to error check the range input

while True:
    try:
        start_range = int(input("Enter the start of the range: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    except TypeError:
        print("Please enter a valid number.")
        continue
    break

while True:
    try: 
        end_range = int(input("Enter the end of the range: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    except TypeError:
        print("Please enter a valid number.")
        continue
    if start_range > end_range:
        print("Please enter a valid number.")
    else: break

# generate the random value
randomval = random.randint(start_range, end_range)
counter = 0
# while loop to check each guess
guess=-1
while guess != randomval:
    try:
        guess = int(input("Guess a number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    except TypeError:
        print("Please enter a valid number.")
        continue
    counter += 1

if counter > 1:
    print(f"You guessed the number in {counter} attempts")
else: 
    print(f"You guessed the number in {counter} attempt")
    

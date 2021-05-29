# This calculates either a human's age in months or dog's age in human years.

print("We're doing age calculations here. Do you want your age in months or your dog's age in human years?\n")
choice = input("Enter 'human' or 'dog':\n")
if choice == 'dog':
    print("Alright, we\'re going to calculate your dog\'s age in dog years. Let's go!\n")
    # sleep = 1   (How do you write a time delay in a Python program?)
    dogName = input("What is your dog's name?\n")
    dogDogAge = input('Got it. How old is ' + dogName + '?\n')

    # Here, we convert the dog's age from a string (dogIntAge) to a float (dogNewAge)
    # and back to a string (dogHumanAge) that can be read in the print statement:
    dogIntAge = float(dogDogAge)
    dogNewAge = (dogIntAge * 7)
    dogHumanAge = str(dogNewAge)

    # Prints the statement, using the dog's name and dog's human age:
    print('Cool. Your dog, ' + dogName + ', is ' + dogHumanAge + ' in human years.')

elif choice == 'human':
    print("Alright, we're going to calculate your human age in months. Let's go!\n")
    # sleep = 1   (How do you write a time delay in a Python program?)
    humanName = input("What is your name?\n")
    humanAge = input('Got it. How old are you, ' + humanName + '?\n')

    # Here, we convert the human's age from a string (humanAge) to a float (humanNewAge)
    # and back to a string (humanMonthAge) that can be read in the print statement:
    humanFloatAge = float(humanAge)
    humanNewAge = (humanFloatAge * 12)
    humanMonthAge = str(humanNewAge)

    # Prints the statement, using the dog's name and dog's human age:
    print('Cool. You, ' + humanName + ', are ' + humanMonthAge + ' months old.')

else:
    print("That input won't work. Please enter 'human' or 'dog'.")
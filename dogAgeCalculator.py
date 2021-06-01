# This calculates either a human's age in months or dog's age in human years.

print("We're doing age calculations here. Do you want your age in months or your dog's age in human years?\n")
choice = input("Enter 'human' or 'dog':\n")
if choice == 'dog':
    print("Alright, we\'re going to calculate your dog\'s age in dog years. Let's go!\n")
    # sleep = 1   (How do you write a time delay in a Python program?)
    dog_name = input("What is your dog's name?\n")
    dog_age = input('Got it. How old is ' + dog_name + '?\n')

    # This version decreases the number of variables involved in converting dog_age input()
    # to an int for multiplication and back to string:
    human_age = int(dog_age) * 7
    human_age = str(human_age)

    # Prints the statement, using the dog's name and dog's human age:
    print('Cool. Your dog, ' + dog_name + ', is ' + human_age + ' in human years.')

elif choice == 'human':
    print("Alright, we're going to calculate your human age in months. Let's go!\n")
    # sleep = 1   (How do you write a time delay in a Python program?)
    human_name = input("What is your name?\n")
    human_age = input('Got it. How old are you, ' + human_name + '?\n')

    # Here, we convert the human's age from a string (humanAge) to a float (humanNewAge)
    # and back to a string (humanMonthAge) that can be read in the print statement:
    human_month_age = int(human_age) * 12
    human_month_age = str(human_month_age)

    # Prints the statement, using the dog's name and dog's human age:
    print('Cool. You, ' + human_name + ', are ' + human_month_age + ' months old.')

else:
    print("That input won't work. Please enter 'human' or 'dog'.")
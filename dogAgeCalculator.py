# This program calculates a dog's age by taking input for dog name & age
# before printing a statement that returns dog name and dog dog age.

choice = input("We're doing age calculations here. Do you want your age in months or your dog's age in human years?\n")



print("Alright, we\'re going to calculate your dog\'s age in dog years. Let's go!\n")
# sleep = 1   (How do you write a time delay in a Python program?)
dogName = input("What is your dog's name?\n")
dogDogAge = input('Got it. How old is ' + dogName + '?\n')

#dogIntAge = int(dogDogAge)
dogIntAge = float(dogDogAge)
dogNewAge = (dogIntAge * 7)
dogHumanAge = str(dogNewAge)

print('Cool. Your dog, ' + dogName + ', is ' + dogHumanAge + ' in human years.')
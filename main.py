import random
number=random.randint(1,6)
guess=int(input("Enter a number from 1 to 6:"))

if guess==number:
 print("Correct!")

else:
 print ("Incorrect.")
print ("The number was", number)
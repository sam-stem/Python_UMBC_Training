#Print out equal signs for title
print("====================================================================")
#Print blank line
print()
#prints out title content
print("Welcome to the UMBC Custom Car Selection Form")
#prints out the equals signs for formatted title
print("====================================================================")
#prints out 2 blank lines for formatting
print()
print()
#prints out another title
print("================== Car Make and Model ===============================")
# Question 1
print(">>>> 1. What make and model of car are you ordering?<<<<")
print("        a. Subaru Impreza 2022")
print("        b. Toyota Corolla 2017")
print("        c. Honda Insight 2021")
print("        d. Tesla Model 3 2020")
#Print blank line
print()
choice = input("Please enter 'a'- 'd' from the selection above: ")
#prints out 2 blank lines for formatting
print()
print()
# Question 2
print(
  ">>>> 2. Would you like to upgrade from the 4 door option to the 2 door option?<<<<"
)
choice2 = input("Please enter 'yes' or 'no': ")
#print blank line
print()
print("================== Exterior ===============================")
#prints blank line
print()
# Question 3
print(">>>> 3. What colour would like your car to be?<<<<")
choice3 = input("Please enter any color you would like: ")
#prints blank line
print()
# Question 4
print(">>>> 4. Would you like the deluxe weather package?<<<<")
choice4 = input("Please enter 'yes' or 'no': ")
#prints blank line
print()
print("================== Engine Selection ===============================")
print(">>>> 5. Which engine would you like your car to have?<<<<")
print("        a. I-4 Entry Engine")
print("        b. V-6 Performance Engine")
print("        c. Eco Diesel Engine")
choice5 = input("Please select 'a'-'c': ")
#prints blank line
print()
print(">>>> 6. Would you like heated seats?<<<<")
choice6 = input("Please enter 'yes' or 'no': ")
#print 2 blank lines
print()
print()
print()
print("----------------------------------------------------------------------")
print(
  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Summary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print(f"Model option: {choice}")
print(f"Upgrade to 2-door: {choice2}")
print(f"Desired color: {choice3}")
print(f"Upgrade to Delux Weather: {choice4}")
print(f"Engine option: {choice5}")
print(f"Upgrade to heated seats: {choice6}")
print(
  "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Summary~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

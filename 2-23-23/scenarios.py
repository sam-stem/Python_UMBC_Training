#You need to centre each line separately:
###
#'\n'.join('{:^80}'.format(s) for s in message.split('\n'))

# Intro
print(
  "*****************Darkness from yonder in a Galaxy beknowst to its people , the journey of jon squire lead him down a few paths as he made his noble journey through the lost kingdom of Aixyah to become a reknowned Knight*****************************"
)
storySelect = input("Please enter 'a'-'c' to embark on each encounter: ")
# Pick a story 1
if (storySelect == 'a'):
  print(
    "Greetings jon squire, I see that some of my local cultivations interests you as you travel through town. May I interest you in some of the fruits of my labor?"
    "\n[enter choices]")
  print(
    "Please select as you desire \n'a.' Decadent strawberries \n'b.'plump peaches \n'c.'Tart kiwis"
  )

  choice1 = input(
    "\nChoose wisely cause i can only aid you once at no cost to you: ")
  if (choice1 == "b"):
    print(
      f"\nalas you have made the right selection these peaches shall provide you with strength for centuries to come"
    )
  else:
    print(
      f"\nSorry young squire it seems that item is no longer available given festering pests in my garden"
    )
# Pick a story 2
elif (storySelect == 'b'):
  print(
    "\nAs the local blacksmith I want to reward you with an honorary shield so that the squire is safe whilst in battle"
  )
  choice2 = input(
    "Please select the most durable material.\n\nGold\n\nPlatinum\n")
  if (choice2 == "Gold"):
    print(
      f"Your formidable strength will be unstoppable, the {choice2} shield shall protect you surely at battle"
    )
  else:
    print(
      f"\nAlas, squire what has made you make such a poor  decision, a {choice2} shield will provide little to no protection you shall crumble at the site of battle "
    )

# Pick a story 3
else:
  print(
    "\nAs the town lead general, you have yet but one step to reach before you are deemed ready for battle. Riddle me this. A right triangle with two opposing legs of length 3 and 4, respectively. What is the final length of the hypothenuse?"
  )
  choice3 = int(input("\nPlease enter the correct hypothenuse length: "))
  if (choice3 == 5):
    print(
      f"\nThat is the correct answer, the hypothenuse length of {choice3} is a response deemed for those only with a ironclad mind of a scholar you sure are ready for battle"
    )
  else:
    print(
      f"\nWoah sorry young squire, {choice3} is an incorrect response. unfortunately, you will now be stripped of your duties"
    )

#https://trinket.io/python3/e55772d7d3
import random
numofplay = []
choicelist = []
print("Random Russian Roulette: Safe edition!")
print("")
print("Each turn is random instead of one after the other, so you may go twice in a row!")
print("")
players = int(input("how many players: "))
if players > 6:
  print("too many players!")
elif players < 2:
  print("You aren't gonna win by yourself dude")
play1 = input("What's player 1's name: ")
numofplay.append(play1)
choicelist.append(play1)
if players > 1:
  play2 = input("What's Player 2's name: ")
  numofplay.append(play2)
  choicelist.append(play2)
  if players > 2:
    play3 = input("What's Player 3's name: ")
    numofplay.append(play3)
    choicelist.append(play3)
    if players > 3:
        play4 = input("What's Player 4's name:")
        numofplay.append(play4)
        choicelist.append(play4)
        if players > 4:
          play5 = input("What's Player 5's name:")
          numofplay.append(play5)
          choicelist.append(play5)
          if players > 5:
              play6 = input("What's Player 6's name:")
              numofplay.append(play6)
              choicelist.append(play6)
while len(numofplay) > 1:
  goes1 = random.choice(numofplay)
  other = random.choice(choicelist)
  print((goes1) + " goes now!")
  choice1 = int(input("hit yourself(1) or a random player(2)"))
  if choice1 == 1:
    rand1 = random.randint(1,6)
    if rand1 == 1:
      numofplay.remove(goes1)
      print (goes1 + " was hit!")
    else:
     print(goes1 + " was spared!")
  elif choice1 == 2:
    choicelist.remove(goes1)
    print(other + " was chosen to get aimed at")
    rand2 = random.randint(1,6)
    choicelist.append(goes1)
    if rand2 == 1:
      numofplay.remove(other)
      print(other + " was hit!")
    else:
      print(other + " was spared! now it's " + goes1 + "'s time to go!")
      rand3 = random.randint(1,5)
      if rand3 == 1:
          numofplay.remove(goes1)
          print(goes1 + " was hit!")
      else:
          print(goes1 + " was spared!")
  else:
    raise Exception("Not an option!")
    
if len(numofplay) == 1:
  print(*str(*numofplay) + " wins!")

  


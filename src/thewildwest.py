import random

card_types = {
  'ace': 1,
  'two': 2,
  'three': 3,
  'four': 4,
  'five': 5,
  'six': 6,
  'seven': 7,
  'eight': 8,
  'nine': 9,
  'ten': 10,
  'jack': 10,
  'queen': 10,
  'king': 10
}


class Card:

  def __init__(self, name, value):
    self.name = name
    self.value = value


  def __repr__(self):
    return f"{self.name}, {self.val}"

deck = []
for key, value in card_types.items():
  for reps in range(4):
    deck.append(Card(key, value))

player_hand = []
dealer_hand = []

def draw_card(hand):
  index = random.randrange(0, len(deck))
  hand.append(deck.pop(index))







Ace = input("Would you like the value of your ace to be 1 or 11? Please make your input a number value.").lower()
Two = 2
Three = 3
Four = 4
Five = 5
Six = 6
Seven = 7
Eight = 8
Nine = 9
Ten = 10
Jack = 11
Queen = 11
King = 11

print("Howdy partner and welcome to the Wild, Wild, West")
do_they_want_to_play = input("Are you sure you want to go on an adventure? You might not be ready for this... Yes or no?").lower()

#This whole paragraph below on line 8 is just to set up the storyline of the game... Everything above that is just to make a smoother enterance to the game as well.

if do_they_want_to_play == "no":
  print("Probably a good decision.")
elif do_they_want_to_play == "yes":
  player_name = input("Well, let me tell you, you got a lotta confidence walking in this town when Big Bill's around. What's your name?: ")
  print(f"Nice to meet you, {player_name}. Crazy stuff's been going down in this ol' boom town as of late, eh? For the past few weeks Big Bill has been robbing our banks, taking our crop, and running around with his two pals Jumpin' Joe and Rockin' Ricky. We sure could use a hero. Say... you said you wanted an adventure. Well I've got a plan to take down Big Bill and his crew. Let me explain: Step 1- Take down Jumpin' Joe at the casino by beating him in his challenge. Step 2- Rockin' Ricky is taking the Railways to Crystal City next week for the weekend, knock his train off the tracks and get a sweet victory. And finally... Step 3- Find and eliminate Big Bill at High Noon this Sunday. And just like that you could save this town.")
  input("Are you ready?: ")
  print("")
  print("Doesn't matter anyway. You're in this town; you might as well try to save it")
  print("")
  print("")
  print("Level 1... Jumpin' Joe's Casino")
  print("")
  print(f"Howdy Ho there parter. I'm Jumpin' Joe. I've heard you've been coming for me, {player_name}. Well I've got good news for ya. I'm the best blackjack player in the land West of the Mississippi. And because of that I'll make you  a deal, if you beat me in a round of blackjack, I'll run away to Jamaica, never to cause this town trouble again, but if I beat you... then you get sent to Davy Jones' Locker on the next ship back to China.")
  #storyline has been setup all the way to the first of three levels.
  #Code coming up is used to play the first level, a game of blackjack which should be made so that the user has a good chance of winning.
  BJ_inst = input("Do you know how to play Wild Wild West Blackjack?(Yes or No): ").lower()
  if BJ_inst == "yes":
    print("Good")
  elif BJ_inst == "no":
    print("Well here's the rundown on how to play: You will be randomly dealt two cards. Your objective is to get the sum of the two cards, where face cards are worth 10 and Aces are worth either 1 or 11 based on your decision, to equal 21. If you wish to draw another card to get your sum higher you may, but beware, if your new card results in a sum higher than 21, you automatically lose. The other way to lose would be to have the dealer, who is playing the same game as you, to get closer to 21 as his sum than you. If you lose three games you will be eliminated and Jumpin' Joe will exile you, but if you come out victorious at least once, Jumpin' Joe will run out of town... Good Luck!")




# black jack psuedocode:
  #define deck
  #draw 10 or so random cards from the deck and keep them as variables
  #create a function and run it, the function should ask the player if they want another card depending on what cards they have. if the sum of their cards is over 21 then they automatically lose, if under 21 present them with the choice again, if at 21 they automatically win. the function should also have the dealer draw another card if their sum is under 21. determine who has more points












else:
  print("Partner, you done messed up... click run again.")
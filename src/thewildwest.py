# import random


# print("Howdy partner and welcome to the Wild, Wild, West")
# do_they_want_to_play = input("Are you sure you want to go on an adventure? You might not be ready for this... Yes or no?").lower()

# #This portion of code is all for blackjack

# if do_they_want_to_play == "no":
#     print("Probably a good decision.")

# def score_in_hand(hand):
#             sum = 0

#             Two_thru_K = [card for card in hand if card != 'A']
#             Aces = [card for card in hand if card == 'A']

#             for card in Two_thru_K:
#                 if card in 'JQK':
#                     sum += 10
#                 else:
#                     sum += int(card)

#             for card in Aces:
#                 if sum <= 10:
#                     sum +=11
#                 else:
#                     sum += 1

#             return sum


# def run_blackjack():
#     wins = 0
#     losses = 0

#     while wins != 3 and losses != 3:
#         card_types = [
#         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
#         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
#         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
#         '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A',
#         ]


#         random.shuffle(card_types)

#         # Plan for Blackjack
#             #Deal 2 cards to the player and the dealer and show the player who has what, one dealer card must be secret

#         dealer_hand = []
#         player_hand = []

#         player_hand.append(card_types.pop())
#         dealer_hand.append(card_types.pop())
#         player_hand.append(card_types.pop())
#         dealer_hand.append(card_types.pop())

#           #Below is a created function which calculates the sum of every card in any hand, including aces

#         stand = False
#         first_hand = True

#         while True:

#             player_hand_total = score_in_hand(player_hand)
#             dealer_hand_total = score_in_hand(dealer_hand)

#             if stand:
#                 print("The dealer's hand:")
#                 print("     ______     ______")
#                 print("    |{}    |".format('    |   |'.join(dealer_hand)))
#                 print("    |  {}  |".format('  |   |  '.join(dealer_hand)))
#                 print("    |    {}|".format('|   |    '.join(dealer_hand)))
#                 print("    L_____⅃    L_____⅃")
#             else:
#                 print("The dealer's hand:")
#                 print("     ______     ______")
#                 print("    |{}    |    |??   |".format(dealer_hand[0]))
#                 print("    |  {}  |    | ??? |".format(dealer_hand[0]))
#                 print("    |    {}|    |   ??|".format(dealer_hand[0]))
#                 print("    L_____⅃    L_____⅃")

#             print("Your hand:")

#             print("    |{}‾‾‾‾|".format('    |   |'.join(player_hand)))
#             print("    |  {}  |".format('  |   |  '.join(player_hand)))
#             print("    |    {}|".format('|   |    '.join(player_hand)))
#             print("    L_____⅃".format('L_____⅃'.join(player_hand)))
#             print(f" Your score total for this round is: {player_hand_total}\n")

#             if stand:
#                 if dealer_hand_total > 21:
#                     print('HE BUSTED!! YOU WIN\n')
#                     wins += 1
#                 elif player_hand_total == dealer_hand_total:
#                     print('You both tied. You both equally suck.\n')
#                 elif player_hand_total > dealer_hand_total:
#                     print('BIG DUBSSSS!! Good game\n')
#                     wins += 1
#                 else:
#                     print('Take the L. Haha. :(\n')
#                     losses += 1


#             if player_hand_total > 21:
#                 print('Bruh. Ya busted. Take that L.\n')
#                 losses += 1
#                 break

#             if first_hand and player_hand_total == 21:
#                 print('BLLAAACKKKJACCCKKK !! BIG DUBS ON THE FIRST DRAW. GG!!\n')
#                 wins += 1
#                 break

#             first_hand = False

#             print('You now have several options...')
#             print('Please type one of the following choices and press enter:')
#             print('     [H] for Hit')
#             print('     [S] for Stand')
#             print('     [F] for Fold\n')

#             hit_or_stay = input('Your choice: \n').lower()

#             if hit_or_stay == "h":
#                 player_hand.append(card_types.pop())
#             elif hit_or_stay == 's':
#                 stand = True
#                 while score_in_hand(dealer_hand) <= 16:
#                     dealer_hand.append(card_types.pop())

#     if losses == 3:
#         do_they_want_to_play == 'no'

#     elif wins == 3:
#         print("")
#         print("Jumpin' Joe: ... \n Jumpin' Joe: ... ... ... \n Jumpin' Joe: I... i... can't believe you actually beat me... \n Jumpin' Joe: Congrats I guess... at least I know Rockin' Ricky will take you down. \n Jumpin' Joe: I'll see you never, loser. Hmpf.")
#         print("")
#         print("")

# # The upcoming portion of code is the definitions and variables for tic-tactoe... 8 definitions and some variables

board = [' ' for x in range(10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == ' '

def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')

#bo is short for board and le is short for length

def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter('X', move)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')


def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for let in ['O', 'X']:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:
        move = 5
        return move

    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]


def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def run_tictactoe():
    print("Here we go now, partner. Get ready to take a real whoopin'!")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Now you can head home. Hahha.')
            break

        if not(isWinner(board, 'X')):
            move = compMove()
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('Computer placed an \'O\' in position', move , ':')
                printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

run_tictactoe()

# set up the board
# show the board
# ask who is who
# state who's turn it is




# #The final portion of code is for the setup of the actual storyline and where all of the  games actually run.
# if do_they_want_to_play == "no":
#     print("You stink.")

# elif do_they_want_to_play == "yes":
#     player_name = input("Well, let me tell you, you got a lotta confidence walking in this town when Big Bill's around. What's your name?: ")
#     print(f"Nice to meet you, {player_name}. Crazy stuff's been going down in this ol' boom town as of late, eh?")
#     print(f"For the past few weeks Big Bill has been robbing our banks, taking our crop, and running around with his two pals Jumpin' Joe and Rockin' Ricky. We sure could use a hero. Say... you said you wanted an adventure. Well I've got a plan to take down Big Bill and his crew. Let me explain:")
#     print(f"      Step 1- Take down Jumpin' Joe at the casino by beating him in his challenge.")
#     print(f"      Step 2- Rockin' Ricky is taking the Railways to Crystal City next week for the weekend, knock his train off the tracks and get a sweet victory. And finally...")
#     print(f"      Step 3- Find and eliminate Big Bill at High Noon this Sunday. And just like that you could save this town.")
#     input("Are you ready?: ")
#     print("")
#     print("Doesn't matter anyway. You're in this town; you might as well try to save it...")
#     print("")
#     print("")
#     print("Level 1... Jumpin' Joe's Casino")
#     print("")
#     print(f"X: 'Howdy Ho there parter. I'm Jumpin' Joe. I've heard you've been coming for me, {player_name}. Well I've got good news for ya. I'm the best blackjack player in the land West of the Mississippi. And because of that I'll make you  a deal, if you beat me in a round of blackjack, I'll run away to Jamaica, never to cause this town trouble again, but if I beat you... then you get sent to Davy Jones' Locker on the next ship back to China.'\n")
#     #storyline has been setup all the way to the first of three levels.
#     #Code coming up is used to play the first level, a game of blackjack which should be made so that the user has a good chance of winning.

#     print("Here's the rundown on how to play: You will be randomly dealt two cards. Your objective is to get the sum of the two cards, where face cards are worth 10 and Aces are worth either 1 or 11 based on your decision, to equal 21. If you wish to draw another card to get your sum higher you may, but beware, if your new card results in a sum higher than 21, you automatically lose. The other way to lose would be to have the dealer, who is playing the same game as you, to get closer to 21 as his sum than you. If you lose three games you will be eliminated and Jumpin' Joe will exile you, but if you come out victorious three times, Jumpin' Joe will run out of town... Good Luck! \n")

#     run_blackjack()

#     print(f"\n Narrator: Great job on completing the first level, {player_name}, but now it's time to head on down to the railroad to take on Rockin' Ricky!! \n He's going to try to get back to the bad guy headquarters at about 11:25 a.m., so we must blow up the train that he's on to try and stop him!"
#     print("")
#     print("The way that you stop Rockin' Ricky from travelling on the train is by convinving the train conductor to run the train off of a bridge that it passes over. Unfortunately, the only way that he has agreed to do this is if you can beat him in an age-old game of tic-tac-toe.")
#     this_is_pointless = input("Do you think you're ready to play him in tic-tac-toe? ")
#     print("Actually, that's irrelevant. Get out there and kick some conductor butt!")
    # print("")
    # print("")
    # print("")
    # print("Train conductor: Well well well... If it isn't an actual challenger to my throne of tic-tac-toe stardom!! You will surely meet death in this match, however! Say, what is your name after all?")
    # print(f"You: {player_name}"
    # print(f"Well, {player_name}, I will definately grant your wish if you beat me in a game, but hey, that's never happened! And I've played every person that's ever loved me, for a grand total of two victories! (both to my mother, as papa wasn't particuarly fond of my presence.)")

    # run_tictactoe()








#                 # Psuedocode scrap paper for blackjack
#                 # If the player's sum is greater than 21, they lose
#                 # If the dealer's sum is greater than 21, they lose
#                 # If the player's sum is less than 21, they get a hit or stay option until they decide to stay
#                 # If the dealer's sum is less than 16, they automatically hit
#                 # If the player wants to stay then straight compare sums
#                 # If the players sum < 21 && > the dealer's sum, then the player wins
#                 # If the player's sum is less than the dealers, then the player loses


# else:
#     print("I don't have even the slightest clue as to how you got here lol. Try to restart the game, I guess.")

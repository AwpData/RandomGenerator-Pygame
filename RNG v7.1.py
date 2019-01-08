"""                                                                                
RNG/PYGAME - PROGRAM (V 7.1)
By: Trevor Tang
Description: Just a bunch of simulations I made (Pygame Released!)
"""
#                                                                                                                            #
# #                                                                                                                          ##
### Hi there! This program showcases my skills with the random/pygame library! Each simulator is sorted by type. Have fun! ###
# #                                                                                                                          ##
#                                                                                                                            #
import random
import pygame
pygame.init()
program = input("Which program would you like to try? (pygame, random): ")

if program == "random":
    print("Welcome to the RNG program")
    programstart = input("Type go to start: ")
    while programstart == "go" or programstart == "back":
        print("")
        print("Which random generator would you like to try?")
        print("")
        print("1. True random number generator")
        print("2. Sequence random number generator")
        print("3. Random Binary Code Sequence")
        print("4. Random Lucky Number drawing and guessing game")
        print("5. Giveaway Simulator. Are you lucky enough to win?")
        print("6. Coin Flipper or game")
        print("7. Card War game against Computer")
        print("8. Dice Roller")
        print("9. Rock Paper Scissors Simulator (DISABLED FOR NOW) ")
        print("10. Social Media Randomized Stuff")
        print("")
        print("===================================")
        print("11. INFO ABOUT THIS CODE AND ABOUT ME!")
        print("12. Patch notes")
        print("")
        print("Type 13 to quit the program")
        print("")
        gamechose = int(input("Please enter the number of the generator you would like to try: "))
        print("")
        
        if gamechose == 1:
            print("The random number generator is set to whatever numbers you want")
            programstart = input("Type list to start: ")
            while programstart == "list":
                print("")
                randommin = int(input("What is the minimum number: "))
                randommax = int(input("What is the maximum number: "))
                numberlist = int(input("How many numbers would you like to generate? (Up to 1000): "))
                print("")
                if numberlist > 0 and numberlist < 1001 :
                    while numberlist > 0 and numberlist < 1001:
                        randomnum_gen = random.randint(randommin, randommax)
                        print(randomnum_gen)
                        numberlist -= 1
                else:
                    print("Error: Please enter a number within the desired range")
                print("")
                programstart = input("Want to generate more? Type list. Want to go back to the menu? Type back. If not, type quit: ")
        
        elif gamechose == 2:
            print("The sequence random number generator will generate a random set of numbers in a list")
            programstart = input("Type list to start: ")
            while programstart == "list":
                print("")     
                numberseq = int(input("How many numbers would you like to generate? (Up to 10000): "))
                print("")
                if numberseq > 0 and numberseq < 10001:
                    while numberseq > 0 and numberseq < 100001:
                        randomnum_gen = random.randint(1, 1000000000000)
                        print(randomnum_gen)
                        numberseq -= 1
                        
                else:
                    print("Error: Please enter a number within the desired range")
                print("")
                programstart = input("Want to generate more? Type list! Want to go back to the menu? Type back. If not, type quit: ")
                
        elif gamechose == 3:
            print("The random binary code sequence will create a random binary code sequence in a column")
            programstart = input("Type list to start: ")
            while programstart == "list":
                print("")
                binaryrand = int(input("How many different numbers would you like to generate? (Min: 8; Max: 80): "))
                print("")
                if binaryrand > 0 and binaryrand < 1001:
                    while binaryrand > 0 and binaryrand < 1001:
                        randomnum_gen = random.randint(0, 1)
                        print(randomnum_gen)
                        binaryrand -= 1
                else:
                    print("Error: Please enter a number within the desired range")
                print("")
                programstart = input("Want to generate more? Type list! Want to go back to the menu? Type back. If not, type quit: ")
        
        elif gamechose == 4:
            print("This category branches into 2 subsections")
            chose = input("Do you want to draw numbers or guess numbers? (draw,guess): ")
            if chose == "draw":
                print("")
                print("This is a randomly generated lucky number simulator")
                print("If the number is chosen a message is shown")
                print("Until you get the randomly chosen lucky number or the first or last number which are considered lucky (10,000, 100,000, and 1 mil only) the program will keep going")
                print("")
                programstart = input("Type draw to start: ")
                while programstart == "draw":
                    print("")
                    amount = int(input("Would you like to draw up to the number 10, 100, 1,000, 10,000, 100,000*, or 1,000,000* numbers? *NOT RECOMMENDED "))
                    if amount == 10:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 10)
                        while randnum != luckynum:
                            randnum = random.randint(1, 10)
                            print(randnum)
                            randadd += 1
                    elif amount == 100:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 100)
                        while randnum != luckynum:
                            randnum = random.randint(1, 100)
                            print(randnum)
                            randadd += 1
                    elif amount == 1000:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 1000)
                        while randnum != luckynum:
                            randnum = random.randint(1, 1000)
                            print(randnum)
                            randadd += 1   
                    elif amount == 10000:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 10000)
                        while randnum != luckynum:
                            randnum = random.randint(1, 10000)
                            print(randnum)
                            randadd += 1
                            if randnum == 1:
                                print("You got 1!")
                                break
                            elif randnum == 10000:
                                print("You got 10,000!")
                                break   
                    elif amount == 100000:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 100000)
                        while randnum != luckynum:
                            randnum = random.randint(1, 100000)
                            print(randnum)
                            randadd += 1
                            if randnum == 1:
                                print("You got 1!")
                                break
                            elif randnum == 100000:
                                print("You got 100,000!")
                                break 
                    elif amount == 1000000:
                        randnum = 0
                        randadd = 0
                        luckynum = random.randint(1, 1000000)
                        while randnum != luckynum:
                            randnum = random.randint(1, 1000000)
                            print(randnum)
                            randadd += 1
                            if randnum == 1:
                                print("You got 1!")
                                break
                            elif randnum == 1000000:
                                print("You got 1,000,000!")
                                break 
                    else:
                        print("Error: Number is not one of the number choses")
                    print("")
                    print("Lucky number found!")
                    print("The lucky number was " + str(luckynum))
                    print("The computer had to draw " + str(randadd) + " numbers")
                    print("")
                    programstart = input("Want to play again? Type draw. Want to go back to the menu? Type back. If not, type quit: ")
            elif chose == "guess":
                print("")
                print("This game has you trying to guess the lucky number")
                print("You can guess out of the numbers 10, 100, or 1,000")
                programstart = input("Type start to start: ")
                while programstart == "start":
                    print("")
                    guesschose = int(input("Would you like to guess out of the numbers 10, 100, or 1000?: "))
                    print("")
                    userguess = 0
                    while guesschose == 10:
                        print("You will have 3 guesses to guess the lucky number")
                        input("Press ENTER to start: ")
                        luckynum = random.randint(1, 10)
                        guessleft = 3
                        while luckynum != userguess and guessleft > 0:
                            userguess = int(input("What is the lucky number?: "))
                            if userguess == luckynum:
                                print("You got it!")
                                guesschose = 0
                            elif userguess != luckynum:
                                print("Wrong!")
                                guessleft -= 1
                        if guessleft == 0:
                            guesschose = 0
                    while guesschose == 100:
                        print("You will have 5 guesses to guess the lucky number")
                        input("Press ENTER to start: ")
                        luckynum = random.randint(1, 100)
                        guessleft = 5
                        while luckynum != userguess and guessleft > 0:
                            userguess = int(input("What is the lucky number?: "))
                            if userguess == luckynum:
                                print("You got it!")
                                guesschose = 0
                            elif userguess != luckynum:
                                print("Wrong!")
                                guessleft -= 1
                        if guessleft == 0:
                            guesschose = 0
                    while guesschose == 1000:
                        print("You will have 10 guesses to guess the lucky number")
                        input("Press ENTER to start: ")
                        luckynum = random.randint(1, 1000)
                        guessleft = 10
                        while luckynum != userguess and guessleft > 0:
                            userguess = int(input("What is the lucky number?: "))
                            if userguess == luckynum:
                                print("You got it!")
                                guesschose = 0
                            elif userguess != luckynum:
                                print("Wrong!")
                                guessleft -= 1
                        if guessleft == 0:
                            guesschose = 0
                    print("")
                    print("The lucky number was: " + str(luckynum))
                    print("")
                    programstart = input("If you want to play again type start! Want to go back to the menu? Type back. If not, type quit: ")
                    
        elif gamechose == 5:
            print("This is a giveaway simulator")
            print("You can choose between a set BASIC giveaway where you join or a random ADVANCED giveaway where you create or join a giveaway")
            chose = input("Which simulator would you like to try? (odds, random): ")
            if chose == "odds":
                print("")
                print("This simulator will put you into a random giveaway and you get to see how likely you are going to win")
                programstart = input("Type start to start: ")
                while programstart == "start":
                    print("")
                    randomentries = random.randint(1, 15000)
                    print("There are currently " + str(randomentries) + " entries")
                    randomentry = random.randint(1, randomentries)
                    print("Your entry number is " + str(randomentry))
                    print("")
                    input("Type draw to see your of winning: ")
                    randomentrychance = 1 / randomentry
                    randomentrychancetotal = randomentrychance * 100
                    print("You have a " + str(randomentrychancetotal) + " percentage chance of winning")
                    print("")
                    input("Type draw to see if you won: ")
                    winner = random.randint(1, randomentries)
                    print("")
                    print("The winner of the draw is number " + str(winner))
                    if winner == randomentry:
                        print("")
                        print("You won the giveaway!")
                        break
                    elif winner != randomentry:
                        print("")
                        print("Sorry, you didn't win")
                    print("")
                    programstart = input("Would you like to try your chances again? Type start. Want to go back to the menu? Type back. If not, type quit: ")
            elif chose == "random":
                print("")
                print("This category splits into 2 more categories")
                programstart = input("Would you like to 'join' or 'create' a random giveaway?: ")
                print("")
                if programstart == "create":
                    while programstart == "create":
                        print("")
                        print("You are creating your own giveaway")
                        game = input("What game are you giving away?: ")
                        print("")
                        print("Giveaway is starting...")
                        print("")
                        randomentries = random.randint(1, 10000)
                        print("There were a total of " + str(randomentries) + " entries.")
                        input("Press ENTER for the winner to be chosen: ")
                        randomuser = random.randint(1, 10)
                        if randomuser == 1:
                            randomuser = "Jonin"
                        elif randomuser == 2:
                            randomuser = "Brute"
                        elif randomuser == 3:
                            randomuser = "Johnnyby"
                        elif randomuser == 4:
                            randomuser = "Bill101"
                        elif randomuser == 5:
                            randomuser = "ThomasL"
                        elif randomuser == 6:
                            randomuser = "Circle13"
                        elif randomuser == 7:
                            randomuser = "PexDz"
                        elif randomuser == 8:
                            randomuser = "Youreallygottowinthose"
                        elif randomuser == 9:
                            randomuser = "Sften0"
                        elif randomuser == 10:
                            randomuser = "olef1"
                        randomwinner = random.randint(1, randomentries)
                        print("")
                        print("The winner of the game " + game + " is " + str(randomwinner) + " who is " + randomuser)
                        print("")
                        programstart = input("Would you like to create another giveaway? Type create! Want to go back to the menu? Type back. If not, type quit: ")
                elif programstart == "join":
                    print("This is an actual simulator of how it feels to join a giveaway")
                    print("")
                    username = input("Enter your username: ")
                    input("Choose a giveaway from the list below! (Press ENTER): ")
                    while programstart == "join":
                        print("")
                        randomgamelist = random.randint(1, 10)
                        if randomgamelist == 1:
                            randomgamelist = "Fallout 4"
                        elif randomgamelist == 2:
                            randomgamelist = "Subnautica"
                        elif randomgamelist == 3:
                            randomgamelist = "Trackmania Turbo"
                        elif randomgamelist == 4:
                            randomgamelist = "Call of Duty WW2"
                        elif randomgamelist == 5:
                            randomgamelist = "Warhammer Vermintide 2"
                        elif randomgamelist == 6:
                            randomgamelist = "Counter-Strike: Global Offensive"
                        elif randomgamelist == 7:
                            randomgamelist = "PC Building Simulator"
                        elif randomgamelist == 8:
                            randomgamelist = "PlayerUnknownBattleGrounds"
                        elif randomgamelist == 9:
                            randomgamelist = "Squad"
                        elif randomgamelist == 10:
                            randomgamelist = "Euro Truck Simulator 2"
                        print("======================")
                        print("Giveaway 1: " + str(randomgamelist))
                        randomentries = random.randint(1, 15000)
                        print("Entries: " + str(randomentries))
                        print("======================")
                        randomgamelist = random.randint(1, 10)
                        if randomgamelist == 1:
                            randomgamelist = "Fallout 4"
                        elif randomgamelist == 2:
                            randomgamelist = "Subnautica"
                        elif randomgamelist == 3:
                            randomgamelist = "Trackmania Turbo"
                        elif randomgamelist == 4:
                            randomgamelist = "Call of Duty WW2"
                        elif randomgamelist == 5:
                            randomgamelist = "Warhammer Vermintide 2"
                        elif randomgamelist == 6:
                            randomgamelist = "Counter-Strike: Global Offensive"
                        elif randomgamelist == 7:
                            randomgamelist = "PC Building Simulator"
                        elif randomgamelist == 8:
                            randomgamelist = "PlayerUnknownBattleGrounds"
                        elif randomgamelist == 9:
                            randomgamelist = "Squad"
                        elif randomgamelist == 10:
                            randomgamelist = "Euro Truck Simulator 2"
                        print("Giveaway 2: " + str(randomgamelist))
                        randomentries2 = random.randint(1, 15000)
                        print("Entries: " + str(randomentries2))
                        print("======================")  
                        randomgamelist = random.randint(1, 10)
                        if randomgamelist == 1:
                            randomgamelist = "Fallout 4"
                        elif randomgamelist == 2:
                            randomgamelist = "Subnautica"
                        elif randomgamelist == 3:
                            randomgamelist = "Trackmania Turbo"
                        elif randomgamelist == 4:
                            randomgamelist = "Call of Duty WW2"
                        elif randomgamelist == 5:
                            randomgamelist = "Warhammer Vermintide 2"
                        elif randomgamelist == 6:
                            randomgamelist = "Counter-Strike: Global Offensive"
                        elif randomgamelist == 7:
                            randomgamelist = "PC Building Simulator"
                        elif randomgamelist == 8:
                            randomgamelist = "PlayerUnknownBattleGrounds"
                        elif randomgamelist == 9:
                            randomgamelist = "Squad"
                        elif randomgamelist == 10:
                            randomgamelist = "Euro Truck Simulator 2"
                        print("Giveaway 3: " + str(randomgamelist))
                        randomentries3 = random.randint(1, 15000)
                        print("Entries: " + str(randomentries3))
                        print("======================")
                        print("")
                        entered = int(input("Please enter the number of the giveaway you want to enter: "))
                        randomuser = random.randint(1, 10)
                        if randomuser == 1:
                            randomuser = "Jonin"
                        elif randomuser == 2:
                            randomuser = "Brute"
                        elif randomuser == 3:
                            randomuser = "Johnnyby"
                        elif randomuser == 4:
                            randomuser = "Bill101"
                        elif randomuser == 5:
                            randomuser = "ThomasL"
                        elif randomuser == 6:
                            randomuser = "Circle13"
                        elif randomuser == 7:
                            randomuser = "PexDz"
                        elif randomuser == 8:
                            randomuser = "Youreallygottowinthose"
                        elif randomuser == 9:
                            randomuser = "Sften0"
                        elif randomuser == 10:
                            randomuser = "olef1"
                        if entered == 1:
                            randomentry = random.randint(1, randomentries)
                            print("Your entry number is: " + str(randomentry))
                            input("Press ENTER to see if you win: ")
                            print("")
                            randomwinner = random.randint(1, randomentries)
                            if randomwinner == randomentry:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + username)
                                print("You won " + randomgamelist + "!")
                            else:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + randomuser)
                        elif entered == 2:
                            randomentry = random.randint(1, randomentries2)
                            print("Your entry number is: " + str(randomentry))
                            input("Press ENTER to see if you win: ")
                            randomwinner = random.randint(1, randomentries2)
                            if randomwinner == randomentry:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + username)
                                print("You won " + randomgamelist + "!")
                            else:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + randomuser)
                        elif entered == 3:
                            randomentry = random.randint(1, randomentries3)
                            print("Your entry number is: " + str(randomentry))
                            input("Press ENTER to see if you win: ")
                            randomwinner = random.randint(1, randomentries3)
                            if randomwinner == randomentry:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + username)
                                print("You won " + randomgamelist + "!")
                            else:
                                print("")
                                print("The winner of the giveaway was entry number " + str(randomwinner) + " who is " + randomuser)
                        print("")
                        programstart = input("Want to join another giveaway? Type join! Want to go back to the menu? Type back. If not, type quit: ")
                            
        elif gamechose == 6:
            print("This is a random coin flipper. This category splits into 2 others")
            programstart = input("Would you like to flip a coin or play heads or tails? (flip or game): ")
            if programstart == "flip":
                print("")
                print("This will simulate a coin being flipped")
                while programstart == "flip":
                    flipchose = int(input("How many coins will be flipped? (Up to 100): "))
                    print("")
                    if flipchose > 0 and flipchose < 101:
                        while flipchose > 0 and flipchose < 101:
                            fliprand = random.randint(0, 1)
                            if fliprand == 0:
                                print("HEADS")
                            elif fliprand == 1:
                                print("TAILS")
                            flipchose -= 1
                        print("")
                        programstart = input("Want to do it again? Type flip. Want to go back to the menu? Type back. If not, type quit: ")
                    
            elif programstart == "game":
                print("")
                print("This is a game where you guess heads or tails")
                programstart = input("Type play to start: ")
                while programstart == "play":
                    print("")
                    gamechose = input("heads or tails: ")
                    print("")
                    if gamechose == "heads":
                        coinrand = random.randint(0, 1)
                        if coinrand == 1:
                            coin = "heads"
                            if gamechose == "heads":
                                print("Coin flips HEADS you win")
                        elif coinrand == 0:
                            coin = "tails"
                            if gamechose == "heads":
                                print("Coin flips TAILS you lose")
                    elif gamechose == "tails":
                        coinrand = random.randint(0, 1)
                        if coinrand == 1:
                            coin = "heads"
                            if gamechose == "tails":
                                print("Coin flips HEADS you lose")
                        elif coinrand == 0:
                            coin = "tails"
                            if gamechose == "tails":
                                print("Coin flips TAILS you win")
                    else:
                        print("")
                        print("Error: Please try again")
                    print("")
                    programstart = input("Type play to play again! Want to go back to the menu? Type back. Otherwise, type quit to stop: ")
                else:
                    print("")
                    print("Error: Quitting program")
            else:
                print("Error: Please enter a game that is listed")
        
        elif gamechose == 7:
            print("This is a game of War against the computer")
            print("I recommend you look up how to play this game if you haven't to understand the game")
            programstart = input("Type start to start the game: ")
            print("")
            while programstart == "start":
                playercards = 10
                computercards = 10
                rounds = 0
                while playercards > 0 and computercards > 0:
                    print("You have " + str(playercards) + " cards left")
                    print("The computer has " + str(computercards) + " cards left")
                    input("Press ENTER to flip a card: ")
                    print("")
                    randomcardp = random.randint(1, 13)
                    randomcardc = random.randint(1, 13)
                    if randomcardp == 11:
                        print("You drew a JACK (11)")
                    if randomcardc == 11:
                        print("Computer drew a JACK (11)")
                    if randomcardp == 12:
                        print("You drew a QUEEN (12)")
                    if randomcardc == 12:
                        print("Computer drew a QUEEN (12)")
                    if randomcardp == 13:
                        print("You drew a KING (13) ")
                    if randomcardc == 13:
                        print("Computer drew a KING (13) ")
                    if randomcardp == 1:
                        print("You drew an ace! (15) ")
                        randomcardp = 15
                    if randomcardc == 1:
                        print("Computer drew an ace! (15) ")
                        randomcardc = 15
                    if randomcardp < 11 and randomcardp > 1:
                        print("You drew a " + str(randomcardp))
                    if randomcardc < 11 and randomcardc > 1:
                        print("Computer drew a " + str(randomcardc))
        # Here it checks for winner below. Sorry for the mess!
                    if randomcardp > randomcardc:
                        print("You win with a " + str(randomcardp))
                        playercards += 1
                        computercards -= 1
                    elif randomcardp < randomcardc:
                        print("Computer wins with a " + str(randomcardc))
                        playercards -= 1
                        computercards += 1
                    elif randomcardp == randomcardc:
                        print("No one wins!")
                        print("Everyone loses a card")
                        playercards -= 1
                        computercards -= 1
                    rounds += 1
                    print("")
                winner = ""
                if playercards > computercards:
                    print("You win!")
                    winner = "You"
                elif computercards > playercards:
                    print("Computer wins!")
                    winner = "Computer"
                elif computercards == playercards:
                    print("TIE!")
                print("")
                print("===GAME SUMMARY===")
                print("")
                print("Rounds taken: " + str(rounds))
                print("WINNER: " + winner)
                print("")
                programstart = input("Want to play again? Type start! If not, type quit: ")
        
        elif gamechose == 8:
            print("This splits into two different categories")
            what = input("Which dice rolling simulator would you like to try? (count, roll): ")
            print("")
            if what == "roll":
                print("This will simulate a number of dice that will roll")
                print("Perfect for board games, gambling games, or for fun")
                print("Each die has 6 sides like a normal die")
                print("It will print what each die rolled and then add them up together")
                programstart = input("Type roll to start: ")
                print("")
                diecount = int(input("How many die will you be rolling? (Up to 4): "))
                while programstart == "roll":
                    print("")
                    if diecount == 1:
                        dieran = random.randint(1, 6)
                        print("Die 1: " + str(dieran))
                        print("")
                        print("The die rolled a " + str(dieran))
                    elif diecount == 2:
                        dieran = random.randint(1, 6)
                        print("Die 1: " + str(dieran))
                        dieran2 = random.randint(1, 6)
                        print("Die 2: " + str(dieran2))
                        print("")
                        print("Die 1 rolled a " + str(dieran))
                        print("Die 2 rolled a " + str(dieran2))
                        print("")
                        dierantotal = dieran + dieran2
                        print("The total of the dice was " + str(dierantotal))
                        print("")
                    elif diecount == 3:
                        dieran = random.randint(1, 6)
                        print("Die 1: " + str(dieran))
                        dieran2 = random.randint(1, 6)
                        print("Die 2: " + str(dieran2))
                        dieran3 = random.randint(1, 6)
                        print("Die 3: " + str(dieran3))
                        print("")
                        print("Die 1 rolled a " + str(dieran))
                        print("Die 2 rolled a " + str(dieran2))
                        print("Die 3 rolled a " + str(dieran3))
                        print("")
                        dierantotal = dieran + dieran2 + dieran3
                        print("The total of the dice was " + str(dierantotal))
                        print("")
                    elif diecount == 4:
                        dieran = random.randint(1, 6)
                        print("Die 1: " + str(dieran))
                        dieran2 = random.randint(1, 6)
                        print("Die 2: " + str(dieran2))
                        dieran3 = random.randint(1, 6)
                        print("Die 3: " + str(dieran3))
                        dieran4 = random.randint(1, 6)
                        print("Die 4: " + str(dieran4))
                        print("")
                        print("Die 1 rolled a " + str(dieran))
                        print("Die 2 rolled a " + str(dieran2))
                        print("Die 3 rolled a " + str(dieran3))
                        print("Die 4 rolled a " + str(dieran4))
                        print("")
                        dierantotal = dieran + dieran2 + dieran3 + dieran4
                        print("The total of the dice was " + str(dierantotal))
                        print("")
                    else:
                        print("Error: Please enter a number within the range")
                    print("")
                    programstart = input("Want to roll again? Type roll. If you want to go back to the menu, type back. If not, type quit: ")
            elif what == "count":
                print("This simulator will roll a die or 2 until a certain number")
                print("Once it reaches that number it will print how many rolls it took to get there")
                programstart = input("Type roll to start: ")
                while programstart == "roll":
                    print("")
                    diecount = int(input("How many die will you like to roll? (1 or 2): "))
                    rollto = int(input("What number would you like to roll to? (Up to 1000): "))
                    if diecount == 1 and rollto < 1001:
                        dierantotal = 0
                        rolls = 0
                        while dierantotal < rollto:
                            dice1 = random.randint(1, 6)
                            dicetotal = dice1
                            dierantotal += dicetotal
                            rolls += 1
                            print("Die 1: " + str(dice1))
                            print("")
                            print("Dice total: " + str(dierantotal))
                            print("")
                        print("To get to " + str(rollto) + " it took " + str(rolls) + " rolls")
                        programstart = input("Want to do it again? Type roll. Want to go back to the menu? Type back. If not, type quit: ")
                    if diecount == 2 and rollto < 1001:
                        dierantotal = 0
                        rolls = 0
                        while dierantotal < rollto:
                            dice1 = random.randint(1, 6)
                            dice2 = random.randint(1, 6)
                            dicetotal = dice1 + dice2
                            dierantotal += dicetotal
                            rolls += 1
                            print("Die 1: " + str(dice1))
                            print("Die 2: " + str(dice2))
                            print("")
                            print("Dice total: " + str(dierantotal))
                            print("")
                        print("To get to " + str(rollto) + " it took " + str(rolls) + " rolls")
                        programstart = input("Want to do it again? Type roll. Want to go back to the menu? Type back. If not, type quit: ")
                        
        elif gamechose == 9:
            print("Sorry but this simulator is currently under construction as it is broken.")
            print("")
            programstart = input("Want to go back to the menu? Type back. If not, type quit: ")
            
        elif gamechose == 1337:
            print("This random generator simulates a rock paper scissor game")
            print("There are 2 simulators: One that simulates a game, the other you play against the computer")
            rps = input("Do you want to play the simulator or against the computer? (simulator or game): ")
            print("")
            if rps == "simulator":
                rock = ""
                rock2 = ""
                paper = ""
                paper2 = ""
                scissors = ""
                scissors2 = ""
                print("")
                print("This will simulate a game of rock paper scissors between 2 people")
                programstart = input("Type play to start: ")
                print("")
                while programstart == "play":
                    print("")
                    simran = random.randint(1, 3)
                    if simran == 1:
                        rock = "rock"
                        print("Player one plays ROCK")
                    elif simran == 2:
                        paper = "paper"
                        print("Player one plays PAPER")
                    elif simran == 3:
                        scissors = "scissors"
                        print("Player one plays SCISSORS")
                    simran2 = random.randint(1, 3)
                    if simran2 == 1:
                        rock2 = "rock"
                        print("Player two plays ROCK")
                    elif simran2 == 2:
                        paper2 = "paper"
                        print("Player two players PAPER")
                    elif simran2 == 3:
                        scissors2 = "scissors"
                        print("Player two plays SCISSORS")
                    print("")
                    if rock == "rock" and rock2 == "rock":
                        print("Player one and player two tie with ROCK")
                    elif paper == "paper" and paper2 == "paper":
                        print("Player one and player two tie with PAPER")
                    elif scissors == "scissors" and scissors2 == "scissors":
                        print("Player one and player two tie with SCISSORS")
                    elif rock == "rock" and paper2 == "paper":
                        print("Player two beats player one tie with PAPER ON ROCK")
                    elif rock == "rock" and scissors2 == "scissors":
                        print("Player one beats player two with ROCK ON SCISSORS")
                    elif paper == "paper" and rock2 == "rock":
                        print("Player one beats player two with PAPER ON ROCK")
                    elif paper == "paper" and scissors2 == "scissors":
                        print("Player two beats player one with SCISSORS ON PAPER")
                    elif scissors == "scissors" and rock2 == "rock":
                        print("Player two beats player one with ROCK ON SCISSORS")
                    elif scissors == "scissors" and paper2 == "paper":
                        print("Player one beats player two with SCISSORS ON PAPER")
                    print("")
                    programstart = input("If you would like to play again type play. Want to go back to the menu? Type back. If not, type quit: ")
            elif rps == "game":
                rock = ""
                paper = ""
                scissors = ""
                print("You will be playing rock paper scissors against the computer")
                programstart = input("Type play to start: ")
                while programstart == "play":
                    print("")
                    move = input("rock, paper, or scissors?: ")
                    print("")
                    if move == "rock":
                        print("You chose ROCK")
                    elif move == "paper":
                        print("You chose PAPER")
                    elif move == "scissors":
                        print("You chose SCISSORS")
                    computermove = random.randint(1, 3)
                    if computermove == 1:
                        rock = "rock"
                        print("Computer chose ROCK")
                    elif computermove == 2:
                        paper = "paper"
                        print("Computer chose PAPER")
                    elif computermove == 3:
                        scissors = "scissors"
                        print("Computer chose SCISSORS")
                    print("")
                    if move == "rock" and rock == "rock":
                        print("You tie with ROCK")
                    elif move == "paper" and paper == "paper":
                        print("You tie with PAPER")
                    elif move == "scissors" and scissors == "scissors":
                        print("You tie with SCISSORS")
                    elif move == "rock" and paper == "paper":
                        print("Computer wins with PAPER ON ROCK")
                    elif move == "rock" and scissors == "scissors":
                        print("You win with ROCK ON SCISSORS")
                    elif move == "paper" and scissors == "scissors":
                        print("Computer wins with SCISSORS ON PAPER")
                    elif move == "scissors" and paper == "paper":
                        print("You win with SCISSORS ON PAPER")
                    elif move == "paper" and rock == "rock":
                        print("You win with PAPER ON ROCK")
                    elif move == "scissors" and rock == "rock":
                        print("Computer wins with ROCK ON SCISSORS")
                    print("")
                    programstart = input("Want to play again? Type play. Want to go back to the menu? Type back. If not, type quit: ")
                    
        elif gamechose == 10:
            print("This is a social media post simulation")
            print("Everything is randomized except for your inputs")
            programstart = input("Type post to start: ")
            print("")
            name = input("What is your name: ")
            while programstart == "post":
                print("")
                status = input("What is your status: ")
                likes = random.randint(0, 100000)
                dislikes = random.randint(0, 10000)
                reposts = random.randint(0, 100000)
                print("")
                print("---------------------")
                print(name + ": " + status)
                print("   Likes: " + str(likes) + ", Dislikes: " + str(dislikes) + ", Reposts: " + str(reposts))
                print("---------------------")
                seenby1 = "Mom"
                seenby2 = "Mom, Dad"
                seenby3 = "Mom, Dad, Bro"
                seenby4 = "Mom, Dad, Bro, Sis"
                seenby5 = "Mom, Dad, Bro, Sis, Bestie"
                seenby6 = "Mom, Dad, Bro, Sis, Bestie, Grandma"
                seenby7 = "Mom, Dad, Bro, Sis, Bestie, Grandma, Grandpa"
                seenby8 = "Mom, Dad, Bro, Sis, Bestie, Grandma, Grandpa, Cousin"
                seenby9 = "Mom, Dad, Bro, Sis, Bestie, Grandma, Grandpa, Cousin, Auntie"
                seenby10 = "Mom, Dad, Bro, Sis, Bestie, Grandma, Grandpa, Cousin, Auntie, Uncle"
                seenby_ran = random.randint(1, 10)
                print("Seenby (Followers): " + str(seenby_ran))
                others_ran = random.randint(50000, 1000000)
                print("+" + str(others_ran) + " others")
                user1 = "Coolkid101"
                user2 = "Whomstve"
                user3 = "User3"
                user4 = "Hellothere"
                user5 = "12345677889"
                user6 = "Humbadeehumbadee"
                user7 = "TouristGuy"
                user8 = "Wooh2"
                user9 = "Jay"
                user10 = "th0mas"
                comment1 = "Sounds boring"
                comment2 = "Have a good time :)"
                comment3 = "Nice job"
                comment4 = "WOW!"
                comment5 = "Meh..."
                comment6 = "Yay"
                comment7 = "Love it!"
                comment8 = "Whaa?"
                comment9 = "Cool"
                comment10 = "Lucky :("
                user_ran = random.randint(1, 10)
                commentnum_ran = random.randint(1, 10000)
                comment_ran = random.randint(1, 10)
                print("---------------------")
                print("      Comments")
                print("")
                print(str(user_ran) + ":")
                if comment_ran == 1:
                    print(comment1)
                elif comment_ran == 2:
                    print(comment2)
                elif comment_ran == 3:
                    print(comment3)
                elif comment_ran == 4:
                    print(comment4)
                elif comment_ran == 5:
                    print(comment5)
                elif comment_ran == 6:
                    print(comment6)
                elif comment_ran == 7:
                    print(comment7)
                elif comment_ran == 8:
                    print(comment8)
                elif comment_ran == 9:
                    print(comment9)
                elif comment_ran == 10:
                    print(comment10)
                print("")
                user_ran = random.randint(1, 10)
                comment_ran = random.randint(1, 10)
                if user_ran == 1:
                    print(user1 + ":")
                elif user_ran == 2:
                    print(user2 + ":")
                elif user_ran == 3:
                    print(user3 + ":")
                elif user_ran == 4:
                    print(user4 + ":")
                elif user_ran == 5:
                    print(user5 + ":")
                elif user_ran == 6:
                    print(user6 + ":")
                elif user_ran == 7:
                    print(user7 + ":")
                elif user_ran == 8:
                    print(user8 + ":")
                elif user_ran == 9:
                    print(user9 + ":")
                elif user_ran == 10:
                    print(user10 + ":")
                if comment_ran == 1:
                    print(comment1)
                elif comment_ran == 2:
                    print(comment2)
                elif comment_ran == 3:
                    print(comment3)
                elif comment_ran == 4:
                    print(comment4)
                elif comment_ran == 5:
                    print(comment5)
                elif comment_ran == 6:
                    print(comment6)
                elif comment_ran == 7:
                    print(comment7)
                elif comment_ran == 8:
                    print(comment8)
                elif comment_ran == 9:
                    print(comment9)
                elif comment_ran == 10:
                    print(comment10)
                print("")
                user_ran = random.randint(1, 10)
                comment_ran = random.randint(1, 10)
                if user_ran == 1:
                    print(user1 + ":")
                elif user_ran == 2:
                    print(user2 + ":")
                elif user_ran == 3:
                    print(user3 + ":")
                elif user_ran == 4:
                    print(user4 + ":")
                elif user_ran == 5:
                    print(user5 + ":")
                elif user_ran == 6:
                    print(user6 + ":")
                elif user_ran == 7:
                    print(user7 + ":")
                elif user_ran == 8:
                    print(user8 + ":")
                elif user_ran == 9:
                    print(user9 + ":")
                elif user_ran == 10:
                    print(user10 + ":")
                if comment_ran == 1:
                    print(comment1)
                elif comment_ran == 2:
                    print(comment2)
                elif comment_ran == 3:
                    print(comment3)
                elif comment_ran == 4:
                    print(comment4)
                elif comment_ran == 5:
                    print(comment5)
                elif comment_ran == 6:
                    print(comment6)
                elif comment_ran == 7:
                    print(comment7)
                elif comment_ran == 8:
                    print(comment8)
                elif comment_ran == 9:
                    print(comment9)
                elif comment_ran == 10:
                    print(comment10)
                print("")
                commentgenran_num = random.randint(1, 10000)
                print("+" + str(commentgenran_num) + " others")
                print("")
                programstart = input("Want to post another thing? Type post. Want to go back to the menu? Type back. If not, type quit: ")
            
        elif gamechose == 11:
            print("My name is Trevor Tang. I am a 9th grader at Sammamish High School")
            print("These series of codes are programs I wrote myself")
            print("They all showcase my skills with the random/pygame library")
            print("There are more than 1,100 LINES IN THIS CODE!")
            print("I hope you enjoy these simulators! :)")
            print("")
            print("")
            programstart = input("Want to go back to the menu? Type back. If not, type quit: ")
            
        elif gamechose == 12:
            print("PATCH NOTES")
            print("=============")
            print("")
            print("V7.1  -Enlarged the window to be able to read the text better")
            print("")
            print("V7.0  -Added pygame section")
            print("      -Added guess the color game")
            print("")
            print("V6.1  -Fixed text bug in count simulator where after every roll, a false message would appear.") 
            print("")
            print("V6.0  -Added a new count simulator within the dice simulator")
            print("      -Added and removed punctuation throughout the whole code")
            print("      -Added semicolons after every input statement")
            print("")
            print("V5.7  -Fixed bug where you could not go back to the menu in dice simulator")
            print("      -If you want to roll more die, you will not be asked to how many die you would like to roll")
            print("      -Simplified the code for dice simulator")
            print("")
            print("V5.6  -The social media simulator will not require you to keep on entering your name if you want to post again")
            print("")
            print("V5.5  -Increased coin flip amount in flip simulator to 100")
            print("      -Added blank lines to various places in the code")
            print("")
            print("V5.4  -You can finally go back to the menu instead of quitting at the end of simulators")
            print("      -Added menu prompt before entering the program to compensate for the new back command")
            print("      -Added quit command in the menu")
            print("")
            print("V5.2  -Added description for Social media simulator")
            print("      -Added loop to be able to post again in social media simulator")
            print("")
            print("V5.1  -Added users into the giveaway simulator if you lost")
            print("      -Now you can enter a username for the giveaways")
            print("")
            print("V5.0  -Added a new category in the giveaway simulator where you can create or join a random giveaway")
            print("")
            print("V4.5: -Now you can choose the min and max numbers you want in the true random number generator")
            print("      -Updated description for lucky number simulator")     
            print("")
            print("V4.1: -Fixed bug when guessing the lucky number right, ending message failed to show")
            print("")
            print("V4.0: -Added new game: Guess the lucky number")
            print("      -Fixed some text bugs")
            print("")
            print("V3.3: -Fixed bug with aces not being wins in war")
            print("      -Fixed computer text with kings in war")
            print("")
            print("V3.2: -Added first and last number as breaks in lucky number drawings for 10k, 100k, and 1mil")
            print("")
            print("V3.1: -Added 100,000 and 1,000,000 to lucky number generator")
            print("")
            print("V3.0: -Added card war game against the computer")
            print("")
            print("V2.0: -Added a lucky number generator")
            print("      -Fixed several bugs")
            print("")
            print("V1.1: -Added loops on generators 1, 2, and 3")
            print("")
            print("V1.0  -First Release out of BETA")
            print("")
            programstart = input("Want to go back to the menu? Type back. If not, type quit: ")
            
        elif gamechose == 13:
            break
elif program == "pygame":
    print("Welcome to the Pygame program")
    programstart = input("Type go to start ")
    while programstart == "go" or programstart == "back":
        print("")
        print("Which Pygame simulation would you like to try?")
        print("")
        print("1. Guess the color")
        print("")
        print("====================================")
        print("2. About me")
        print("3. Patch notes")
        print("")
        print("Type 4 to quit the program")
        print("")
        gamechose = int(input("Please type the number of the simulation you would like to try: "))
        print("")
        
        if gamechose == 1:
            print("This simulation will have you trying to guess the color of random hues")
            print("Make sure you answer in tuples EX: (0,0,0)")
            print("Remember that color ranges in RGB are from 0-255")
            programstart = input("Type go to start ")
            while programstart == "go":
                window = pygame.display.set_mode([1000, 500])
                red = random.randint(0, 255)
                green = random.randint(0, 255)
                blue = random.randint(0, 255)
                color = (red, green, blue)
                Rect = pygame.Rect(0, 0, 1000, 500)
                pygame.draw.rect(window, color, Rect)
                pygame.display.flip()
                print("")
                r = int(input("What is the R value? "))
                g = int(input("What is the G value? "))
                b = int(input("What is the B value? "))
                rgbguess = (r, g, b)
                window = pygame.display.set_mode([1000, 500])
                window.fill(rgbguess)
                Rect = pygame.Rect(0, 0, 1000, 500)
                pygame.draw.rect(window, rgbguess, Rect)
                pygame.display.flip()
                print("")
                print("You guessed " + str(rgbguess))
                print("(Pictured Above)")
                print("The real color was " + str(color))
                print("")
                programstart = input("Type go to play again. Or back to go to the menu. Or quit to quit the program: ")
                
        elif gamechose == 2:
            print("My name is Trevor Tang. I am a 9th grader at Sammamish High School")
            print("These series of codes are programs I wrote myself")
            print("They all showcase my skills with the random/pygame library")
            print("There are more than 1,100 LINES IN THIS CODE!")
            print("I hope you enjoy these simulators! :)")
            print("")
            print("")
            programstart = input("Want to go back to the menu? Type back. If not, type quit: ")
        
        elif gamechose == 3:
            print("PATCH NOTES")
            print("=============")
            print("")
            print("V7.1  -Enlarged the window to be able to read the text better")
            print("")
            print("V7.0  -Added pygame section")
            print("      -Added guess the color game")
            print("")
            print("V6.1  -Fixed text bug in count simulator where after every roll, a false message would appear.") 
            print("")
            print("V6.0  -Added a new count simulator within the dice simulator")
            print("      -Added and removed punctuation throughout the whole code")
            print("      -Added semicolons after every input statement")
            print("")
            print("V5.7  -Fixed bug where you could not go back to the menu in dice simulator")
            print("      -If you want to roll more die, you will not be asked to how many die you would like to roll")
            print("      -Simplified the code for dice simulator")
            print("")
            print("V5.6  -The social media simulator will not require you to keep on entering your name if you want to post again")
            print("")
            print("V5.5  -Increased coin flip amount in flip simulator to 100")
            print("      -Added blank lines to various places in the code")
            print("")
            print("V5.4  -You can finally go back to the menu instead of quitting at the end of simulators")
            print("      -Added menu prompt before entering the program to compensate for the new back command")
            print("      -Added quit command in the menu")
            print("")
            print("V5.2  -Added description for Social media simulator")
            print("      -Added loop to be able to post again in social media simulator")
            print("")
            print("V5.1  -Added users into the giveaway simulator if you lost")
            print("      -Now you can enter a username for the giveaways")
            print("")
            print("V5.0  -Added a new category in the giveaway simulator where you can create or join a random giveaway")
            print("")
            print("V4.5: -Now you can choose the min and max numbers you want in the true random number generator")
            print("      -Updated description for lucky number simulator")     
            print("")
            print("V4.1: -Fixed bug when guessing the lucky number right, ending message failed to show")
            print("")
            print("V4.0: -Added new game: Guess the lucky number")
            print("      -Fixed some text bugs")
            print("")
            print("V3.3: -Fixed bug with aces not being wins in war")
            print("      -Fixed computer text with kings in war")
            print("")
            print("V3.2: -Added first and last number as breaks in lucky number drawings for 10k, 100k, and 1mil")
            print("")
            print("V3.1: -Added 100,000 and 1,000,000 to lucky number generator")
            print("")
            print("V3.0: -Added card war game against the computer")
            print("")
            print("V2.0: -Added a lucky number generator")
            print("      -Fixed several bugs")
            print("")
            print("V1.1: -Added loops on generators 1, 2, and 3")
            print("")
            print("V1.0  -First Release out of BETA")
            print("")
            programstart = input("Want to go back to the menu? Type back. If not, type quit: ")

        elif gamechose == 4:
            break
print("")
print("Quitting program...")
print("")   
print("Finished")
print("")
print("Created by: Awpdata")
print("Copyright 2018")

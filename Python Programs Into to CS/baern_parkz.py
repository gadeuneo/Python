# baern_parkz.py
#   Input phrase for another player to guess. Input guesses.
#   Output hangman game: so-far solved phrase, number of guesses remaining, letters guessed so far.
#   By Zoe Park and Nikko Baer


def bubbleSortInPlace(l):
    for nForSorting0ToN in range(len(l) - 1, 0, -1):
        for i in range(nForSorting0ToN):
            if l[i] > l[i + 1]:
                temp = l[i + 1]
                l[i + 1] = l[i]
                l[i] = temp
    return l

# Sorts the list of numbers, returning an independent copy.
# Input: List of numbers.
# Output: List of numbers.
def bubbleSort(l):
	# Python trick: l[:] is a _copy_ of all of l.
    return bubbleSortInPlace(l[:])

def main():
    cont=True
    
    # Initializing user's statistics
    wonGames=0
    lostGames=0
    
    #Starting the game
    while cont==True:
        
        #Input player 1 phrase for player 2 to guess
        legalChars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ -'"
        alphaChars="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        phrase=input("\nEnter a phrase consisting of letters, spaces, dashes, and apostrophes: ".title())
        valid=False
        while valid==False:
            valid=True
            for i in phrase:
                if i not in legalChars:
                    valid=False
            if valid==False:
                phrase=input("\nInvalid phrase. Enter a new phrase consisting \nof letters, spaces, dashes, and apostrophes: ".title())
            isalpha=False
            if valid==True:
                while isalpha==False:
                    for k in phrase:
                        if k in alphaChars:
                            isalpha=True
                    if isalpha==False:
                        phrase=input("\nInvalid phrase. Enter a new phrase containing letters: ".title())
                        valid=False

        # Creating a copy of the phrase with spaces in between the characters to compare
        # with the phrase displayed on screen
        spacedPhrase = ""
        for k in phrase:
            spacedPhrase+=(k+" ")
    
        # Creating the phrase solves so far to be displayed on screen
        solvedPhrase=""
        for j in phrase:
            if j in alphaChars:
                solvedPhrase+="_ "
            else:
                solvedPhrase+=(j+" ")

        # Initializing variables
        remainingGuesses=6
        guessedLetters=""
        
        print("\n"*100)
        # Player 2 inputs here
        while solvedPhrase!=spacedPhrase and remainingGuesses>0:
        
            # Print on-screen messages
            print("\nphrase: ".title()+solvedPhrase)
            print("\nletters guessed so far: ".title()+"".join((bubbleSort(list(guessedLetters)))))
            print("\nnum guesses remaining: ".title()+str(remainingGuesses))
        
            # Input player 2 guess
            guess=input("\nenter the letter you wish to guess: ".title())
            guess = guess.lower()
            while (len(guess)!=1) or (guess not in alphaChars) or (guess in solvedPhrase) or (guess in guessedLetters):
                if ((guess in solvedPhrase) or (guess in guessedLetters)) and not ((len(guess)!=1) or (guess not in alphaChars)):
                    print("\nyou already guessed that letter; try again.".title())
                else:
                    print("\nthat is not a valid character to guess; only letters are allowed.".title())
            
                # Print on-screen messages
                print("\nphrase: ".title()+solvedPhrase)
                print("\nletters guessed so far: ".title()+"".join(bubbleSort(list(guessedLetters))))
                print("\nnum guesses remaining: ".title()+str(remainingGuesses))
            
                guess=input("\nenter the letter you wish to guess: ".title())
                guess = guess.lower()
        
            # Processing guess
            if guess in spacedPhrase or guess.upper() in spacedPhrase:
                print("\nGOOD GUESS!")
                tempPhrase=""
                for letter in range(len(spacedPhrase)):
                    if guess==spacedPhrase[letter] or guess.upper()==spacedPhrase[letter]:
                        tempPhrase+=spacedPhrase[letter]
                    else:
                        tempPhrase+=solvedPhrase[letter]
                solvedPhrase=tempPhrase
            else:
                print("\nINCORRECT GUESS")
                remainingGuesses-=1
            guessedLetters+=guess
        
        #Determining whether they have won or lost
        if remainingGuesses==0:
            print("\nSorry, you lose. The correct phrase was: ".title()+phrase)
            lostGames+=1
        else:
            print("\nCongratulations, you win!".title())
            wonGames+=1
        
        # Asking if they want to play again
        prompt=input("\nDo you want to play again? Type 'yes' or 'no': ".title())
        while len(prompt) ==0:
            prompt=input("\nDo you want to play again? Type 'yes' or 'no': ".title())
        if prompt[0] in "nN":
            cont=False
            print("\nYou won".title(),str(wonGames),"games and lost".title(),str(lostGames),"games.".title())
        while prompt[0] not in "nNyY":
            print("\nplease enter yes or no".title())
            prompt=input("\nDo you want to play again?: ".title())
            if prompt[0] in "nN":
                cont=False
                print("\nYou won".title(),str(wonGames),"games and lost".title(),str(lostGames),"games.".title())
                
main()

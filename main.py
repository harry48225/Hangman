'''
Created on 9 Dec 2015

@author: Harry
'''
'''
Created on 9 Dec 2015

@author: Harry
'''

import random #Needed for random words


words = ['HELLO', 'GOODBYE'] # The list of all of the words


while True: #The main loop
    
    n = random.randint(0,1)             #
                                        #
    chosenWordMaster = list(words[n])   #
    chosenWord = list(words[n])         # These set up lists and choose the word to be guessed
    lettersfound = []                   #
    lettersGuessed = []                 #
    lives = 8                           #
    
    
    for letter in chosenWord:           #
                                        # Adding underscores to the hidden list to show the user how many letters
        lettersfound.append('_')        #
                                
    
    
    while lives > 0:                    # This runs until the user guesses wrong 8 times
        
        print 'Letters guessed: ',      #
        for letter in lettersGuessed:   # Showing the user the letters that have already been guessed
            print letter + '',          # 
            
        print  
        print 'Lives remaining: %d ' % (lives)  #
        for letter in lettersfound:             # This prints the sections of the word that they have already found
            print letter,                       #
       
       
        print      
        letter = raw_input('Please enter a letter: ')               # Asking them to guess a letter
        while len(letter) != 1:                                     #
            print 'You can only enter one letter at a time!'        # Making sure that they have guessed a letter
            letter = raw_input('Please enter a letter: ')           #
            
        
        while letter.upper() in lettersGuessed:                     # making sure that it
            print 'You have already guessed that letter!'           # is one that they haven't already guessed
            letter = raw_input('Please enter a letter: ')           #
            
        letter = letter.upper()     #Making the letter uppercase
            
        if letter in chosenWord:        # Checking if the letter that they have guesses is in the word
            
            while True:                                 #
                if letter in chosenWord:                #
                    x = chosenWord.index(letter)        #
                    lettersfound[x] = chosenWord[x]     # Adding the letters that they have guessed to the list and replacing the under scores in it.
                    chosenWord[x] = '_'                 #
                else:                                   #
                    break                               #
            print 'That was correct!'                   #
            
        else:
            print 'That was wrong!'     # Letter is not in the chosen word
            lives -= 1
        lettersGuessed.append(letter)
        
        if lettersfound == chosenWordMaster: # If they have found the entire word
            
            print 'You win!'
            print 'The word was ' + words[n]  # Prints the word
            break
        
    if lives == 0:  # Printing game over if they run out of lives
        print 'Gameover'
        
    again = raw_input('Would you like to play again? y/n: ')    #
    while again.upper() not in ['YES', 'Y', 'NO', 'N']:         # Want to play again?
        print 'Error invalid response!'                         #
        again = raw_input('Would you like to play again? y/n: ')#
    
    if again in ['NO', 'NO']:
        break                   # Breaking out of the entire loop and therefore ending the program if they do not want to play again

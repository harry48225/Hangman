'''
Created on 9 Dec 2015

@author: Harry
'''
'''
Created on 9 Dec 2015

@author: Harry
'''

import random #Needed for random words
import time


    


print 'Hello and welcome to HangMan!' #Welcome statement

playing = 1

while playing == 1:
    
    wLIST = 0
    wordfile = open('words.txt', 'r+')

    words = wordfile.read().split() # The list of all of the words

    for word in words:
    
        wLIST += 1

    wLIST -= 1
    
    AsciiArt =  ['    _________', '    |         |', '    |         0', '    |        /|\\', '    |        / \\', '    |', '    |']
    for line in AsciiArt: print line
    print
    print
    print 'Menu'
    print 'Play HangMan(1)'
    print 'Add a word(2)'
    print 'View all words(3)'
    print 'Quit(4)'
    option = raw_input('Select an option: ')
    
    option = int(option) #Converting it to a number
    
    if option == 1:
    
        while True: #The main loop
            
            n = random.randint(0, wLIST)             #
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
                
            again = int(raw_input('Enter a number 1(playagain) 2(menu) 3(exit): '))    #
            while again not in [1, 2, 3]:         # Want to play again?
                print 'Error invalid response!'                         #
                again = int(raw_input('Enter a number 1(playagain) 2(menu) 3(exit): '))#
            
            if again == 2:
                break                   # Breaking out of the game loop and therefore returning to the menu
            elif again == 3:
                playing = 0
    
                break
    
    if option == 2: 
        
        while True:
            newWord = raw_input('Please enter a new word: ').upper()
            
            if ' ' in newWord:
                print 'You must only enter ONE word!'
                
            elif newWord in words:
                print 'You must enter a NEW word!'
                
            else:
                break
        
        newWord = ' ' + newWord  
        wordfile = open('words.txt', 'a')
        wordfile.write(newWord)
        print 'Word added!'
        
    if option == 3:
        linebreak = 0
        for word in words:   
            
            time.sleep(0.1)
            if linebreak == 2:
                print word
                linebreak = 0
            
            else:    
                print word + ' ',
                linebreak += 1
    
    print
    raw_input('Press enter to continue!')        
    if option == 4:
        
        playing = 0
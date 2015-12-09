'''
Created on 9 Dec 2015

@author: Harry
'''
'''
Created on 9 Dec 2015

@author: Harry
'''

import random


words = ['HELLO', 'GOODBYE']

n = random.randint(0,1)

chosenWordMaster = list(words[n])
chosenWord = list(words[n])
lettersfound = []
lettersGuessed = []
lives = 8


for letter in chosenWord:
    
    lettersfound.append('_')
    


while lives > 0:
    
    print 'Letters guessed: ',
    for letter in lettersGuessed:
        print letter + '',
        
    print  
    print 'Lives remaining: %d ' % (lives)
    for letter in lettersfound:
        print letter,
   
   
    print      
    letter = raw_input('Please enter a letter: ').upper()
    while letter in lettersGuessed:
        print 'You have already guessed that letter!'
        letter = raw_input('Please enter a letter: ').upper()
        

    if letter in chosenWord:
        
        while True:
            if letter in chosenWord:
                x = chosenWord.index(letter)
                lettersfound[x] = chosenWord[x]
                chosenWord[x] = '_'
            else:
                break
        print 'That was correct!'
        
    else:
        print 'That was wrong!'
        lives -= 1
    lettersGuessed.append(letter)
    if lettersfound == chosenWordMaster:
        
        print 'You win!'
        break
    
if lives == 0:
    print 'Gameover'
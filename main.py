'''
Created on 9 Dec 2015

@author: Harry
'''
'''
Created on 9 Dec 2015

@author: Harry
'''

import random


words = ['Hello', 'Goodbye']

n = random.randint(0,1)

chosenWord = list(words[n])
lettersfound = []
lettersGuessed = []
print chosenWord

for letter in chosenWord:
    
    lettersfound.append('_')

while True:
    
    for letter in lettersfound:
        print letter,
   
   
    print      
    letter = raw_input('Please enter a letter: ')
    while letter in lettersGuessed:
        print 'You have already guessed that letter!'
        letter = raw_input('Please enter a letter: ')
        

    if letter in chosenWord:
        
        while True:
            if letter in chosenWord:
                x = chosenWord.index(letter)
                lettersfound[x] = chosenWord[x]
                chosenWord[x] = '_'
            else:
                break
        print 'That was correct!'
        print chosenWord
    else:
        print 'That was wrong!'
    lettersGuessed.append(letter)
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
print chosenWord

for letter in chosenWord:
    
    lettersfound.append('_')

while True:
    print lettersfound    
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
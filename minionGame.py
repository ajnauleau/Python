# Kevin and Stuart want to play the 'The Minion Game'.

## Game Rule ##s

# Both players are given the same string, .
# Both players have to make substrings using the letters of the string.
# Stuart has to make words starting with consonants.
# Kevin has to make words starting with vowels.
# The game ends when both players have made all possible substrings.

## Scoring ##
# A player gets +1 point for each occurrence of the substring in the string.

## INPUT IN CAPS ! ##

def minion_game(string):
    
    vowels = ['A','E','I','O','U']
    consts = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    kevin = 0
    stuart = 0
    vowelArray = []
    constsArray = []
    
    for letter in string:
        
        for v in vowels:
            if (letter == v):
                vowelArray.append(letter)
                
        for c in consts:
            if (letter == c):
                constsArray.append(letter)
                
    cleanvowelArray = list(set(vowelArray))
    
    for vowel in cleanvowelArray:
        s = string
        index = string.index(vowel)
        initpattern = string[index:]
        initscore = s.count(initpattern)
        kevin = initscore
        
        for subString in range(len(string[index:])-1):
            pattern = string[index:-(subString+1)]
            score = s.count(pattern)
            kevin = kevin + score
        
                
    cleanconstsArray = list(set(constsArray))
    
    for consts in cleanconstsArray:
        s = string
        index = string.index(consts)
        initpattern = string[index:]
        initscore = s.count(initpattern)
        stuart = initscore + stuart
        
        for subString in range(len(string[index:])-1):
            pattern = string[index:-(subString+1)]
            score = s.count(pattern)
            stuart = stuart + score

    if (stuart > kevin):
        print("Stuart %s" % stuart)
    elif (stuart < kevin):
        print("Kevin %s" % kevin)
    else:
        print("Draw")

if __name__ == '__main__':
    print("Spell a word in CAPS")
    s = input()
    minion_game(s)

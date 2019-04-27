# File name: problemSetDay9.py
word = 'code'
list(word)
blank = '_'
gp = list(blank)
gp *= len(word)
print(gp)
guessnum = 0
userguess = input("Enter a letter ")
gp[4]
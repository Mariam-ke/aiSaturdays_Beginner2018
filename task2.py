import random

words = [word.rstrip('\n')[::-1] for word in open('words.txt')][::-1]
randomPhrase = " ".join([words[random.randrange(0, len(words))] for i in range(4)])

print randomPhrase

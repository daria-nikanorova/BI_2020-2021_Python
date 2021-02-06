import numpy as np
import random

text = input().split()
messy_text = []
for word in text:
    letters = np.array([letter for letter in word])
    random.shuffle(letters[1:-1])
    word = (''.join(letters))
    messy_text += [word]
messy_text = (' '.join(messy_text))
print(messy_text)

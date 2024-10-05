import random
import time
fakts = []
for i in range(4):
    fakt = input("Podaj fakt o sobie.")
    fakts.append(fakt)
time.sleep(2)
print(random.choice(fakts))

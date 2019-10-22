import numpy as np
import matplotlib.pyplot as plt


MAX = 5  # maximum heigght of sandpile
width = 9
height = 9
SANDPILE = np.zeros((width, height))  # 10x10 array
NUM_ITER = 1000
print(SANDPILE)


for i in range(NUM_ITER):
    SANDPILE[int(width/2)][int(height/2)] += 1
    for x in range(0, width, 1):
        for y in range(0, height, 1):

            if SANDPILE[x][y] < MAX:
                SANDPILE[x][y] = SANDPILE[x][y]

            elif SANDPILE[x][y] >= MAX:
                SANDPILE[x][y] = SANDPILE[x][y] - 4
                if x + 1 < width:
                    SANDPILE[x + 1][y] += 1
                if x - 1 >= 0:
                    SANDPILE[x - 1][y] += 1
                if y + 1 < height:
                    SANDPILE[x][y + 1] += 1
                if y - 1 >= 0:
                    SANDPILE[x][y - 1] += 1

            print(SANDPILE)



print("Final Sandpile")
print(SANDPILE)

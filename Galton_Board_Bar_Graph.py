import numpy as np
from random import randint
import random
import sys
import math 
import matplotlib.pyplot as plt
import scipy.stats as st

N=51 # no of columns
board = np.zeros((N,N))

def force(containers, y_index):
    left = 0
    right = 0
    for i in range(len(containers)):
        if i < y_index:
            left += containers[i]
        if i > y_index:
            right += containers[i]
    return right - left

B = 10000 # No of balls

def normal():
    containers = [0] * (N)
    for _ in range(B):
        pos = 0
        for _ in range(0, N-1):
            turn = randint(0, 1)
            if turn == 1:
                pos += 1
        containers[pos] = containers[pos] + 1
        containers = np.array(containers)
    board[N-1] = containers 


def magnetic():
    for _ in range(B):
        index = N//2
        for _ in range(0, N-1):
            force_ = force(board[N-1], index)
            a_list = [0,1]
            factor = 0.75 #Value between 0 and 1 with 1 being maximum magnetism and 0 is no magnetism
            left_prob = max(0, .5 - factor*(force_/B))
            distribution = [left_prob, 1 - left_prob]
            turn = random.choices(a_list, distribution)
            if turn == [0]:
                index = max(0, index - 1)
            if turn == [1]:
                index = min(N-1, index + 1)
        board[N-1][index] = board[N-1][index] + 1

def curved():
    for _ in range(B):
        index = N // 2
        a_list = [0, 1]
        distribution = [.5, .5]
        turn = random.choices(a_list, distribution)
        curved_factor = 0.75  #0 to be no curve and 0.99 to be the maximum
        if turn == [0]:
            distribution = [0.5 + curved_factor*0.5, 1-0.5 - curved_factor*0.5]
        if turn == [1]:
            distribution = [1-0.5 - curved_factor*0.5, 0.5 + curved_factor*0.5]
        for _ in range(1, N - 1):
            turn = random.choices(a_list, distribution)
            if turn == [0]:
                index = max(0, index - 1)
            if turn == [1]:
                index = min(N-1, index + 1)
        board[N - 1][index] = board[N - 1][index] + 1

option = 0  #0 for normal, 1 for magnetic, 2 for curved
if option == 0:
    normal()
elif option == 1:
    magnetic()
else:
    curved()


container = board[N-1]
x_axis = np.arange(1, len(board[N-1]) + 1)


plt.bar(x_axis,container, label="Number of Balls")
plt.legend()

plt.xlabel('Container')
plt.ylabel('Balls')
plt.title('Galton Board')
plt.show()






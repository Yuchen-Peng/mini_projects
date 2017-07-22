'''
Random move hanoi tower: at each step one of all valid moves is taken at uniform random; calculate the mean and standard deviation
for the center of mass for all plates after T random move
'''

from random import randint
from __future__ import division
import numpy as np

def validstate(position,N):
# return all valid states given the previous position 
    space = list()
    l = len(position)
    for i in range(l):
        if position[i] + 1 < N and (position[i] + 1) not in position[0:i] and position[i] not in position[0:i]:
            new_position = position[:]
            new_position[i] += 1
            if new_position not in space:
                space.append(new_position)
        if position[i] - 1 > -1 and (position[i] - 1) not in position[0:i] and position[i] not in position[0:i]:
            new_position = position[:]
            new_position[i] -= 1
            if new_position not in space:
                space.append(new_position)
    return space

def initial_position(M):
    ini_position = []
    for i in range(M):
        ini_position.append(0)
    return ini_position

def stat(M,N,T,n=1000000):
    center_list = list()
    for iter in range(n):
        ini_position = initial_position(M)
        position = ini_position
        for t in range(T):
            space = validstate(position,N)
            position = space[randint(0,len(space)-1)]
        sum_p = 0
        sum_m = 0
        for i in range(M):
            sum_m += (i+1)
            sum_p += (i+1)*position[i]
        center = sum_p/sum_m
        center_list.append(center)

    return np.array(center_list).mean(), np.array(center_list).std()

stat(3,3,16)

stat(6,6,256)
        

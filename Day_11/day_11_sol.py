#!/bin/python3
import math
import os
import random
import re
import sys

class HourG:
    def __init__(self, array):
        self.A = array
    def hourGlass(self):
        soma = []
        for i in range(0, (int(len(self.A)/2))+1):
            for j in range(0, (int(len(self.A[0])/2))+1):
                aa = [self.A[i][j], self.A[i][j+1], self.A[i][j+2], self.A[i+1][j+1],
                      self.A[i+2][j], self.A[i+2][j+1], self.A[i+2][j+2]]
                soma.append(sum(aa))
        print (max(soma))

if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    hg = HourG(arr)
    hg.hourGlass()

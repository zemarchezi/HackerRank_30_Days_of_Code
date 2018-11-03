#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = float(meal_cost) * (int(tip_percent) / 100)
    tax = float(meal_cost) * (int(tax_percent) / 100)
    totalCost = float(meal_cost) + tip + tax
    roundCost = int(round(totalCost))
    return (print('The total meal cost is %d dollars.' % (roundCost)))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = int(input())

    tax_percent = int(input())

    solve(meal_cost, tip_percent, tax_percent)

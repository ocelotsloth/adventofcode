from numpy import loadtxt
from itertools import combinations
from math import prod

numbers = loadtxt("input", comments="#", delimiter="\n", dtype=int)

for pair in combinations(numbers, 2):
    if sum(pair) == 2020:
        answer = prod(pair)
        print("SOLVED: " + str(answer))


#!/bin/python3

class ConsecInteger:
    def __init__(self, n):
        self.n = n
    def consecInteger(self):
        binN = bin(self.n)[2:]

        ones = binN.split('0')
        countConsec = []
        for i in range(0,len(ones)):
            countConsec.append(ones[i].count('1'))

        print (max(countConsec))


if __name__ == '__main__':
    n = int(input())

    dd = ConsecInteger(n)
    dd.consecInteger()

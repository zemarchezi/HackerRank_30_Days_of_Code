#!/bin/python3
#Write your code here
import sys
# do not necesearlly requires that, Iǘe just putted it to
# remember that it exsists
from collections import deque
class Solution:
    # Write your code here
    def __init__(self):
        self.stack = []
        self.queue = deque([])
    def pushCharacter(self, st):
        self.stack.append(st)

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        return (self.stack.pop())
    def dequeueCharacter(self):
        ### This is if you are not using the 'deque' method
        # ch = self.queue[0]
        # self.queue = self.queue[1:]
        # return (ch)
        ### Using the 'deque' method
        return (self.queue.popleft())


# read the string s
s=input()
#Create the Solution class object
obj=Solution()

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")  

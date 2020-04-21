import sys
from collections import deque

class Solution:
    def __init__(self):
        self.queue = deque()
        self.stack = list()

    # implementation of queue
    # insert each character of string s into queue
    def enqueueCharacter(self, s):
        self.queue.append(s)

    # implementation of stack
    # insert each character of string s into stack
    def pushCharacter(self, s):
        self.stack.append(s)

    def dequeueCharacter(self):
        x = self.queue.popleft()
        return x

    def popCharacter(self):
        z = self.stack.pop()
        return z

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
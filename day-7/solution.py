# Solution accepted by hackerrank but not my python editor
if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().rstrip().split()))
    for i in range(n):
            print(arr[n-i-1], end=" ")



# Solution correct using python editor
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = input()
    n = int(n)
    term = list()
    if isinstance(n, int):
        if 1 <= n <= 1000:
            for i in range(n):
                take_input = input()
                take_input_valid = int(take_input)
                if isinstance(take_input_valid, int):
                    if 1 <= take_input_valid <= 10000:
                        term.append(take_input_valid)
        reverse_term = term[::-1]
        list_to_str =' '.join(map(str, term)) 
        reverse_list_to_str = ' '.join(map(str, reverse_term)) 
        print(list_to_str)
        print(reverse_list_to_str)
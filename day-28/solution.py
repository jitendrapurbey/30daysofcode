#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input())

    names = list()
    for N_itr in range(N):
        firstNameEmailID = input().split()

        firstName = firstNameEmailID[0]

        emailID = firstNameEmailID[1]
        x = re.findall("@gmail.com$", emailID)
        if x:
            names.append(firstName)
    sorted_names = sorted(names)
    for i in range(len(sorted_names)):
        print(sorted_names[i]) 
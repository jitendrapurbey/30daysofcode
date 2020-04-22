# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def isprime(num):
    if num == 1:
        return "Not prime"
    sq = int(math.sqrt(num))
    for x in range(2, sq+1):
        if num % x == 0:
            return "Not prime"
    return "Prime"
    

if __name__ == "__main__":
    t = int(input())
    if 1 <= t <= 30:
        for i in range(t):
            n = int(input())
            if 1 <= n <= 2*10**9:
                j = isprime(n)
                print(j)
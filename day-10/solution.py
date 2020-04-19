#mine solution
# converts decimal number to binary
def decimal_to_binary(n):
    if 1 <= n <= 10 ** 6:
        list_binary = list()
        num = int(n / 2)
        binary = n % 2
        list_binary.append(binary)
        while num != 0:
            binary = num % 2
            num = int(num / 2)
            list_binary.append(binary)
        binary_no_list = list_binary[::-1]
        return binary_no_list


if __name__ == '__main__':
    # find maximum number of consecutive 1s in the binary representation of n
    num = int(input())
    n = decimal_to_binary(num)
    list_of_1s = list()
    count = 0
    length = len(n)
    for rank, i in enumerate(n):
        if i == 1:
            count = count + 1
        if i == 0:
            if count != 0:
                list_of_1s.append(count)
            count = 0
        if rank == length - 1:
            list_of_1s.append(count)
            break
    print(max(list_of_1s))



# other solution
import sys, math

n = int(input().strip())
count = 0
maxi = 0
while n > 0:
    if n % 2 == 1:
        count += 1
    else:
        if count > maxi:
            maxi = count
        count = 0
    n=math.floor(n / 2)
if count > maxi:
    maxi = count
print(maxi)
    

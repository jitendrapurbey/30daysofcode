# Enter your code here. Read input from STDIN. Print output to STDOUT

test_times = int(input())
if 1<=test_times and test_times <=10:
    for no_of_times in range(test_times):
        take_input = input()
        length_of_input = len(take_input)
        even_words = []
        odd_words = []
        if 2 <= length_of_input <=10000:
            for i in range(length_of_input):
                even_or_odd = i % 2
                if even_or_odd == 0:
                    even_word = ''
                    even_letter = take_input[i]
                    even_word = even_word + even_letter
                    even_words.append(even_word)
                else:
                    odd_word = ''
                    odd_letter = take_input[i]
                    odd_word = odd_word + odd_letter
                    odd_words.append(odd_word)

            even = ''.join(even_words)
            odd = ''.join(odd_words)

            whole_word = even + " " + odd
            print(whole_word)        


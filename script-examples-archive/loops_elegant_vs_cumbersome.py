
'''
Write a program that reads from the console integers (one for a line)
until their sum is equal to 0. Immediately after that, it should display
the sum of the squares of all the entered numbers.

It is guaranteed that at some point the sum of the entered numbers will be
equal to 0. After that, you should stop reading the input.

In case the first integer equals to 0, just print out 0 instead of the
sum of the squares.

You only need to output the sum of the squares once.
'''

# Sean Ravenhill

total = 0
total_squared = 0

while True:
    number = int(input())
    total += number
    if total != 0:
        total_squared += number * number
        continue
    elif total == 0:
        total_squared += number * number
        print(total_squared)
        break
    else:
        print(0)
        break


# Username: l33T

n_sum = int(input())
s_sum = n_sum * n_sum

while n_sum != 0:
    temp_var = int(input())
    n_sum += temp_var
    s_sum += temp_var * temp_var

print(s_sum)

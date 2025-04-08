

# Sum of Digits / Digital Root (6 kyu) Codewars

'''
Description:
Digital root is the recursive sum of all the digits in a number.

Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
The input will be a non-negative integer.
'''

def digital_root(n):

    sum_digits = 0

    if (n <= 9):
        return n
    else:
        while n > 9:
            sum_digits = 0
            for i in str(n):
                sum_digits += int(i)

            n = sum_digits
                
        return sum_digits

n = 942
print(digital_root(n))




def reverse(num):
    return int(num[::-1])


def palindrome(num1):
    if reverse(num1)== int(num1):
        print('palindrome')
    else:
        print('not a palindrome')


palindrome(input('enter a number:'))

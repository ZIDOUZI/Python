def is_odd(n):
    return n % 2 == 1


while True:
    s = input('Enter a number:')
    if s == 'q':
        break
    if is_odd(eval(s)):
        print('The number is odd')
    else:
        print('The number is not odd')

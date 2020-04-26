def main():
    number = int(input('Enter a non-negative integer: '))
    if number < 0:
        print('Your number must be a non-negative.')
    else:
        y = 1
        for num in range (1, number+1):
            y *= num
        print(number, 'Factorial is', y)
main()
#  REsQUIREMENTS

# 1) Write a program that performs the following tasks:

# 2) Write a main function that reads one symbol, 2 integer and draws the figure similar to the following picture.

# 3) Your main function should call DrawRectangle and DrawTriangle functions to draws the figure below.

# 4) You should have a function drawBar(symbol, length) which use a loop to draw a horizontal bar of length with the symbol filled.

# 5) DrawRectangle function takes 3 arguments (symbol, width, and height) which calls DrawBar.

# 6) DrawTriangle function takes 2 arguments (symbol and height) which calls DrawBar. exercise. You can make this function with 3 arguments (symbol, height, and direction).

def main():
    symbol = input('Enter the symbol for the shapes: ')

    width = int(input('Enter the width of the shape: '))

    height = int(input('Enter the height of the shapes: '))

    DrawRectangle(symbol, width, height)

    DrawTriangle(symbol, height)



def DrawBar(symbol, width):
    bar = symbol * width
    print(bar)

def DrawRectangle(symbol, width, height):
    n = 0
    while n < height:
        DrawBar(symbol, width)
        n += 1
    print("\n")

def DrawTriangle(symbol, width):
    rows = (width * 2) - 1
    i = 1
    while i <= rows:
        if i > width:
            actual_row = width - (i - width)
        else:
            actual_row = i
        DrawBar(symbol, actual_row)
        i += 1

main()
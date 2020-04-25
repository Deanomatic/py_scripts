#  Problem Specification:
# Write a program described below:
# Read an integer value between 2 and 20 and store the value as upper.
# Using a nested-loop print the multiplication table from 2 to the upper value.
# Using a loop print the heading as shown below.

# variable containing the input and the int value of upper
upper = int(input('What is the upper bound of multiplication table (between 2 & 20)? '))
# variable for interating through upper. Needs to start at 2 because 2 is the lowest multiply per requirements
i = 2
# used to help format the table and numbers
spacer = "   "
# lengthening the divider based on upper value
print("----" * upper)
# adding initial space for top row of numbers in table
print(spacer + spacer, end="")
# looping through upper and printng out each numbering counting till
# it equals upper
while i <= upper:
    print(str(i) + spacer, end="")
    i += 1
# another dividing line
print("\n", "----" * upper)
# variable for lowest possible multiplication number
starting_num = 2
# variable used for looping through upper value again
counter = 2
# nested loop for printing out the rest of the table
while starting_num <= upper:
    # prints the first 2 numbers in each row
    print(str(starting_num) + "|" + spacer + str(starting_num * 2) + spacer, end="")
    # prints out the rest of the numbers in each row 
    while counter < upper:
        print(str(starting_num * (counter + 1)) + spacer, end="")
        counter += 1
    # creates new row of numbers
    print("\n")
    # resetting the counter so that it will print more rows for each loop through the upper value
    counter = 2
    # raising upper value by 1
    starting_num += 1

f = open(input("Enter your file path you wish to calculate: "), "r")
# /Users/deansmith/workspace/python-exercises/python_homework/steps.txt
steps_count = list(f.read().splitlines())
# setting a list of dictionaries to define an int value per month. This is used to properly loop through and divide 
# up the steps
months = {'January': 31, 'Febuary': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}
# Variable used to track and seperate amount of days per month
counter = 0
steps_list = list()
# For loop that iterates through the monnths list
# items() gets each dict key value pair
# month is the string, days is the int value
for month, days in months.items():
    # looping the numbers in file line by line
    for step in steps_count:
        if counter < days:
            num_of_steps = int(step)
            # adding the numbers to the empty steps_list
            steps_list.append(num_of_steps)
            counter += 1
            # calculatoing the average of steps in a month
            average_steps = sum(steps_list) / counter
    # removing already calculated numbers from the steps_count list
    del steps_count[0:days]
    print("The average steps taken in " + month + "is " + str(average_steps))
    # reseting the list to be used again
    steps_list = list()
    counter += 1
    # reseting the counter for the next month in the list
    counter = 0


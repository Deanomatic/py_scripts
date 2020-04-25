f = open(input("Enter your file path you wish to calculate: "), "r")
# /Users/deansmith/workspace/python-exercises/python_homework/steps.txt
steps_count = list(f.read().splitlines())

months = {'January': 31, 'Febuary': 28, 'March': 31, 'April': 30, 'May': 31, 'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

counter = 0
steps_list = list()
for month, days in months.items():
    for step in steps_count:
        if counter < days:
            num_of_steps = int(step)
            steps_list.append(num_of_steps)
            counter += 1
            # print(num_of_steps, "step -", counter)
            average_steps = sum(steps_list) / counter
    del steps_count[0:days]
    print("The average steps taken in " + month + "is " + str(average_steps))
    steps_list = list()
    counter += 1
    counter = 0


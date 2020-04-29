import re
# 1) Input takes a file path
# 2) Read the file
# 3) Find all valid emails in file
# 4) Count all emails
# 5) Output count of emails 
# 6) Output emails
# 7) Input takes another file path
# 8) Write emails to new file path

f = open(input("Enter your file path you wish to read: "), "r")
#/Users/deansmith/workspace/python_fun/email-inputB.txt
emails = list(f.read().splitlines())
# lst = re.findall('^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$', emails)
count = len(emails)
print("Found" + str(count) + "valid eamil addresses")
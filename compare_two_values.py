# VISA full time master's MCQ.
# def func(a, b):
#     x = a
#     y = b
#     while x != y:
#         if x > y:
#             x = x - y
#         if x < y:
#             y = y - x
#     return x or y
#
#
# print(func(2437, 875))

import re


# Open the file in the read mode
# fname = input("Enter the file name")
def main():
    fname = 'C:/Users/Jenil/Desktop/201210.txt'
    with open(fname) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    # print(content)
    count_initial = 0
    no_of_emails = 0
    counter = 0
    # for line in content:
        # string_search = re.compile(r'(From java)')
    # print(string_search)
    email_unique_array = []  # Declare a array for storing the unique email addresses

    for line in content:
        # search using the string where there are lines starting from 'From java' which contains the email addresses in it
        searchObject = string_search.search(line)
        if searchObject != None:
            # Increment the count if the searchObject is not empty
            count_initial = count_initial + 1
        emailregex = re.findall('\S+@\S+', line)
        emailregexset = set(emailregex)
        if len(set(emailregex)) != 0:

            for email in emailregex:

                if email not in email_unique_array:
                    email_unique_array.append(email)
                    no_of_emails = no_of_emails + 1

    # Print the output
    print('Total Number of email messages in file:', count_initial)
    print('Total Number of unique email addresses: ', no_of_emails)
    print('All the unique email addresses in the file are: \n')
    for uniqueemail in email_unique_array:
        print(uniqueemail)


if __name__ == '__main__':
    main()

# # Q1
numbers = [1, 2, 3, 4, 5]
print(numbers[1:-5])
# It displays [].
print(numbers[:])


# Q2
sales_list = []
days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
for d in days:
    sale = input(f'Enter the sales on {d}: ')
    sales_list.append(float(sale))

total_sales = 0.0
for s in sales_list:
    total_sales += s

print(f"Total sales: {total_sales}")

# Q3
places = ['Vatican', 'Zoo', 'Texas', 'Museum', 'Egypt', 'Mexico']
print(places)
places.sort()
print(places)
places.sort(reverse=True)
print(places)


# Q4
courses= ['DATA606', 'DATA607', 'DATA605', 'DATA602']
course_rooms={'DATA606': '102', 'DATA607': '105', 'DATA605': '201', 'DATA602': '205'}
course_instructors={'DATA606': 'Jane', 'DATA607': 'Tom', 'DATA605': 'Mark', 'DATA602': 'Travis'}
course_times={'DATA606': '6pm', 'DATA607': '7pm', 'DATA605': '6pm', 'DATA602': '8pm'}

while True:
    print("Course numbers:", courses)
    choice = input("Enter Q to quit, or enter a course number from the list to see it's info: ")
    if (choice == 'Q' or choice == 'q'):
        print("Quitting the program...")
        break
    elif (choice not in course_rooms.keys()):
        print("That's not a course number. Enter a valid course number, or Q to quit.")
        print()
    else:
        print(f"Here is the info for {choice}: ")
        print('Room number:', course_rooms[choice])
        print('Instructor:', course_instructors[choice])
        print('Meeting time:', course_times[choice])
        print()

# Q5
address_book = {"Jake": 'jake@collegehumor.com', "Amir": 'amir@collegehumor.com', "Ben": 'ben@collegehumor.com', "Rosie": 'rosie@collegehumor.com'}
names = ['Jake', 'Amir', 'Ben', 'Rosie']
while True:
    print('People in your address book:', names)
    choice = input(f'Options:\n'
                   f'L: Look up a person\'s email address.\n'
                   f'A: Add a new name and email address.\n'
                   f'C: Change an existing email address.\n'
                   f'D: Delete an existing name and email address.\n'
                   f'Q: Quit the program.\n')
    print()
    if (choice.upper() == 'Q'):
        print("Quitting the program...")
        break
    elif (choice.upper() == 'L'):
        name = input("Enter the name of the person whose email you want to look up: ")

        if name not in names:
            print("That name is not in the address book. Please enter a valid name.")
        else:
            print(f'{name}\'s email address is {address_book[name]}.')

    elif (choice.upper() == 'A'):
        name = input("Enter the name of the new person: ")
        email = input("Enter the new person's email address: ")
        names.append(name)
        address_book[name] = email
        print("New person added!")

    elif (choice.upper() == 'C'):
        name = input("Enter the name of the person whose email will change: ")
        new_email = input("Enter the new email: ")
        address_book[name] = new_email
        print("The email changed.")

    elif (choice.upper() == 'D'):
        name = input('Enter the name of the person who will be deleted from the address book: ')
        del address_book[name]
        names.remove(name)
        print("The person was deleted.")

    else:
        print("Please enter a valid option.")




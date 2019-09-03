checklist = list()

# Create
def create(item):
    checklist.append(item)

# Read
def read(index):
    print(checklist[index])
    return checklist[index]

# Update official
def update(index, item):
    checklist[index] = item

# Destroy official
def destroy(index):
    checklist.pop(index)

# List all items
def list_all_items(): # Python is linear, reads from top to bottom
    index = 0
    for list_item in checklist:
        print("{} {}".format(index, list_item))
        # old python print = print(str(index) + list_item)
        index += 1

# Mark Complete
def mark_completed(index):
    print("^_^" + str(checklist[index]))

# User input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

# User input
# function_code = input("Please Enter a value:")
# print(function_code)

# Select Function code
def select(function_code):
    # Create item
    if function_code == "C":
        input_item = user_input("Input item to add: ")
        create(input_item)
    # READ
    elif function_code == "R":
        item_index = int(user_input("Display at which index in list: "))
        # Remember that item_index must actually exist or our program will crash.
        read(item_index)
    # Print all items
    elif function_code == "P":
        list_all_items()
    elif function_code == "D":
        user_index = int(user_input("Index to remove: "))
        destroy(user_index)
    elif function_code == "M":
        item_index = int(user_input("Enter index to add mark: "))
        mark_completed(item_index)
    elif function_code == "U":
        index_item = int(user_input("Enter index of list to update: "))
        item = user_input("Enter item to update: ")
        update(index_item, item)
    elif function_code == "Q":
        return False
    # Catch all
    else:
        print("Unknown Option")
    return True
# Run Tests
#test()

running = True
while running:
    selection = user_input(
        "Press C to add to list, R to read from list, U to update list, "
        "\nD to destroy list, P to display full list, and Q to quit\n")
    running = select(selection)


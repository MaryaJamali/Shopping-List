# make a list to hold onto our items
shopping_list = []
# print out instructions on how use the app
print("What should we use at the store? ")
print("Enter 'DONE' to stop adding items. ")
while True:
    # ask for new item
    new_item = input("---> ")
    # be able to quit the app
    if new_item.upper() == "DONE":
        break
    # add new item to our list
    shopping_list.append(new_item)
# print out the list
print("Here's your list: ")
for item in shopping_list:
    print(item)


# Function shopping_list program
# make a list to hold onto our items
shopping_list = []


def show_help():
    # print out instructions on how use the app
    print("What should we use at the store? ")
    print("Enter 'DONE' to stop adding items. ")
    print("Enter 'HELP' to show all instruction in our app. ")
    print("Enter 'SHOW' to show all items in our shopping list. ")


def show_list():
    # print out the list
    print("Here's your list: ")
    for item in shopping_list:
        print(item)


def add_to_list(new_item):
    # add new item to our list
    shopping_list.append(new_item)
    print("Added {item} to list now. the list now has {count_items} items"
          .format(item=new_item, count_items=len(shopping_list)))


def run_app():
    show_list()
    while True:
        # ask for new item
        new_item = input("---> ")
        # be able to quit the app
        if new_item.upper() == "DONE":
            break
        elif new_item.upper() == "HELP":
            show_help()
            continue
        elif new_item.upper() == "SHOW":
            show_list()
            continue
        else:
            add_to_list(new_item)


run_app()

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali

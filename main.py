
"""
Library management project

"""
import adding, removing, updating, viewing


booklist = []

print("Welcome to Library management system\nSelect your operation")
print("0 for exit.\n1 for adding new books\n2 for removing books")
print("3 for updating book \n4 for viewing book list ")

while True:
    option = input("Enter your operation ")

    if option == "0":
        break
    elif option == "1":
        booklist = adding.add_books(booklist)
    elif option == "2":
        booklist = removing.remove_books(booklist)
    elif option == "3":
        booklist = updating.update_books(booklist)
    elif option == "4":
       viewing.print_books(booklist)
    else:
        print("Invalid operation\n")

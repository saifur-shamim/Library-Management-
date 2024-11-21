
def update_books(booklist):
    id =int(input("Enter the book id which you want to update "))

    f = False
    for book in booklist:
        if book["ID"]==id:
            print("Enter the new data of the updating book ")
            book["ID"] = int(input("Enter the id: "))
            book["Title"] = input("Enter the name of book ")
            book["Author"] = input("Enter the name of author ")
            book["ISBN"] = input("Enter the ISBN number ")
            book["Year"] = input("Enter the publishing year ")
            book["Price"] = float(input("Enter the price "))
            book["Quantity"] = input("Enter the quantity ")
            print("Updated Successfully")
            f=True
            break

    if f==False:
       print(f"Error! the book is not in the list ")

    return booklist
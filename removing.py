
def remove_books(booklist):
    print("Provide the following info of the removing book")
    id = int(input("Enter the book id: "))
    title = input("Enter the name of book ")
    author = input("Enter the name of author ")
    isbn = input("Enter the ISBN number ")
    year = input("Enter the publishing year ")
    price = float(input("Enter the price "))
    quantity = input("Enter the quantity ")

    book = {
        "ID": id,
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Year": year,
        "Price": price,
        "Quantity": quantity,
    }

    if book in booklist:
        booklist.remove(book)
        print(f"{book['Title']} removed successfully")
    else:
        print(f"{book['Title']} does not exist in the list ")

    return booklist
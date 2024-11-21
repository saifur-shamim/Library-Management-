
from save_books import save_all_books
def add_books(booklist):
    id = int(input("Enter the book ID: "))
    title = input("Enter the name of book ")
    author = input("Enter the name of author ")
    isbn = input("Enter the ISBN number ")
    year = input("Enter the publishing year ")
    price = float(input("Enter the price "))
    quantity = input("Enter the quantity ")

    book = {
        "ID" : id ,
        "Title": title,
        "Author": author,
        "ISBN": isbn,
        "Year": year,
        "Price": price,
        "Quantity": quantity,
    }

    booklist.append(book)
    save_all_books(booklist)

    print(f"'{title}' added successfully")

    return booklist
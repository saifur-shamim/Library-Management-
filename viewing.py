
def print_books(booklist):
    if booklist != []:
        for book in booklist:
            print(f"ID: {book["ID"]} | Title : {book["Title"]} | Author: {book["Author"]} | ISBN : {book["ISBN"]} | Price: {book["Price"]} | Quantity : {book["Quantity"]}")

    else:
        print("Empty! there is no book ")
def save_all_books(booklist):
    with open("list.csv", "w") as fp:
        for book in booklist:
            line = f"{book['ID']},{book['Title']}, {book['Author']}, {book['ISBN']}, {book['Year']}, {book['Price']}, {book['Quantity']}\n"
            fp.write(line)
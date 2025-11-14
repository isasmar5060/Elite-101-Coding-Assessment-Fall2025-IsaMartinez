from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author

print("Welcome to the online library!")
def view_books(library_books):
    for book in library_books:
        if book["available"] == True:
             print(book["title"] + " by " + book["author"] + ", ID numbered as: " + book["id"])

view_books(library_books)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def book_search(library_books):
    query = input("Please type the author or genre of a book you wish to search for: ").strip().lower()
    
    results = list(filter(
        lambda b: query in b["author"].lower() or query in b["genre"].lower(),
        library_books
    ))
    
    if results:
        for b in results:
            print(f"{b['title']} by {b['author']} ({b['genre']})")
    else:
        print("No results found.")
        
# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def book_checkout(library_books):
    book_name = input("Please enter the name of the book you want to check out: ").strip().lower()
    
    for book in library_books:
        if book_name == book["title"].lower():
            if book["available"]:
                book["available"] = False
                book["due_date"] = (datetime.now() + timedelta(days=14)).strftime("%Y-%m-%d")
                print(f"Congrats! '{book['title']}' has been checked out.")
                print(f"Due date: {book['due_date']}")
            else:
                print(f"Sorry, '{book['title']}' is already checked out until {book['due_date']}.")
            break
    else:
        print("This book is not found in the library, could you try again?")
        
book_checkout(library_books)


#case insensitive: "apple" = "APPle" = "APPLE" = "ApPle"
# for case insensitive, equate capital to lowercase
# 1: if author/genre matches true available, turn available status into false
# 2: when such, import current time & make timer for 2 weeks after current time
# 3: for book, add +1 to "checkouts"


# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass

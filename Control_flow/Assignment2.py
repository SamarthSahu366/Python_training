# program to :Create a program to implement a simple text-based menu system
# for a library that allows users to add, remove, search, and list
# books. Use loops and conditional statements effectively
def library_menu():
    library = []

    def add_book():
        book = input("enter the book title to add: ").strip()
        if book:
            if book not in library:
                library.append(book)
                print(f'"{book}" has been added to the library.')
            else:
                print(f'"{book}" is already in the library.')
        else:
            print("book title cannot be empty.")

    def remove_book():
        book = input("enter the book title to remove: ").strip()
        if book in library:
            library.remove(book)
            print(f'"{book}" has been removed from the library.')
        else:
            print(f'"{book}" is not in the library.')

    def search_book():
        book = input("enter the book title to search: ").strip()
        if book in library:
            print(f'"{book}" is available in the library.')
        else:
            print(f'"{book}" is not in the library.')

    def list_books():
        if library:
            print("\nbooks in the library:")
            for i, book in enumerate(library, start=1):
                print(f"{i}. {book}")
        else:
            print("The library is empty.")

    while True:
        print("\nLibrary Menu:")
        print("1. add a Book")
        print("2. remove a Book")
        print("3. search for a Book")
        print("4. List All Books")
        print("5. exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            add_book()
        elif choice == '2':
            remove_book()
        elif choice == '3':
            search_book()
        elif choice == '4':
            list_books()
        elif choice == '5':
            print("exiting the library system. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    library_menu()

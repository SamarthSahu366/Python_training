def library_catalog():
    catalog = {
        'To Kill a Mockingbird': {'author': 'Harper Lee', 'category': 'Fiction'},
        '1984': {'author': 'George Orwell', 'category': 'Dystopian'},
        'Python Programming': {'author': 'John Doe', 'category': 'Education'},
    }

    while True:
        print("\nLibrary Catalog:")
        print("1. search by Title")
        print("2. search by Author")
        print("3. search by Category")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        if choice == '1': 
            title = input("Enter book title: ")
            if title in catalog:
                print(f"Title: {title}, Author: {catalog[title]['author']}, Category: {catalog[title]['category']}")
            else:
                print("Book not found.")
        
        elif choice == '2':  
            author = input("Enter author name: ")
            found = False
            for title, info in catalog.items():
                if info['author'].lower() == author.lower():
                    print(f"Title: {title}, Author: {info['author']}, Category: {info['category']}")
                    found = True
            if not found:
                print("No books found by this author.")
        
        elif choice == '3':
            category = input("Enter category: ")
            found = False
            for title, info in catalog.items():
                if info['category'].lower() == category.lower():
                    print(f"Title: {title}, Author: {info['author']}, Category: {info['category']}")
                    found = True
            if not found:
                print("No books found in this category.")
        
        elif choice == '4':  # Exit
            break
        else:
            print("Invalid choice. Please try again.")

library_catalog()

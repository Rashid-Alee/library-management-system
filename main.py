# main.py

from library import Library


def print_menu():
    print("\n=== Library Management System ===")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display All Books")
    print("5. Register Member")
    print("6. Remove Member")
    print("7. Display All Members")
    print("8. Issue Book")
    print("9. Return Book")
    print("10. Quit")
    print("===============================")


def main():
    library = Library()

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            library.add_book(title, author)

        elif choice == "2":
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == "4":
            library.display_all_books()

        elif choice == "5":
            name = input("Enter member name: ")
            library.register_member(name)

        elif choice == "6":
            name = input("Enter member name to remove: ")
            library.remove_member(name)

        elif choice == "7":
            library.display_all_members()

        elif choice == "8":
            title = input("Enter book title to issue: ")
            member_name = input("Enter member name: ")
            library.issue_book(title, member_name)

        elif choice == "9":
            title = input("Enter book title to return: ")
            library.return_book(title)

        elif choice == "10":
            print("Exiting the Library Management System. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

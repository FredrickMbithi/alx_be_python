def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

shopping_list = []

def main():
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid choice. Please try again.")
            continue

        if choice == 1:
            # Prompt for and add an item
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f'"{item}" added to the shopping list.')
        elif choice == 2:
            # Prompt for and remove an item
            item = input("Enter the item to remove: ")
            try:
                shopping_list.remove(item)
                print(f'"{item}" removed from the shopping list.')
            except ValueError:
                print(f'"{item}" not found in the shopping list.')
        elif choice == 3:
            # Display the shopping list
            if shopping_list:
                print("Shopping List:")
                for idx, it in enumerate(shopping_list, 1):
                    print(f"{idx}. {it}")
            else:
                print("The shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

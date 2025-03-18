def display_list(lst):
    print("Current list:" if lst else "The list is currently empty.", lst)

def get_number(prompt):
    try: return float(input(prompt))
    except ValueError: print("Invalid input!")

def add_number(lst): lst.append(get_number("Add a number: "))

def remove_number(lst):
    num = get_number("Remove a number: ")
    print("Number removed." if num in lst and lst.remove(num) else "Not Found.")

def insert_number(lst):
    num, idx = get_number("Enter number: "), int(input("Enter index: "))
    lst.insert(idx, num) if 0 <= idx < len(lst) else print("Invalid index!")

def pop_number(lst):
    idx = int(input("Enter an index to pop: "))
    print(f"Popped: {lst.pop(idx)}") if 0 <= idx < len(lst) else print("Invalid Index!")

def calculate_stats(lst):
    print(f"Sum: {sum(lst)}, Avg: {sum(lst)/len(lst)}, Max: {max(lst)}" if lst else "Not found.")

def search_number(lst):
    num = get_number("Enter a number to search: ")
    print(f"Found at index {lst.index(num)}" if num in lst else "Not found.")

def remove_odds(lst):
    lst[:] = [num for num in lst if num % 2 == 0]
    print("Odd numbers removed.")

def main():
    lst, menu = [], [add_number, remove_number, insert_number, pop_number, calculate_stats, search_number, remove_odds]
    print("Welcome to the List Operations Program!")
    while True:
        print("\n" + "\n".join(f"{i+1}. {m.__name__.replace('_', ' '). title()}" for i, m in enumerate(menu)) + "\n8. Exit")
        choice = input("Enter choice: ")
        if choice == '8' : break
        if choice.isdigit() and 1 <= int(choice) <= 7: menu[int(choice)-1](lst)
        else: print("Invalid choice!")
        if input("Print list? (yes/no): ").strip().lower() == "yes":display_list(lst)
    print("Goodbye!")
if __name__ == "__main__":
    main()
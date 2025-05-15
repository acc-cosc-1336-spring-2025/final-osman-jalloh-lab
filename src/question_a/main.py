from question_a import stock_purchase_history 
def main():
    while True:
        print("\n1 - Display stock purchase history")
        print("2 - Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            stock_purchase_history()
        elif choice == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid input. Try again.")

if __name__ == "__main__":
    main()
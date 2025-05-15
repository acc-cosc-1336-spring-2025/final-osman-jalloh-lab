from multiplication import create_multiplication_table, display_multiplication_table 
def main():
    while True:
        table = create_multiplication_table()
        print("\nMultiplication Table:")
        display_multiplication_table(table)

        choice = input("\nDo you want to continue? (y/n): ")
        if choice.lower() != 'y':
            print("Exiting program. Goodbye!")
            break

if __name__ == "__main__":
    main()

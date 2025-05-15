from companies import get_stock_list, Stock

def create_stock_file(stocks, filename="stock_file.dat"):
    with open(filename, "w") as file: 
        for stock in stocks:
            file.write(f"{stock.get_symbol()} {stock.get_company_name()}\n")

def read_stock_file(filename="stock_file.dat"):
    stock_list = []
    try:
        with open(filename, "r") as file:
            for line in file:
                parts = line.strip().split(' ', 1)
                if len(parts) == 2:
                    symbol, company_name = parts
                    stock = Stock(symbol, company_name)
                    stock_list.append(stock)
    except FileNotFoundError:
        print("stock_file.dat not found.")
    return stock_list

def display_stock_list(stocks):
    print("\nStock Purchase History:")
    for stock in stocks:
        print(f"Symbol: {stock.get_symbol()}, Company: {stock.get_company_name()}")
    print()

def display_menu():
    print("\nMenu:")
    print("1 - Display stock purchase history")
    print("2 - Exit")

def main():
    # Create initial file
    stocks = get_stock_list()
    create_stock_file(stocks)

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Now read from the file so it always works
            stock_list = read_stock_file()
            if stock_list:
                display_stock_list(stock_list)
            else:
                print("No stock data found.")
        elif choice == '2':
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()



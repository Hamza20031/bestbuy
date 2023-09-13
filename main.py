import products
import store


def start(best_buy):
    while True:
        print("Welcome to Best Buy!")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose an option (1-4): ")

        if choice == "1":
            print("Listing all products:")
            best_buy.get_all_products()
        elif choice == "2":
            print(f"Total amount in store: {best_buy.get_total_quantity()}")
        elif choice == "3":
            print("Available products:")
            best_buy.get_all_products()
            product_name = input("Enter the name of the product you want to buy: ")
            quantity = int(input("Enter the quantity: "))

            selected_product = None  # Initialize variable

            # Loop to find the product
            for product in best_buy.products:
                if product.name == product_name:
                    selected_product = product
                    break

            if selected_product is None:
                print("Product not found!")
                continue  # Skip the rest of the loop

            try:  # Correct indentation for the try-except block
                total_price = float(selected_product.buy(quantity))
                print(f"Order successful! Total cost: {total_price}")  # Corrected from self.total_price
            except Exception as e:
                print(str(e))
        elif choice == "4":  # Correct indentation for the elif block
            print("Thank you for shopping with us. Goodbye!")
            break
        else:
            print("Invalid option, please choose again.")


def main():
    product_list = [products.Product("MacBook Air M2", price=1450, quantity=100),
                    products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
                    products.Product("Google Pixel 7", price=500, quantity=250)
                    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
def calculate_product(quantity, price):
    return quantity * price

def add_to_list(sales: list, sale):
    sales.append(sale)
    return sales

def record():
    continuee = "yes"
    sales = []
    general_total = 0

    while continuee == "yes":
        name = input ("enter product name: ")
        quantity = int(input("enter product quantity: "))
        price = int(input ("enter product price : "))

        subtotal = calculate_product(quantity, price)
        general_total += subtotal

        print(f"Subtotal {name}: ${subtotal}")

        sale = {
            "product name": name,
            "product quantity":quantity,
            "product price":price,
            "subtotal": subtotal
        }
    
        add_to_list(sales, sale)
        continuee = input("¿do you want to continue buying? yes/no ")

    for sale in sales:
        print("")
        print("DAILY SALES SUMMARY")
        print("")
        print("product name: ", sale["product name"])
        print("product quantity: ", sale["product quantity"])
        print("product price: $", sale["product price"])

    print(f"\ntotal purchase: ${general_total}")
    return sales, general_total
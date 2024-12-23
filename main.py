
def val_int(n):
    while True:
        try:
            a = int(input(n))
            if a:
                return a
        except ValueError:
            print("Invalid input, try again!")


def val_float(n):
    while True:
        try:
            a = float(input(n))
            if a:
                return a
        except ValueError:
            print("Invalid input, try again!")



number_of_installments = val_int("Number of installments: ")
full_purchase_cost = val_float("Insert float: ")
purchase_name = ((input("Purchase name: ")).lower()).strip()








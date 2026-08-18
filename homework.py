while True:
    try:
        bill = float(input("Enter shopping bill: "))
        discount = float(input("Enter discount %: "))
        final_amount = bill - (bill * discount / 100)
    except ValueError:
        print("Enter numbers only.")
    except TypeError:
        print("Calculation error.")
    else:
        print("Final amount:", final_amount)
        break
    finally:
        print("Attempt done.\n")

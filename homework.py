valid = False
while not valid:
    try:
        parts = input("Enter bill, discount, people (e.g., 1000,10,2): ").split(",")
        if len(parts) != 3:
            raise ValueError
        bill = float(parts[0])
        disc = float(parts[1])
        people = int(parts[2])
        if bill <= 0 or disc < 0 or people < 0:
            raise ValueError
        discount = bill * disc / 100
        final = bill - discount
        per_person = final / people
    except ValueError:
        print("Invalid input! Use format: 100")
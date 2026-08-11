bill = float(input("Bill: "))
discount = float(input("Discount %: "))
people = int(input("People: "))

discount_amount = bill * discount / 100
final_bill = bill - discount_amount
each = final_bill / people

print("Discount:", discount_amount)
print("Final bill:", final_bill)
print("Each person:", each)
"""Challenge question."""

dozens: int = 2
singles: int = 3
print("I have" + str(dozens) + " dozen eggs")
print("plus " + str(singles) + " single eggs.")
total_eggs: int = dozens * 12 + singles
print("I have " + str(total_eggs) + " eggs.")

age: int = int(input("What is your age?"))
if age <= 12:
    price: int = 5
    print(price)
elif age > 60:
    price: int = 5
    print(price)
else:
    price: int = 10
    print(price)
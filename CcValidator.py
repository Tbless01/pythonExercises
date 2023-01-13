creditCardNumber = input("Hello, kindly enter card detail to verify:  ")
if creditCardNumber.__getitem__(0) == "5":
    print()
    print("========================================")
    print('Credit Card Type: MasterCard')
elif creditCardNumber.__getitem__(0) == "4":
    print()
    print("========================================")
    print("Credit Card Type: Visa Card")
elif creditCardNumber.__getitem__(0) == "6":
    print()
    print("========================================")
    print("Credit Card Type: Discover cards")
elif creditCardNumber.__getitem__(0) == "3" or creditCardNumber.__getitem__(1) == "7":
    print()
    print("========================================")
    print("Credit Card Type: American Express Card")
else:
    print()
    print("========================================")
    print("Credit Card Type: Invalid Card")

creditCard = [int(u) for u in creditCardNumber]
print("Credit Card Number:", creditCardNumber)
print("Credit Card Digit Length:", len(creditCardNumber))
doubleSum = 0
sumTotalEven = 0
fromStart = 0
for i in range(0, len(creditCard), 2):
    doubleSum = (creditCard[i] * 2)
    if doubleSum > 9:
        doubleSum = (doubleSum // 10) + (doubleSum % 10)
    sumTotalEven += doubleSum
# print(sumTotalEven)
for i in range(0 + 1, len(creditCard) + 1, 2):
    fromStart += creditCard[i]
# print(fromStart)
sumOfBoth = sumTotalEven+fromStart
# print(sumOfBoth)
if sumOfBoth % 10 == 0:
    print("Credit Card Validity Status: Valid ")
else:
    print("Credit Card Validity Status: Invalid ")
# for j in range(creditCard):
print("========================================")

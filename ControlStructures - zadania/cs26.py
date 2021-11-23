PIN = 1111
for i in range (1,4):
    proba1 = int(input("Enter your PIN: "))
    if proba1 == PIN:
        print("Correct")
        break
    else:
        print("Incorrect...")
        print("Sorry, your payment card has been blocked.")

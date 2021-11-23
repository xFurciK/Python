PIN = 1111
attempt = 3
while attempt > 0:
    proba = int(input("Enter your PIN: "))
    if proba == PIN:
        print("Correct")
        break
    else:
        print("Incorrect")
        attempt -= 1
if attempt == 0:
    print("Blocked")
    
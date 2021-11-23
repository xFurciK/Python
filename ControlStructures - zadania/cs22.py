for num in range (1,31):
    if num%3==0 and num%5==0:
        print("BINGO")
    elif num%5==0:
        print("FIVE")
    elif num%3==0:
        print("THREE")
    else:
        print(num)
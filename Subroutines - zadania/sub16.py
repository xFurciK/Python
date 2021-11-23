def month(n):
    if n >= 1 and n <=12:
        if n == 1:
            print("Styczen")
        elif n == 2:
            print("Luty")
        elif n==3:
            print("Marzec")
        elif n==4:
            print("Kwiecien")
        elif n==5:
            print("Maj")
        elif n==6:
            print("Czerwiec")
        elif n==7:
            print("Lipiec")
        elif n==8:
            print("Sierpien")
        elif n==9:
            print("Wrzesien")
        elif n==10:
            print("Pazdziernik")
        elif n==11:
            print("Listopad")
        elif n==12:
            print("Grudzien")
    else:
        print("Zla liczba!")
        
n = int(input("Enter month number: "))
month(n)
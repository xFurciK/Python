print("Zagrajmy. Zgadnij liczbę od 1 do 6")
import random
dice = random.randint(1,6)
user = int(input(f"Prosze wskazac cyfre od 1 do 6 : "))
if dice == user:
    print("Brawo! Udalo ci sie zgadnac!")
else:
    print(f"Niestety, tym razem sie nie udalo, szukana cyfra to {dice} ")
    
import random

def zobacz_pomoc(liczba_podana,liczba_wytypowana):
    if liczba_podana > liczba_wytypowana:
        return print("Liczba jest za duża!")
    elif liczba_podana < liczba_wytypowana:
        return print("Liczba jest za mała!")

liczba_max = 100
liczba_wytypowana = int(random.randint(0,liczba_max))
while True:
    liczba_podana = int(input("Zgadnij liczbę wymyśloną przez komputer w zakresie od 0 do {} : ".format(liczba_max)))
    if liczba_podana != liczba_wytypowana:
        zobacz_pomoc(liczba_podana,liczba_wytypowana)
        continue
    else:
        print("Gratulacje, zgadłeś!")
        break

import random

def zobacz_pomoc(liczba_podana,liczba_wytypowana):
    if liczba_podana > liczba_wytypowana:
        return print("Liczba jest za duża!")
    elif liczba_podana < liczba_wytypowana:
        return print("Liczba jest za mała!")

liczba_podana = 0
liczba_max = 100
liczba_wytypowana = int(random.randint(0,liczba_max))
while liczba_podana != liczba_wytypowana:
    zobacz_pomoc(liczba_podana,liczba_wytypowana)
    liczba_podana = int(input("Zgadnij liczbę wymyśloną przez komputer w zakresie od 0 do {} : ".format(liczba_max)))

print("Gratulacje, zgadłeś!")

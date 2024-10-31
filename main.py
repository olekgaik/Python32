print("Program do obsługi ładowarki paczek\n" + "*"*40)

POJEMNOSC_PACZKI = 20
liczba_towarow = int(input("Podaj liczbę towarów do wysyłki: "))
laczna_waga = 0
liczba_paczek = 1

pojemnosc_biezacej_paczki = POJEMNOSC_PACZKI

for towary in range(liczba_towarow):
    waga_produktu = int(input(f"Podaj wagę {towary + 1}. towaru: "))
    laczna_waga += waga_produktu
    if pojemnosc_biezacej_paczki - waga_produktu < 0:
        pojemnosc_biezacej_paczki = POJEMNOSC_PACZKI - waga_produktu
        liczba_paczek += 1
    else:
        pojemnosc_biezacej_paczki -= waga_produktu

print(f"\nŁączna ilość wysłanych towarów: {liczba_towarow}")
print(f"Łączna waga wysłanych towarów: {laczna_waga}")
print(f"Liczba wysłanych paczek: {liczba_paczek}")
print(f"Suma niewykorzystanego miejsca w paczkach w kilogramach: {liczba_paczek*20-laczna_waga}")
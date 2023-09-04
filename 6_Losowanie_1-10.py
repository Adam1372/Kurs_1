"""
PyCharm-Kurs1    <-- katalog projektu.
Ctrl+Shift+F10     <-- wybieram plik do edycji

Tylko na typie intiger (int) działają wszystkie operatory porównania (< , >).

 Gra - Komp losuje liczbę ( 1 - 10 ) i zgadywanie jej.
"""

from random import randint  # dołączanie biblioteki

los = randint(1,10)  #  losowanie od 1 do 10
odp = -1
i = 0    # ilość prób grającego
# robić wcięcia 4 spacje.
while odp != los:
    i += 1  # dodajemy od razu 1, aby to było pierwsze losowanie.
    odp  = int(input (" Podaj liczbę: ")) # zamienia liczbę na typ int.
    if odp> los:
        print("Niestety, wylosowana liczba jest mniejsza od twojej")
    elif odp < los:
        print("Niestety, wylosowana liczba jest większa od twojej")
print("Brawo! Odgadłeś za " , i, "razem")  # połączy stringi

# ( Alt+Shift+F10 ) otwiera listę plików projektu.
# Z lewej strony kliknąć PKM na nazwe projektu  (PyCharm-Kurs1 ) i wybrać New
# Nadać nazwę nowemu plikowi i kliknąć Enter.
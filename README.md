# domek
Zadanie na potrzeby zajęć z programowania I

## Główne cele
- ćwiczenie wykorzystania pętli, instrukcji warunkowych, funkcji,
- pobieranie danych ze standardowego wejścia, wyprowadzanie na standardowe wyjście,
- odczytywanie i zapisywanie w plikach tekstowych.


Uwaga: zadanie zostało pożyczone z OIJ, czyli Olimpiady Informatycznej Juniorów (https://oij.edu.pl/zbior_zadan/etap1/).

[Treść zadania (PDF)](https://github.com/oleklamza/domek/tree/main/domzad.pdf) 

## Etapy realizacji
Program powstaje etapami. Każdy etap ma swoją odrębną gałąź.

[etap-1](https://github.com/oleklamza/domek/tree/etap-1)
Testowo wyświetlamy dane pobierane ze standardowego wejścia. Musimy zastosować przekierowanie z pliku: `python3 dom.py < dom0a.in`
(W Windowsie w Powershellu analogiczne polecenie wygląda tak:
`Get-Content dom0a.in | python3 dom.py`).

[etap-2](https://github.com/oleklamza/domek/tree/etap-2)
Zgodnie z opisem zadania: odczytujemy z pierwszego wiersza wartości N i M (liczby wierszy i kolumn obrazka). Następnie czytamy w pętli N wierszy (nie ma potrzeby obsługiwania wyjścia poza plik: `EOFError` z pierwszego etapu).

Dodatkowo dla zainteresowanych: prosty przykład wykorzystania _list comprehension_, _generator expression_ i _map_.

[etap-3](https://github.com/oleklamza/domek/tree/etap-3)
Przekształcamy obrazek odczytany z wejścia (pliku tekstowego) na postać
wewnętrzną wygodną do przetwarzania: tablicę dwuwymiarową (a raczej, w przypadku
Pythona, listę dwuwymiarową, czyli listę list).
Od razu piszemy kod przekształcający postać wewnętrzną z powrotem na obrazek. 

[etap-4](https://github.com/oleklamza/domek/tree/etap-4)
Implementujemy najprostszy i daleki od optymalnego algorytm opadania śnieżynek.

[etap-5](https://github.com/oleklamza/domek/tree/etap-5)
Staramy się zoptymalizować kod przekształcający obrazek.

[etap-dodatkowy](https://github.com/oleklamza/domek/tree/etap-dodatkowy)
Inny algorytm. Udało się ograniczyć do dwóch zagnieżdżonych pętli, co zdecydowanie pozytywnie wpływa na czas wykonania. 
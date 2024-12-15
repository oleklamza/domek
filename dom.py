# Pomiar czasu (więcej informacji poniżej, w opisie algorytmu)
from time import time
t0 = time()


# Odczytujemy pierwszy wiersz wejścia: wartości N i M
line = input()
n, m = map(int, line.split())


# Zamieniamy obrazek na postać wewnętrzną
rows = []
for i in range(n):
	line = input()
	rows.append(list(line))

"""
Opadanie śnieżynek -- nowy algorytm

W poprzednim etapie omówiliśmy optymalizacje zaproponowanego na początku
algorytmu, w którego centrum znajdowała się pętla wyznaczająca położenie
śnieżynek jak w animacji "klatka po klatce". Z tego względu cały proces,
dla każdej kolumny obrazka oddzielnie, musi być powtarzany wiele razy
(maksymalnie N-1). Zbudowaliśmy więc algorytm o złożoności obliczeniowej
sześciennej O(n^3), czego efektem są stosunkowo długie i -- tak naprawdę --
nieakceptowalne czasy wykonywania: dla testowego obrazka dom10c.in jest
to ok. 80 sekund bez optymalizacji i ok. 20 sekund po optymalizacji.
Więcej z tego algorytmu wydusić się nie da.

Wróćmy zatem na początek i przemyślmy to jeszcze raz.

Na pewno zostaniemy przy założeniu, że przetwarzamy każdą kolumnę osobno.
Wynika to z budowy danych i zasad przedstawionych w zadaniu. Skupiamy się
więc na gwiazdkach-śnieżynkach w kolumnie. Poprzednio szliśmy od dołu, żeby
"robić miejsce" dla opadających śnieżynek. A może jednak spróbowalibyśmy
iść od góry? Widzę to tak: czytam pole i -- jeżeli jest to gwiazdka --
chowam ją do kieszeni (zwiększam "licznik śnieżynek"), a następnie czyszczę
pole (wstawiam kropkę). Schodzę piętro niżej i działam tak samo.
Kluczowe jest tu natrafienie na #. Jeżeli do tego dojdzie (a kiedyś musi),
wyciągam z kieszeni wszystkie zebrane śnieżynki i układam je jedna nad drugą,
tworząc stos o wysokości wynikającej z licznika śnieżynek.
W ten sposób przetwarzam kolumnę, aż znajdę się na dole (z zadania wiem, że
w ostatnim wierszu na pewno jest #). Wszystkie śnieżynki są już na swoich
docelowych miejscach, nie ma potrzeby ponawiania procesu (jak było w poprzednim
rozwiązaniu). To samo powtarzam dla każdej kolumny i gotowe!
"""

for c in range(m):
	sf_cnt = 0
	for r in range(n):
		if rows[r][c] == '*':
			rows[r][c] = '.'
			sf_cnt += 1
		elif rows[r][c] == '#':
			for i in range(sf_cnt):
				rows[r-i-1][c] = '*'
			sf_cnt = 0

"""
Wygląda to całkiem zgrabnie. Zwróćcie uwagę na pętle: są dwie główne. Pierwsza
idzie po kolumnach, druga po wierszach. Jej wnętrze zostanie wykonane N*M razy,
czyli mamy złożoność kwadratową. Do tego dochodzi pętla ustawiająca stosik
zebranych śnieżynek.
Jakie wyniki?
Skupimy się na czasie przetwarzania dwóch plików:
- dom0a.in: ok. 0.3 milisekundy
- dom10c.in: ok. 0.2 sekundy
Uzyskujemy wyniki ok. 100 razy lepsze niż w zoptymalizowanej wersji poprzedniego
algorytmu!

Czas na wnioski.
Naprawdę dużo zależy od algorytmu. Warto poświęcić chwilę na przemyślenie
sprawy, kilkukrotne przeczytanie "na nowo" wytycznych, tak żeby nie skupić
się na jednym rozwiązaniu, ale móc wybierać z kilku.
Cenne jest myślenie o optymalizacji implementowanych algorytmów, ale trzeba
mieć cały czas w głowie słowa Donalda Knutha o przedwczesnej optymalizacji.
"""


# Składamy dane z powrotem do postaci obrazka i wyświetlamy
for i in range(n):
	line = ''.join(rows[i]) 
	print(line)


# Wyświetlenie czasu realizacji zadania
print(time() - t0)
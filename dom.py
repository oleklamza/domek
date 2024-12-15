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
Opadanie śnieżynek -- optymalizacje
Na potrzeby sprawdzania optymalizacji wprowadziłem roboczo zmienną cnt
zliczającą wykonania wewnętrznej pętli.
Przykładowe wyniki dla podstawowej wersji kodu:
- dla pliku dom0a.in jest to 10830,
- dla pliku dom10c.in jest to 997002999. 
"""
cnt = 0

"""
Jak korzystać z tego opracowania?
Wydzieliłem trzy sekcje z omówieniem kolejnych optymalizacji oraz ich
analizą. Proponuję zapoznać się z nimi po kolei.
Aby aktywować daną optymalizację, przypiszcie jej numer do poniższej
zmiennej `OPTI`:
"""
OPTI = 1

"""
# Optymalizacja 1

Pierwsza optymalizacja polega na (potencjalnym) zmniejszeniu liczby
iteracji zewnętrznej pętli. Nie wykonujemy jej n-1 razy, ale do momentu,
kiedy jest to potrzebne. Skąd wiedzieć kiedy przestać? Wtedy, kiedy nie ma
już nic do zmiany. Przyda nam się do tego zmienna logiczna `changed`.
Zoptymalizowany kod znajdziecie poniżej.

Efekty? Dla wspomnianych powyżej plików uzyskujemy wyniki:
- dom0a.in -> cnt = 10260 (różnica 570, co stanowi ~5% mniej iteracji)
- dom10c.in -> cnt = 987022989 (różnica 9980010, czyli ~1% mniej...)

Choć wydawało się, że to dobry pomysł, optymalizacja nie przyniosła 
wymiernych korzyści.
"""
if OPTI == 1:
	...
	while True:
		changed = False
		for c in range(m):
			for r in range(n-2, -1, -1):
				cnt += 1
				if rows[r][c] == '*' and rows[r+1][c] == '.':
					rows[r+1][c] = '*'
					rows[r][c] = '.'
					changed = True

		if not changed:
			break
	...

"""
Ale chwila... Idea jest przecież słuszna -- przerywamy, kiedy śnieżynki dolecą
na dół. Problem w tym, że w powyższej implementacji **globalnie** ustalamy
konieczność powtórzenia, a w algorytmie każda kolumna jest rozpatrywana
niezależnie od innych. Czas na kolejną optymalizację...

# Optymalizacja 2

Wprowadźmy modyfikację, w której konieczność powtórzenia ustalamy na poziomie
pojedynczej kolumny (kod poniżej).
Jakie wyniki? Względem wersji podstawowej mamy:
- dom0a.in -> cnt = 3021, czyli 72% mniej iteracji,
- dom10c.in -> cnt = 305761932, czyli 69% mniej!
To już coś! 
"""
if OPTI == 2:
	...
	for c in range(m):
		while True:
			changed = False
			for r in range(n-2, -1, -1):
				cnt += 1
				if rows[r][c] == '*' and rows[r+1][c] == '.':
					rows[r+1][c] = '*'
					rows[r][c] = '.'
					changed = True

			if not changed:
				break
	...

"""
Co jeszcze można by tu przyspieszyć?
Jeszcze raz wróćmy do początku: naszym zadaniem jest doprowadzenie śnieżynek
na dół. Czyli lecą od góry do dołu. Z kolei my, w kodzie, każdą kolumnę
przetwarzamy, idąc od dołu do góry. Wniosek: wiemy, gdzie (na jakiej wysokości)
pojawiła się ostatnia (najwyżej położona) śnieżynka. Powinniśmy więc zatrzymać
"marsz ku górze" na tej właśnie pozycji, a nie niepotrzebnie iść dalej.

# Optymalizacja 3

Wprowadzamy zmienną `r_top`, która będzie przechowywała numer wiersza, w którym
doszło do ostatniej zmiany. W kolejnym powtórzeniu pętli `for r` dojdziemy
tylko do tej wartości. Kod znajdziecie poniżej, a teraz wyniki (względem
wersji podstawowej):
- dom0a.in -> cnt = 1830 zamiast 10830 (Popatrzcie na podobieństwo liczb.
  To znak! ;), czyli 83% mniej,
- dom10c.in -> cnt = 305761932 zamiast 997002999, czyli 84% mniej iteracji!
"""
if OPTI == 3:
	...
	for c in range(m):
		r_top = -1
		while True:
			changed = False
			for r in range(n-2, r_top, -1):
				cnt += 1
				if rows[r][c] == '*' and rows[r+1][c] == '.':
					rows[r+1][c] = '*'
					rows[r][c] = '.'
					changed = True
					r_top = r
			
			if not changed:
				break
	...

"""
Na koniec warto wspomnieć o jednej, **bardzo** istotnej sprawie.
Optymalizacje, które tu przedstawiłem, były efektem typowej pracy nad kodem.
Zwykle działamy tak: piszemy kod, który "jakoś tam" działa. Później staramy
się go ulepszyć. Testujemy, sprawdzamy, jak sobie radzi w różnych sytuacjach,
jak reaguje na zwiększenie rozmiaru danych wejściowych itp.
Warto jednak pamiętać o istotnej myśli, którą wyraził Donald Knuth:

"Premature optimization is the root of all evil".

Na potrzeby tych rozważań uprośćmy sprawę do stwierdzenia:

"Jeżeli nie musimy, nie optymalizujmy".

(Zachęcam do poszukania głębiej. Dobry punkt startowy:
https://wiki.c2.com/?PrematureOptimization)

Czy tu musieliśmy? W opisie zadania z zawodów OIJ możemy przeczytać, że
limit czasu na wykonanie tego programu to 2 sekundy przy maksymalnym rozmiarze
obrazka 1000x1000. W pierwszej implementacji mieliśmy ok. 80 sekund, a po
optymalizacjach udało się uzyskać wynik ok. 20 sekund.
Jest lepiej i -- moim zdaniem -- było warto, ale to wciąż za słabo.

Zainteresowanych rozwiązaniem tego problemu zachęcam do zajrzenia do ostatniego
etapu, który znajduje się w gałęzi _etap-dodatkowy_.
"""

# Składamy dane z powrotem do postaci obrazka i wyświetlamy
for i in range(n):
	line = ''.join(rows[i]) 
	print(line)


# Wyświetlenie czasu realizacji zadania i liczby wykonań instrukcji if
print(time() - t0)
print(cnt)
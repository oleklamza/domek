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


# Opadanie śnieżynek
# Kod najlepiej analizować od wewnątrz na zewnątrz, czyli od pętli (A) do (C)

# (C) chcemy, żeby wszystkie gwiazdki spadły najniżej jak się da;
# zakładamy skrajny przypadek, w którym gwiazdka leci z samej góry na sam dół;
# z tego wynika konieczność powtórzenia całego procesu n-1 razy 
for i in range(n-1):
	# (B) iterujemy po kolumnach (c jak column)
	for c in range(m):
		# (A) iterujemy po wierszach (r jak row);
		# interesuje nas tak naprawdę pojedynczy znak w bieżącej kolumnie
		# uwaga: idziemy od dołu!
		for r in range(n-2, -1, -1):
			# jeśli bieżący znak to gwiazdka
			# oraz pod spodem jest kropka (wolne miejsce)...
			if rows[r][c] == '*' and rows[r+1][c] == '.':
				# ...przenosimy gwiazdkę w dół
				rows[r+1][c] = '*'
				rows[r][c] = '.'

# Chwila na rozważania
# Powyżej mamy trzy pętle umieszczone jedna w drugiej. W takiej sytuacji mówi się
# o zagnieżdżaniu pętli. W tego typu konstrukcjach czai się niebezpieczeństwo:
# wewnętrzny kod (w naszym przypadku instrukcja if) wykonuje się całkiem
# sporo razy...
# Przyjmijmy, że mamy obrazek 1000x1000 znaków. Sprawdźmy, ile razy wykona się
# wewnętrzna instrukcja if (n-1 i n-2 zaokrąglam do 1000). Policzmy:
# 1000 wierszy (A) * 1000 kolumn (B) * 1000 powtórzeń (C)
# daje 1 000 000 000 (miliard) powtórzeń instrukcji if!!!
# Python nie jest zbyt szybkim językiem, więc w praktyce wykonanie tego programu
# na takich danych potrwa dobrych kilkadziesiąt sekund.
# (Pomiar czasu realizuję za pomocą funkcji time() z modułu time; zwróćcie uwagę
# na linie kodu: 1-3, a następnie 63-64).
# Sami sprawdźcie, jak długo będziecie czekać na wynik dla pliku dom10c.in
# z folderu dom_testy (w repozytorium umieściłem wszystkie przykładowe pliki
# zamieszczone na stronie OIJ).
# W kolejnym etapie zajmiemy się optymalizacją dotychczasowego rozwiązania.


# Składamy dane z powrotem do postaci obrazka i wyświetlamy
for i in range(n):
	line = ''.join(rows[i]) 
	print(line)


# Wyświetlenie czasu realizacji zadania
print(time() - t0)
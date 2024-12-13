# Odczytujemy pierwszy wiersz wejścia: wartości N i M
line = input()
n, m = map(int, line.split())


# Iterujemy n razy; w każdej iteracji czytamy z wejścia jeden wiersz
# i dodajemy go do listy wierszy (rows)
rows = []
for i in range(n):
	line = input() # czytamy z wejścia pojedynczy wiersz
	line_as_list = list(line) # rozbijamy wiersz na listę pojedynczych znaków
	rows.append(line_as_list) # dołączamy do listy wierszy

## Oczywiście powyższą pętlę można zapisać zwięźlej:
# rows = []
# for i in range(n):
# 	line = input()
# 	rows.append(list(line))

## Albo nawet tak:
# rows = []
# for i in range(n):
# 	rows.append(list(input()))

## Uwaga: przy wyborze stopnia skumulowania kodu zawsze bierzcie pod uwagę
## jego czytelność. Ostatnia postać omawianej pętli jest przykładem pójścia
## o jeden krok za daleko, z kolei pierwsza postać jest raczej zbyt rozwlekła.


## Sprawdźcie, jak wyglądają dane (obrazek) w przetworzonej postaci,
## czyli listy list: [ [...], [...], ...]
# print(rows)


# Przetwarzanie (opadaniem śnieżynek zajmiemy się w kolejnym etapie)
...


# Składamy dane z powrotem do postaci obrazka i wyświetlamy
for i in range(n):
	# join() łączy elementy z listy rows[i] w jeden łańcuch znaków
	line = ''.join(rows[i]) 
	print(line)
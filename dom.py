# >>> odczytujemy pierwszy wiersz wejścia: wartości N i M
line = input()

nm = line.split() # dzielimy na spacji (i innych białych znakach) 
n = int(nm[0])    # zamieniamy z tekstu (stringa) na liczby całkowite
m = int(nm[1])    # ...

## to samo ^^^ można zrobić za pomocą tzw. list comprehension
## (https://peps.python.org/pep-0202/, https://realpython.com/list-comprehension-python/)
# n, m = [int(x) for x in line.split()]

## albo generator expression (https://peps.python.org/pep-0289/,
## https://realpython.com/introduction-to-python-generators/):
# n, m = (int(x) for x in line.split())

## albo mapowania (np.: https://realpython.com/python-map-function/):
# n, m = map(int, line.split())


# >>> iterujemy n razy; w każdej iteracji czytamy z wejścia i wyświetlamy
i = 0
while i < n:
	line = input()
	print(line)
	# print(i, line) # możemy też wyświetlić sobie numer linii
	i += 1

## to samo ^^^ można zapisać zgrabniej za pomocą instrukcji for
# for i in range(n):
# 	line = input()
# 	print(line)

## w sytuacjach, gdy w kodzie pętli for nie wykorzystujemy zmiennej licznika,
## można nadać jej nazwę _ (znak podłogi), czyli: for _ in range...
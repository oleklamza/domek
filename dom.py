# pierwsza, robocza wersja kodu
# tylko na potrzeby wstępnych testów
while (True):
	try:
		# czytamy wiersz ze standardowego wejścia
		line = input()
		# piszemy na standardowe wyjście
		print(line)
	except EOFError:
		break
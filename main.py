#!/usr/bin/env	python3

import sys

def header(linha):
	if linha.find("#") == 0:
		print(f"\033[31m{linha}\033[0m", end= "")
		return True
	return False
		
def bold(linha):
	not_bold = 0
	bold_start = linha.find("**")
	bold_end = linha.find("**", bold_start+2)
	next_bold = linha.find("**", bold_end+2)
	if bold_start == -1 or bold_end == -1:
		return False
	while True:
		print(linha[not_bold:bold_start], end="")
		print("\033[1m" + linha[bold_start:bold_end+2] + "\033[0m", end="")
		if next_bold == -1:
			print(linha[bold_end+2:], end="")
			break
		not_bold = bold_end+2
		bold_start = next_bold
		bold_end = linha.find("**", bold_start+2)
		next_bold = linha.find("**", bold_end+2)
	return True

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()

arquivo = open(sys.argv[1], "r")

linhas = arquivo.readlines()
for linha in linhas:
	if not header(linha) and not bold(linha):
		print(linha, end= "")

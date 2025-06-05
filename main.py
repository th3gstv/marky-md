#!/usr/bin/env	python3

import sys

def header(linha):
	if linha.find("#") == 0:
		print(f"\033[31m{linha}\033[0m", end= "")
		return True
	return False
		
def bold(linha):
	if linha.find("**") == -1:
		return False
	sections = linha.split("**")
	sections_len = len(sections)
	for i in range(0, sections_len, 2):
		print(sections[i], end="")
		if i+1 < sections_len:
			print("\033[1m" + sections[i+1] + "\033[0m", end="")
	return True

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()

arquivo = open(sys.argv[1], "r")

linhas = arquivo.readlines()
for linha in linhas:
	if not header(linha) and not bold(linha):
		print(linha, end= "")

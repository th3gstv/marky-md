#!/usr/bin/env	python3

import sys

def header(linha):
    if linha.find("#") == 0:
        linha = "\033[31m" + linha + "\033[0m" 
    return linha	


def bold(linha):
    if linha.find("**") == -1:
        return linha
    sections = linha.split("**")
    linha = ""
    for i in range(0, len(sections), 2):
        linha += sections[i]
        if i+1 < len(sections):
            linha += "\033[1m" + sections[i+1] + "\033[0m"
    return linha

def italic(linha):
    if linha.find("_") == -1:
        return linha
    sections = linha.split("_")
    linha = ""
    for i in range(0, len(sections), 2):
        linha += sections[i]
        if i+1 < len(sections):
            linha += "\033[3m" + sections[i+1] + "\033[0m"
    return linha

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()

sys.argv.pop(0)
for filename in sys.argv:
    arquivo = open(filename, "r")
    linhas = arquivo.readlines()
    arquivo.close()
    for linha in linhas:
        linha = header(linha)
        linha = bold(linha)
        linha = italic(linha)
        print(linha, end= "")
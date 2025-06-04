import sys
from re import search

print(sys.argv)
##arquivo = open("nome do arquivo", "modo")
## modos -> "r" (read) |
    ##arquivo = open("README.md", "r")
    ##linhas = arquivo.readlines()
    ##print(linhas)
if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()

arquivo = open(sys.argv[1], "r")

linhas = arquivo.readlines()
for item in linhas:
    if item.find("#") == 0:
        print(f"\033[31m{item}\033[0m")

    else:
        print(item, end= " ")
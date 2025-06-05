#!/usr/bin/env	python3

import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} FILENAME")
    exit()

arquivo = open(sys.argv[1], "r")

linhas = arquivo.readlines()
for item in linhas:
    if item.find("#") == 0:
        print(f"\033[31m{item}\033[0m", end= "")
    else:
        print(item, end= "")

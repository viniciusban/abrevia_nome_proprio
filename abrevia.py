#!/usr/bin/env python

def abrevia_nome(nome):
    nomes = []
    partes = nome.split()
    ultimo = partes[-1]
    del partes[-1]
    for p in partes:
        nomes.append(p[0])
    return "%s, %s." % (ultimo, ". ".join(nomes))

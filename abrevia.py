#!/usr/bin/env python

def abrevia_nome(nome):
    partes = nome.split()
    return "%s, %s." % (partes[-1], partes[0][0])

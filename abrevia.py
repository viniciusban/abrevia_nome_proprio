#!/usr/bin/env python


def abrevia_nome(nome):
    def _abrevia(a):
        return ["%s." % s[0] for s in a]

    nomes = []
    partes = nome.split()
    if len(partes) == 1:
        return partes[0]

    partes_abreviadas = _abrevia(partes[0:-1])
    return "%s, %s" % (partes[-1], ' '.join(partes_abreviadas))

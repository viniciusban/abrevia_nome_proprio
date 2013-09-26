#!/usr/bin/env python


def abrevia_geral(nome):
    def _abrevia(a):
        return ["%s." % s[0] for s in a]

    nomes = []
    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return partes[0]

    partes_abreviadas = _abrevia(partes[0:-1])
    return "%s, %s" % (partes[-1],
            ' '.join(partes_abreviadas))

def abrevia_descendente(nome):
    def _abrevia(a):
        return ["%s." % s[0] for s in a]

    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return partes[0]

    nomes = []

    if not partes[-1] in "filha filho junior neta neto":
        return None

    if len(partes) > 2:
        # conserva o penultimo nome.
        i_final_para_abreviar = -2
        i_inicial_para_nao_abreviar = -2
    else:
        i_final_para_abreviar = -1
        i_inicial_para_nao_abreviar = -1

    partes_abreviadas = _abrevia(partes[0:i_final_para_abreviar])
    return "%s, %s" % (
            ' '.join(partes[i_inicial_para_nao_abreviar:]),
            ' '.join(partes_abreviadas))

#!/usr/bin/env python


def _abrevia_partes(a, primeira=None):
    """
    primeira = False -> nao abrevia a 1a parte.
    """

    if not primeira:
        primeira = True if primeira is None else False

    if primeira:
        return ["%s." % s[0] for s in a]
    else:
        # nao abrevia o 1o nome
        return a[:1] + ["%s." % s[0] for s in a[1:]]


def abrevia_geral(nome, primeiro_nome=None):
    """
    primeiro_nome = False -> nao abrevia o 1o nome.
    """

    if not primeiro_nome:
        primeiro_nome = True if primeiro_nome is None else False

    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return nome

    partes_abreviadas = _abrevia_partes(partes[:-1],
                                        primeira=primeiro_nome)
    return "%s, %s" % (partes[-1],
                       ' '.join(partes_abreviadas))


def abrevia_descendente(nome, elimina_descendencia=None, primeiro_nome=None):
    """
    primeiro_nome = False -> nao abrevia o 1o nome.
    """

    if not primeiro_nome:
        primeiro_nome = True if primeiro_nome is None else False

    partes = nome.split()
    if elimina_descendencia:
        quant_minima_de_nomes = 2
        i_a_desconsiderar = -1
    else:
        quant_minima_de_nomes = 1
        i_a_desconsiderar = None

    if len(partes) <= quant_minima_de_nomes:
        # nao abrevia se tem poucos nomes
        return nome

    if not partes[-1] in "filha filho junior neta neto":
        return nome

    if len(partes) > 2:
        # nao abrevia o penultimo nome.
        i_final_para_abreviar = -2
        i_inicial_para_nao_abreviar = -2
    else:
        i_final_para_abreviar = -1
        i_inicial_para_nao_abreviar = -1

    partes_abreviadas = _abrevia_partes(partes[0:i_final_para_abreviar],
                                        primeira=primeiro_nome)
    return "%s, %s" % (
        ' '.join(partes[i_inicial_para_nao_abreviar:i_a_desconsiderar]),
        ' '.join(partes_abreviadas))

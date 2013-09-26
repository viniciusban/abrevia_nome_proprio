#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _abrevia_partes(a, abrevia_primeira_palavra=None, retira_conectores=None):
    """
    abrevia_primeira_palavra = False -> nao abrevia a 1a parte.
    retira_conectores = True -> retira "da", "dos", "de", etc.
    """

    if not abrevia_primeira_palavra:
        abrevia_primeira_palavra = True if abrevia_primeira_palavra is None else False
    if not retira_conectores:
        retira_conectores = True if retira_conectores is None else False

    # so abrevia palavras com +2 letras.
    b = [p[0]+"." if len(p) > 2 else p for p in a]

    if not abrevia_primeira_palavra:
        b[0] = a[0]

    return b


def abrevia_geral(nome, primeiro_nome=None, retira_conectores=None):
    """
    primeiro_nome = False -> nao abrevia o 1o nome.
    retira_conectores = True -> retira "da", "dos", "de", etc.
    """

    if not primeiro_nome:
        primeiro_nome = True if primeiro_nome is None else False
    if not retira_conectores:
        retira_conectores = True if retira_conectores is None else False

    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return nome

    partes_abreviadas = _abrevia_partes(partes[:-1],
                                        abrevia_primeira_palavra=primeiro_nome,
                                        retira_conectores=retira_conectores)
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
                                        abrevia_primeira_palavra=primeiro_nome)
    return "%s, %s" % (
        ' '.join(partes[i_inicial_para_nao_abreviar:i_a_desconsiderar]),
        ' '.join(partes_abreviadas))

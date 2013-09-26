#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _abrevia_partes(a, abrevia_primeira_palavra=None, retira_conectores=None,
                    abrevia_maria=None, abrevia_depois_de_maria=None):
    """
    abrevia_maria default == False
    abrevia_primeira_palavra default == True.
    retira_conectores default == True -> retira "da", "dos", "de", etc.
    """

    if abrevia_maria is None:
        abrevia_maria = False
    if abrevia_depois_de_maria is None:
        abrevia_depois_de_maria = True
    if abrevia_primeira_palavra is None:
        abrevia_primeira_palavra = True
    if retira_conectores is None:
        retira_conectores = True

    b = a[:]

    if retira_conectores:
        conectores = "da de do das dos".split()
        b = [p for p in b if p not in conectores]

    depois_de_maria = None
    if not abrevia_depois_de_maria and b[0].lower() == "maria":
        depois_de_maria = b[1]

    # so abrevia palavras com +2 letras.
    b = [p[0] + "." if len(p) > 2 else p for p in b]

    if depois_de_maria:
        b[1] = depois_de_maria

    if abrevia_primeira_palavra:
        if abrevia_maria and a[0].lower() == "maria":
            b[0] = a[0][0] + "ª"
    else:
        b[0] = a[0]

    return b


def abrevia_geral(nome, abrevia_primeiro_nome=None, retira_conectores=None,
                  abrevia_maria=None, abrevia_depois_de_maria=None):
    """
    abrevia_maria = True -> abrevia o nome Maria.
    abrevia_primeiro_nome = False -> nao abrevia o 1o nome.
    retira_conectores = True -> retira "da", "dos", "de", etc.
    """

    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return nome

    partes_abreviadas = _abrevia_partes(partes[:-1],
                                        abrevia_primeira_palavra=abrevia_primeiro_nome,
                                        retira_conectores=retira_conectores,
                                        abrevia_maria=abrevia_maria,
                                        abrevia_depois_de_maria=abrevia_depois_de_maria)
    return "%s, %s" % (partes[-1],
                       ' '.join(partes_abreviadas))


def abrevia_descendente(nome, elimina_descendencia=None, abrevia_primeiro_nome=None):
    """
    abrevia_primeiro_nome = False -> nao abrevia o 1o nome.
    """

    if not abrevia_primeiro_nome:
        abrevia_primeiro_nome = True if abrevia_primeiro_nome is None else False

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
                                        abrevia_primeira_palavra=abrevia_primeiro_nome)
    return "%s, %s" % (
        ' '.join(partes[i_inicial_para_nao_abreviar:i_a_desconsiderar]),
        ' '.join(partes_abreviadas))

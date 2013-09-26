#!/usr/bin/env python
# -*- coding: utf-8 -*-


def _abrevia_partes(nome,
                    abrevia_primeiro_nome=None,
                    retira_conectores=None,
                    abrevia_maria=None,
                    abrevia_depois_de_maria=None,
                    abrevia_descendente=None):

    """
    abrevia_maria default == False
    abrevia_primeiro_nome default == True.
    retira_conectores default == True -> retira "da", "dos", "de", etc.
    """


    partes = nome.split()
    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return nome

    if abrevia_maria is None:
        abrevia_maria = False
    if abrevia_depois_de_maria is None:
        abrevia_depois_de_maria = True
    if abrevia_primeiro_nome is None:
        abrevia_primeiro_nome = True
    if retira_conectores is None:
        retira_conectores = True
    if abrevia_descendente is None:
        abrevia_descendente = False

    if abrevia_descendente:
        descendentes = "filha filho junior neta neto".split()
        if partes[-1].lower() not in descendentes:
            return nome

    b = partes[:-1]

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

    if not abrevia_primeiro_nome:
        b[0] = partes[0]

    if abrevia_maria and partes[0].lower() == "maria":
        b[0] = partes[0][0] + "ª"

    return "%s, %s" % (partes[-1], " ".join(b))


def abrevia_geral(nome,
                  abrevia_primeiro_nome=None,
                  retira_conectores=None,
                  abrevia_maria=None,
                  abrevia_depois_de_maria=None,
                  abrevia_descendente=None):
    """
    abrevia_maria = True -> abrevia o nome Maria.
    abrevia_primeiro_nome = False -> nao abrevia o 1o nome.
    retira_conectores = True -> retira "da", "dos", "de", etc.
    """

    partes_abreviadas = _abrevia_partes(
        nome,
        abrevia_primeiro_nome=abrevia_primeiro_nome,
        retira_conectores=retira_conectores,
        abrevia_maria=abrevia_maria,
        abrevia_depois_de_maria=abrevia_depois_de_maria,
        abrevia_descendente=abrevia_descendente)

    return partes_abreviadas


def abrevia_descendente(*args,
                        **kw):
                        # nome,
                        # elimina_descendencia=None,
                        # abrevia_primeiro_nome=None):
    """
    abrevia_primeiro_nome = False -> nao abrevia o 1o nome.
    """

    return abrevia_geral(*args, **kw)

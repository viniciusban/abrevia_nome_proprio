#!/usr/bin/env python
# -*- coding: utf-8 -*-


def abrevia_nome(nome,
                 abrevia_primeiro_nome=None,
                 retira_conectores=None,
                 abrevia_maria=None,
                 abrevia_depois_de_maria=None,
                 anexa_nome_descendente=None,
                 retira_nome_descendente=None):

    """Abrevia um nome proprio, colocando o ultimo nome no inicio.

    Por padrao, a regra de abreviacao eh:
        - mantem o ultimo nome
        - abrevia todos os outros nomes maiores de 2 caracteres.
        - retira conectores "da", "de", "dos", etc.

    Mas tambem pode:
        - nao abreviar o primeiro nome.
        - abreviar "maria" para "mª".
        - nao abreviar o nome depois de "maria".
        - juntar nomes de descendente com o antecessor: "junior", "filho",
            "neto", etc.
        - retirar o nome de descendente.
    """

    partes = nome.split()

    if abrevia_maria is None:
        abrevia_maria = False
    if abrevia_depois_de_maria is None:
        abrevia_depois_de_maria = True
    if abrevia_primeiro_nome is None:
        abrevia_primeiro_nome = True
    if retira_conectores is None:
        retira_conectores = True
    if anexa_nome_descendente is None:
        anexa_nome_descendente = False
    if retira_nome_descendente is None:
        retira_nome_descendente = False

    if anexa_nome_descendente:
        # anexa o nome de descendente com o nome que vem antes dele.
        # Exemplo: "pedro ferreira junior" seria abreviado para
        # "junior, p. f.".
        # Mas se anexa_nome_descendente == True fica assim:
        # "ferreira junior, p."
        descendentes = "filha filho junior neta neto".split()
        if partes[-1].lower() in descendentes:
            if retira_nome_descendente:
                # apaga o nome do descendente
                if len(partes) > 2:
                    del partes[-1]
                else:
                    return nome
            else:
                if len(partes) > 2:
                    partes[-1] = " ".join(partes[-2:])
                    del partes[-2]
        else:
            return nome

    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
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
        # desfaz abreviacao do nome depois de "maria"
        b[1] = depois_de_maria

    if not abrevia_primeiro_nome:
        # desfaz abreviacao do primeiro nome
        b[0] = partes[0]

    if abrevia_maria and partes[0].lower() == "maria":
        # "maria" vira "mª"
        b[0] = partes[0][0] + "ª"

    return "%s, %s" % (partes[-1], " ".join(b))


def abrevia_de_todas_as_formas(nome):
    """executa a abreviacao de nomes usando todas as combinacoes
    possiveis de parametros.
    """

    nomes = []
    bools = [True, False]
    params = {}
    for params['abrevia_primeiro_nome'] in bools:
        for params['retira_conectores'] in bools:
            for params['abrevia_maria'] in bools:
                for params['abrevia_depois_de_maria'] in bools:
                    for params['anexa_nome_descendente'] in bools:
                        for params['retira_nome_descendente'] in bools:
                            resultado = abrevia_nome(nome, **params)
                            nomes.append(resultado)
    return list(set(nomes))

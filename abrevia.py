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
        - abreviar "maria" para "mª" se for o primeiro nome.
        - nao abreviar o nome depois de "maria", qdo "maria" for o primeiro
          nome.
        - anexar nome de descendente ao nome anterior: "junior", "filho",
            "neto", etc.
        - retirar o nome de descendente.
    """

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

    if not abrevia_primeiro_nome and abrevia_maria:
        raise ValueError(
            "abrevia_primeiro_nome nao pode ser False quando abrevia_maria "
            "for True.")

    if anexa_nome_descendente and retira_nome_descendente:
        raise ValueError(
            "anexa_nome_descendente e retira_nome_descendente nao "
            "podem ser True ao mesmo tempo.")
    elif anexa_nome_descendente or retira_nome_descendente:
        descendentes = "filha filho junior neta neto".split()

    partes = nome.replace(".", ". ").split()

    if retira_nome_descendente:
        if partes[-1].lower() in descendentes:
            # apaga o nome do descendente
            del partes[-1]
    elif anexa_nome_descendente:
        # anexa o nome de descendente com o nome que vem antes dele.
        # Exemplo: "pedro ferreira junior" seria abreviado para
        # "junior, p. f.", por padrao.
        # Mas se anexa_nome_descendente == True, fica assim:
        # "ferreira junior, p."
        if partes[-1].lower() in descendentes:
            if len(partes) > 2:
                # soh junta se tiver mais de 2 nomes pq nomes como
                # "Carlos Neto" ficariam soh com 1 parte e seriam
                # descartados no teste de um nome soh, abaixo.
                partes[-2] = " ".join(partes[-2:])
                del partes[-1]
        else:
            return nome

    if len(partes) == 1:
        # nao abrevia se tem um nome soh.
        return nome

    # a eh o array com nomes que serao abreviados.
    # Nao pega o ultimo nome pq ele nao eh abreviado nunca.
    a = partes[:-1]

    if retira_conectores:
        conectores = "da de do das dos e".split()
        a = [s for s in a if s not in conectores]

    depois_de_maria = None
    if not abrevia_depois_de_maria and a[0].lower() == "maria":
        depois_de_maria = a[1]

    # So abrevia palavras com +2 letras.
    # Obs.: partes do nome com 1 letra tambem sao "abreviadas"
    a = [s if len(s) == 2 else s[0] + "." for s in a]

    if depois_de_maria:
        # desfaz abreviacao do nome depois de "maria"
        a[1] = depois_de_maria

    if not abrevia_primeiro_nome:
        # desfaz abreviacao do primeiro nome
        a[0] = partes[0]

    if abrevia_maria and partes[0].lower() == "maria":
        # "maria" vira "mª"
        a[0] = partes[0][0] + "ª"

    return "%s, %s" % (partes[-1], " ".join(a))


def abrevia_de_todas_as_formas(nome):
    """abrevia nomes usando todas as combinacoes possiveis de parametros.
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
                            if (params['anexa_nome_descendente'] and
                                    params['retira_nome_descendente']):
                                continue
                            elif (not params['abrevia_primeiro_nome'] and
                                    params['abrevia_maria']):
                                continue

                            resultado = abrevia_nome(nome, **params)
                            if resultado != nome:
                                nomes.append(resultado)
    return list(set(nomes))

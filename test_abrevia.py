#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abrevia import *


def test_nao_abrevia_com_1_nome():
    nome = "fulano"
    assert nome == abrevia_nome(nome)


def test_abrevia_com_2_nomes():
    assert "silva, j." == abrevia_nome("jose silva")


def test_abrevia_com_3_nomes():
    assert "sauro, j. s." == abrevia_nome("jose silva sauro")


def test_nao_anexa_nome_descendente_1_nome():
    nome = "junior"
    assert nome == abrevia_nome(nome,
                                anexa_nome_descendente=True)


def test_nao_anexa_nome_descendente_sem_junior():
    nome = "fulano de tal"
    assert nome == abrevia_nome(nome,
                                anexa_nome_descendente=True)


def test_anexa_nome_descendente_varios_nomes():
    assert "sauro junior, j. s." == abrevia_nome(
        "jose silva sauro junior",
        anexa_nome_descendente=True)


def test_anexa_nome_descendente_2_nomes():
    assert "junior, j." == abrevia_nome("jose junior",
                                        anexa_nome_descendente=True)


def test_nao_abrevia_eliminando_descendente_2_nomes():
    nome = "jose junior"
    assert nome == abrevia_nome(nome,
                                anexa_nome_descendente=True,
                                elimina_nome_descendente=True)


def test_nao_abrevia_eliminando_descendente_sem_junior():
    nome = "fulano de tal"
    assert nome == abrevia_nome(nome,
                                anexa_nome_descendente=True,
                                elimina_nome_descendente=True)


def test_abrevia_eliminando_descendente_varios_nomes():
    assert "sauro, j. s." == abrevia_nome(
        "jose silva sauro junior",
        anexa_nome_descendente=True,
        elimina_nome_descendente=True)


def test_nao_abrevia_primeiro_nome():
    assert "sauro, maria s." == abrevia_nome("maria silva sauro",
                                             abrevia_primeiro_nome=False)


def test_anexa_nome_descendente_varios_nomes_exceto_primeiro():
    assert "sauro junior, jose s." == abrevia_nome(
        "jose silva sauro junior",
        anexa_nome_descendente=True,
        abrevia_primeiro_nome=False)


def test_abrevia_eliminando_descendente_varios_nomes_exceto_primeiro():
    assert "sauro, jose s." == abrevia_nome(
        "jose silva sauro junior",
        abrevia_primeiro_nome=False,
        anexa_nome_descendente=True,
        elimina_nome_descendente=True)


def test_nao_abrevia_nome_conector():
    assert "sauro, m. da s." == abrevia_nome(
        "maria da silva sauro",
        retira_conectores=False)


def test_elimina_nome_conector():
    assert "sauro, m. s." == abrevia_nome(
        "maria da silva sauro",
        retira_conectores=True)


def test_abrevia_maria_quando_primeiro_nome():
    assert "sauro, mª s." == abrevia_nome(
        "maria da silva sauro",
        abrevia_maria=True)


def test_nao_abrevia_depois_de_maria():
    assert "sauro, m. silva" == abrevia_nome(
        "maria da silva sauro",
        abrevia_depois_de_maria=False)


def test_tudo_maria():
    nome = "maria da silva sauro"
    nomes = abrevia_tudo(nome)
    resultados = set(nomes)

    esperados = set([
            "sauro, m. s.",
            "sauro, m. da s.",
            "sauro, maria s.",
            "sauro, maria da s.",
            "sauro, m. silva",
            "sauro, mª silva",
            "sauro, mª s.",
            "sauro, mª da s.",
            "sauro, maria silva",
            "maria da silva sauro",
            ])

    assert esperados == resultados


def test_tudo_vicente():
    nome = "vicente barbosa de andrade neto"
    nomes = abrevia_tudo(nome)
    resultados = set(nomes)

    esperados = set([
            "neto, v. b. a.",
            "neto, v. b. de a.",
            "neto, vicente b. a.",
            "neto, vicente b. de a.",
            "andrade, v. b.",
            "andrade, v. b. de",
            "andrade, vicente b.",
            "andrade, vicente b. de",
            "andrade neto, v. b.",
            "andrade neto, v. b. de",
            "andrade neto, vicente b.",
            "andrade neto, vicente b. de",
            ])

    assert esperados == resultados


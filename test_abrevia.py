#!/usr/bin/env python
# -*- coding: utf-8 -*-

from abrevia import *


def test_nao_abrevia_com_1_nome():
    nome = "fulano"
    assert nome == abrevia_geral(nome)


def test_abrevia_com_2_nomes():
    assert "silva, j." == abrevia_geral("jose silva")


def test_abrevia_com_3_nomes():
    assert "sauro, j. s." == abrevia_geral("jose silva sauro")


def test_nao_abrevia_descendente_1_nome():
    nome = "junior"
    assert nome == abrevia_descendente(nome)


def test_nao_abrevia_descendente_sem_junior():
    nome = "fulano de tal"
    assert nome == abrevia_descendente(
            nome,
            abrevia_descendente=True)


def test_abrevia_descendente_varios_nomes():
    assert "sauro junior, j. s." == abrevia_descendente(
        "jose silva sauro junior")


def test_abrevia_descendente_2_nomes():
    assert "junior, j." == abrevia_descendente("jose junior")


def test_nao_abrevia_eliminando_descendente_1_nome():
    nome = "junior"
    assert nome == abrevia_descendente(nome, elimina_descendencia=True)


def test_nao_abrevia_eliminando_descendente_2_nomes():
    nome = "jose junior"
    assert nome == abrevia_descendente(nome, elimina_descendencia=True)


def test_nao_abrevia_eliminando_descendente_sem_junior():
    nome = "fulano de tal"
    assert nome == abrevia_descendente(nome, elimina_descendencia=True)


def test_abrevia_eliminando_descendente_varios_nomes():
    assert "sauro, j. s." == abrevia_descendente(
        "jose silva sauro junior", elimina_descendencia=True)


def test_nao_abrevia_primeiro_nome():
    assert "sauro, maria s." == abrevia_geral("maria silva sauro",
                                              abrevia_primeiro_nome=False)


def test_abrevia_descendente_varios_nomes_exceto_primeiro():
    assert "sauro junior, jose s." == abrevia_descendente(
        "jose silva sauro junior",
        abrevia_primeiro_nome=False)


def test_abrevia_eliminando_descendente_varios_nomes_exceto_primeiro():
    assert "sauro, jose s." == abrevia_descendente(
        "jose silva sauro junior",
        abrevia_primeiro_nome=False,
        elimina_descendencia=True)


def test_nao_abrevia_nome_conector():
    assert "sauro, m. da s." == abrevia_geral(
        "maria da silva sauro",
        retira_conectores=False)


def test_elimina_nome_conector():
    assert "sauro, m. s." == abrevia_geral(
        "maria da silva sauro",
        retira_conectores=True)


def test_abrevia_maria_quando_primeiro_nome():
    assert "sauro, mª s." == abrevia_geral(
        "maria da silva sauro",
        abrevia_maria=True)


def test_nao_abrevia_depois_de_maria():
    assert "sauro, m. silva" == abrevia_geral(
        "maria da silva sauro",
        abrevia_depois_de_maria=False)

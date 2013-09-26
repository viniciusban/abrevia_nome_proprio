#!/usr/bin/env python

from abrevia import *


def test_abrevia_com_1_nome():
    assert "nome" == abrevia_geral("nome")


def test_abrevia_com_2_nomes():
    assert "ultimo, p." == abrevia_geral("prim ultimo")


def test_abrevia_com_3_nomes():
    assert "ultimo, p. s." == abrevia_geral("prim seg ultimo")


def test_nao_abrevia_descendente_1_nome():
    assert "junior" == abrevia_descendente("junior")


def test_nao_abrevia_descendente_sem_junior():
    assert None == abrevia_descendente("fulano de tal")


def test_abrevia_descendente_varios_nomes():
    assert "terc junior, p. s." == abrevia_descendente("prim seg terc junior")


def test_abrevia_descendente_2_nomes():
    assert "junior, p." == abrevia_descendente("prim junior")


def test_abrevia_eliminando_descendente():
    assert "terc, p. s." == abrevia_eliminando_descendente("prim seg terc junior")

#!/usr/bin/env python

from abrevia import *


def test_abrevia_com_1_nome():
    assert "primeiro" == abrevia_geral("primeiro")


def test_abrevia_com_2_nomes():
    assert "ultimo, p." == abrevia_geral("primeiro ultimo")


def test_abrevia_com_3_nomes():
    assert "ultimo, p. s." == abrevia_geral("primeiro segundo ultimo")


def test_abrevia_com_4_nomes():
    assert "ultimo, p. s. t." == abrevia_geral("primeiro segundo terceiro ultimo")


def test_abrevia_junior():
    assert "segundo junior, p." == abrevia_geral("primeiro segundo junior")

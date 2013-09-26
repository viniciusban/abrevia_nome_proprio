#!/usr/bin/env python

from abrevia import abrevia_nome as abrevia


def test_abrevia_com_1_nome():
    assert "primeiro" == abrevia("primeiro")


def test_abrevia_com_2_nomes():
    assert "ultimo, p." == abrevia("primeiro ultimo")


def test_abrevia_com_3_nomes():
    assert "ultimo, p. s." == abrevia("primeiro segundo ultimo")


def test_abrevia_com_4_nomes():
    assert "ultimo, p. s. t." == abrevia("primeiro segundo terceiro ultimo")


def test_abrevia_junior():
    assert "segundo junior, p." == abrevia("primeiro segundo junior")

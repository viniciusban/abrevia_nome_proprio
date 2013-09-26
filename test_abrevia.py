#!/usr/bin/env python

from abrevia import abrevia_nome as abrevia

def test_abrevia_com_2_nomes():
    assert "ultimo, p." == abrevia("primeiro ultimo")

def test_abrevia_com_3_nomes():
    assert "ultimo, p. s." == abrevia("primeiro segundo ultimo")

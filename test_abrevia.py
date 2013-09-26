#!/usr/bin/env python

from abrevia import abrevia_nome as abrevia

def test_abrevia_com_dois_nomes():
    assert "ultimo, p." == abrevia("primeiro ultimo")

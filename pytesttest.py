import pytest

def con(number,sist):
    if (sist == 2):
        return bin(number)[2:]
    elif (sist == 8):
        return oct(number)[2:]
    elif (sist == 16):
        return hex(number)[2:]
def dex(t):
    a = bin(t)[2:]

    b = int(a,2)

    d = hex(b)[2:]

    c = int(d,16)

    v = bin(c)[2:]

    t = int(v,2)
    return t




def test_con () :
    assert con(255,16) == 'ff'
    assert con(255,8) == '377'
    assert con(255,2) == '11111111'
def test_dex ():
    assert dex(12) == 12
    assert bin(12)[2:] =='1100'
    assert int(12) ==12
    assert hex(12)[2:] == 'c'
    assert int(12) == 12
    assert bin(12)[2:] == '1100'
    assert int(12) == 12






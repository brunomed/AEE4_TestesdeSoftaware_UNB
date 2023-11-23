import pytest
from Calculadora import add


# requisito 1
def test_add_func_empstr():
    assert add("") == 0

def test_add_func_floatstr():
    with pytest.raises(Exception, match="ERRO DECIMAL"):
        add("1.2")

def test_add_func_correct():
    assert add("1,2") == 3

def test_add_func_oneNum():
    assert add("1") == 1

test_add_func_empstr()

test_add_func_floatstr()

test_add_func_correct()

test_add_func_oneNum()



# requisito 2
def test_add_func_manyNum():
    assert add("1,2,3,5,6,7,8,9") == 41

def test_add_func_n():
    assert add("1,2\n3") == 6

def test_add_func_invalid():
    with pytest.raises(Exception, match='Invalid String'):
        add('2,\n3')

test_add_func_manyNum()
test_add_func_n()
test_add_func_invalid()


# requisito 4
def test_add_separador():
    with pytest.raises(Exception, match='Invalid String'):
        add('1,2,')

test_add_separador()


#requisito 5
def test_add_given_separator():
    assert add("//;\n1;3") == 4

def test_add_given_separator1():
    with pytest.raises(Exception, match="'|' esperado, mas econtrado ','" ):
        add("//|\n1|2,3")

test_add_given_separator()

test_add_given_separator1()
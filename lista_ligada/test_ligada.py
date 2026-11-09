from lista_ligada import ListaLigada
import pytest

@pytest.fixture
def lista():
    lista = ListaLigada()
    lista.adicionar(10)
    lista.adicionar(20)
    lista.adicionar(30)
    lista.adicionar(40)
    return lista
    
    
def test_exibir_lista(lista):
    lista.exibir()
    assert "10 -> 20 -> 30 -> 40 -> null"


def test_print_str_lista(lista):
    print(lista)
    assert "10 -> 20 -> 30 -> 40 -> null"


def test_inserir_inicio_lista_cheia(lista):
    lista.inserir_inicio(5)
    assert lista.primeiro.item == 5
    assert "5 -> 10 -> 20 -> 30 -> 40 -> null"


def test_inserir_inicio_lista_vazia():
    lista0 = ListaLigada()
    lista0.inserir_inicio(1)
    assert lista0.primeiro.item == 1
    assert "1 -> null"


if __name__ == "__main__":
    pytest.main(["-v"])
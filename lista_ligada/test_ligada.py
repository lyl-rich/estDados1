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
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"


def test_print_str_lista(lista):
    print(lista)
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"


def test_inserir_inicio_lista_cheia(lista):
    lista.inserir_inicio(5)
    assert lista.primeiro.item == 5
    assert str(lista) == "5 -> 10 -> 20 -> 30 -> 40 -> null"


def test_inserir_inicio_lista_vazia():
    lista0 = ListaLigada()
    lista0.inserir_inicio(1)
    assert lista0.primeiro.item == 1
    assert "1 -> null"


def test_pesquisar_true(lista):
    assert lista.pesquisar(30) == True


def test_pesquisar_false(lista):
    assert lista.pesquisar(90) == False


def test_obter_true(lista):
    assert lista.obter(2) == 30


def test_obter_false(lista):
    assert lista.obter(5) == None


def test_inserir_true(lista):
    assert lista.inserir(2, 25) is True
    assert str(lista) == "10 -> 20 -> 25 -> 30 -> 40 -> null"
    assert lista.tamanho == 5


def test_inserir_posicao_igual_tamanho(lista):
    assert lista.inserir(4, 45) is True
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> 45 -> null"
    assert lista.tamanho == 5


def test_inserir_false(lista):
    assert lista.inserir(5, 50) is False
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"
    assert lista.tamanho == 4


def test_remover_true(lista):
    assert lista.remover(2) == True
    assert str(lista) == "10 -> 20 -> 40 -> null"
    assert lista.tamanho == 3
    


def test_remover_false(lista):
    assert lista.remover(4) == False
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"
    assert lista.tamanho == 4


def test_remover_primeir0(lista):
    assert lista.remover(0) == True
    assert lista.primeiro.item == 20
    assert str(lista) == "20 -> 30 -> 40 -> null"


def test_remover_item_true(lista):
    assert lista.remover_item(30) == True
    assert str(lista) == "10 -> 20 -> 40 -> null"
    assert lista.tamanho == 3
    


def test_remover_item_false(lista):
    assert lista.remover_item(15) == False
    assert str(lista) == "10 -> 20 -> 30 -> 40 -> null"
    assert lista.tamanho == 4


def test_remover_item_primeir0(lista):
    assert lista.remover_item(10) == True
    assert lista.primeiro.item == 20
    assert str(lista) == "20 -> 30 -> 40 -> null"


if __name__ == "__main__":
    pytest.main(["-v"])
from lista_ligada.lista_ligada import ListaLigada

class Fila:

    def __init__(self):
        self._elementos = ListaLigada()


    def enfileirar(self, item):
        self._elementos.adicionar(item)


    def desenfileirar(self):
        item = self.primeiro()
        self._elementos.remover(0)
        return item


    def primeiro(self):
        if self.vazia():
            return None
        return self._elementos.primeiro.item


    def vazia(self): #is_empty()
        return self._elementos.primeiro is None
    
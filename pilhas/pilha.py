from lista_ligada.lista_ligada import ListaLigada

class Pilha():

    def __init__(self):
        self._elementos = ListaLigada()


    def empilhar(self, item): #push
        self._elementos.inserir_inicio(item)


    def desempilhar(self): #pop
        item = self.topo()
        self._elementos.remover(0)
        return item


    def topo(self): #peek
        if self.vazia():
            return None
        return self._elementos.primeiro.item


    def vazia(self): #is_empty()
        return self._elementos.primeiro is None
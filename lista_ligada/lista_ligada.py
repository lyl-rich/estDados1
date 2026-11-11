from lista_ligada.no import No

class ListaLigada:

    def __init__(self):
        self.primeiro: No = None
        self.tamanho = 0


    def adicionar(self, item):
        """ Adiciona no fim da lista - O(n)"""

        novo_no = No(item)
        if self.primeiro is None:
            self.primeiro = novo_no
        else:
            atual = self.primeiro
            while atual.proximo:
                atual = atual.proximo
            atual.proximo = novo_no
        self.tamanho += 1


    def inserir_inicio(self, item):
        """ Adiciona no inicio da lista - O(1)"""

        novo_no = No(item)
        novo_no.proximo = self.primeiro
        self.primeiro = novo_no
        self.tamanho += 1


    def exibir(self):
        """ Exibe os itens da lista - O(n)"""

        atual = self.primeiro
        while atual:
            print(atual.item, end=" -> ")
            atual = atual.proximo
        print("null")


    def __str__(self):
        """ Retorna uma representação em string da lista - O(n)"""

        itens = []
        atual = self.primeiro
        while atual:
            itens.append(str(atual.item))
            atual = atual.proximo
        return " -> ".join(itens) + " -> null"


    '''
    def __str__(self):
        """ Retorna uma representação em string da lista - O(n)"""

        atual = self.primeiro
        string = ""

        while atual:
            string += atual.item + " -> "
            atual = atual.proximo
        return string + "null"
    '''


    def pesquisar(self, item):
        """ Retorna True caso o item procurado exista na lista e
        False, em caso contrário. O(n)"""
        
        atual = self.primeiro
        while atual:
            if atual.item == item:
                return True
            atual = atual.proximo
        return False


    def obter(self, posicao):
        """ Retorna o item guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None. O(n)"""
        
        if 0 < posicao < self.tamanho:
            atual = self.primeiro
            for _ in range(posicao):
                atual = atual.proximo
            
            return atual.item
        return None


    def inserir(self, posicao, item):
        """ Adiciona um item em uma posição da lista
        empurrando os demais itens para o fim da lista.
        Se a posição não é válida, retorna False. O(n)"""
        
        if 0 <= posicao <= self.tamanho:
            if posicao == 0:
                self.inserir_inicio(item)
                return True
            
            atual = self.primeiro
            for _ in range(posicao - 1):
                atual = atual.proximo
            
            novo_no = No(item)
            novo_no.proximo = atual.proximo
            atual.proximo = novo_no
            self.tamanho += 1
            
            return True
        return False


    def remover(self, posicao):
        """ Remove um item de uma posição da lista
        e puxa os demais itens para o início da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False. O(n)"""

        if 0 <= posicao < self.tamanho:
            if (posicao == 0):
                self.primeiro = self.primeiro.proximo
                self.tamanho -= 1
                return True
            
            atual = self.primeiro
            for _ in range(posicao - 1):
                atual = atual.proximo
                
            atual.proximo = atual.proximo.proximo
            self.tamanho -= 1
            
            return True
        return False


    def remover_item(self, item):
        """ Remove um item existente na lista e retorna True.
        Caso o item não seja encontrado, retorna False. O(n)"""

        atual = self.primeiro
        for posicao in range(self.tamanho):
            if atual.item == item:
                self.remover(posicao)
                return True
            
            atual = atual.proximo
        return False


    def vazia(self):
        return self.tamanho == 0
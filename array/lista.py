class Lista:

    def __init__(self, capacidade):
        self.capacidade = capacidade
        self.array = [None] * capacidade
        self.tamanho = 0    # ULTIMO/ATUAL do array



    def adicionar(self, numero):
        if (self.tamanho < self.capacidade):
            self.array[self.tamanho] = numero
            self.tamanho += 1
            return True
        
        return False



    def pesquisar(self, numero):
        for num in self.array:
            if (num == numero):
                return True

        return False



    def obter(self, posicao):
        """
        Retorna o número guardado em uma determinada posição da lista.
        Caso a posição não exista na lista, retorna None.
        """
        if (0 <=posicao < self.tamanho):
            return self.array[posicao]
        
        return None



    def inserir(self, posicao, numero):
        """
        Adiciona um número em uma posição da lista
        empurrando os demais números para o fim da lista.
        Se tem espaço na lista retorna True, se não, False.
        """
#       if (0 <= posicao <= self.tamanho) and (self.tamanho < self.capacidade):
        if (0 <= posicao <= self.tamanho < self.capacidade):
            for i in range(self.tamanho, posicao, -1):
                self.array[i] = self.array[i-1]

            self.array[posicao] = numero
            self.tamanho += 1
            return True

        return False



    def remover(self, posicao):
        """
        Remove um número de uma posição da lista e
        puxa os demais números para deixar o espaço vazio no fim da lista.
        Ao final, retorna True. Caso a posição não exista na lista, retorna False.
        """
        if (0 <= posicao < self.tamanho):
            self.tamanho -= 1   #agora vale o mesmo que o indice (começa de 0) e ja diminui o tamanho

            for i in range(posicao, self.tamanho):
                self.array[i] = self.array[i+1]

            self.array[self.tamanho] = None
            return True
        
        return False

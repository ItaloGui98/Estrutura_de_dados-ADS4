class No:
    def __init__(self, valor1, valor2, proximo=None):
        self.valor1 = valor1
        self.valor2 = valor2
        self.proximo = proximo


class Lista:
    def __init__(self):
        self.cabeca = None

    def ObterProximo(self, no):
        return no.proximo

    def ObterValor(self, no):
        return (no.valor1, no.valor2)

    def AlterarNo(self, no, novo_valor1, novo_valor2):
        no.valor1 = novo_valor1
        no.valor2 = novo_valor2

    def Tamanho(self):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def Existe(self, valor1):
        atual = self.cabeca
        while atual is not None:
            if atual.valor1 == valor1:
                return True
            atual = atual.proximo
        return False

    def mostrarALL(self):
        elementos = []
        atual = self.cabeca
        while atual is not None:
            elementos.append((atual.valor1, atual.valor2))
            atual = atual.proximo
        return elementos

    def Buscar(self, valor1):
        return self.Existe(valor1)

    def Inserir(self, valor1, valor2):
        novo = No(valor1, valor2)

        if self.cabeca is None or valor1 <= self.cabeca.valor1:
            novo.proximo = self.cabeca
            self.cabeca = novo
            return

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.valor1 < valor1:
            atual = atual.proximo

        novo.proximo = atual.proximo
        atual.proximo = novo

    def Excluir(self, valor1):
        atual = self.cabeca
        anterior = None

        while atual is not None:
            if atual.valor1 == valor1:
                if anterior is None:
                    self.cabeca = atual.proximo
                else:
                    anterior.proximo = atual.proximo
                self.Destrutor(atual)
                return True
            anterior = atual
            atual = atual.proximo

        return False

    def Destrutor(self, no):
        no.proximo = None
        del no

##Questão 2
def main():
    lista = Lista()

    lista.Inserir(5, 10)
    lista.Inserir(2, 20)
    lista.Inserir(8, 30)
    lista.Inserir(1, 40)
    lista.Inserir(5, 99)  

    print("Lista ordenada:", lista.mostrarALL())
    print("Tamanho da lista:", lista.Tamanho())

    print("Existe valor1 = 8?", lista.Existe(8))
    print("Existe valor1 = 100?", lista.Existe(100))
    print("Buscar valor1 = 2:", lista.Buscar(2))

    primeiro = lista.cabeca
    print("Valores do primeiro nó:", lista.ObterValor(primeiro))

    segundo = lista.ObterProximo(primeiro)
    print("Valores do segundo nó:", lista.ObterValor(segundo))

    lista.AlterarNo(primeiro, 1, 777)
    print("Lista após AlterarNo no primeiro nó:", lista.mostrarALL())

    lista.Excluir(2)
    print("Lista após excluir valor1 = 2:", lista.mostrarALL())
    print("Tamanho final:", lista.Tamanho())

main()
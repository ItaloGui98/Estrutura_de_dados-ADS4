class No:
    def __init__(self, coeficiente, grau, proximo=None):
        self.coeficiente = coeficiente
        self.grau = grau
        self.proximo = proximo

class Polinomio:
    def __init__(self):
        self.cabeca = None

    def inserir(self, coeficiente, grau):
        novo = No(coeficiente, grau)

        if self.cabeca is None or grau > self.cabeca.grau:
            novo.proximo = self.cabeca
            self.cabeca = novo
            return

        atual = self.cabeca
        while atual.proximo is not None and atual.proximo.grau >= grau:
            atual = atual.proximo

        novo.proximo = atual.proximo
        atual.proximo = novo

    def simplificar(self):
        atual = self.cabeca
        while atual is not None and atual.proximo is not None:
            if atual.grau == atual.proximo.grau:
                atual.coeficiente += atual.proximo.coeficiente
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo

        fantasma = No(0, None, self.cabeca)
        atual = fantasma
        while atual.proximo is not None:
            if atual.proximo.coeficiente == 0:
                atual.proximo = atual.proximo.proximo
            else:
                atual = atual.proximo
        self.cabeca = fantasma.proximo

    def grau(self):
        if self.cabeca is None:
            return 0
        return self.cabeca.grau

    def tamanho(self):
        contador = 0
        atual = self.cabeca
        while atual is not None:
            contador += 1
            atual = atual.proximo
        return contador

    def avaliar(self, x):
        resultado = 0
        atual = self.cabeca
        while atual is not None:
            resultado += atual.coeficiente * (x ** atual.grau)
            atual = atual.proximo
        return resultado

    def __add__(self, outro):
        resultado = Polinomio()

        atual = self.cabeca
        while atual is not None:
            resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo

        atual = outro.cabeca
        while atual is not None:
            resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo

        resultado.simplificar()
        return resultado

    def __sub__(self, outro):
        resultado = Polinomio()

        atual = self.cabeca
        while atual is not None:
            resultado.inserir(atual.coeficiente, atual.grau)
            atual = atual.proximo

        atual = outro.cabeca
        while atual is not None:
            resultado.inserir(-atual.coeficiente, atual.grau)
            atual = atual.proximo

        resultado.simplificar()
        return resultado

    def __mul__(self, outro):
        resultado = Polinomio()

        atual1 = self.cabeca
        while atual1 is not None:
            atual2 = outro.cabeca
            while atual2 is not None:
                resultado.inserir(
                    atual1.coeficiente * atual2.coeficiente,
                    atual1.grau + atual2.grau,
                )
                atual2 = atual2.proximo
            atual1 = atual1.proximo

        resultado.simplificar()
        return resultado

    def exibir(self):
        if self.cabeca is None:
            return "0"

        partes = []
        atual = self.cabeca
        primeiro = True

        while atual is not None:
            coef = atual.coeficiente
            grau = atual.grau

            if coef == 0:
                atual = atual.proximo
                continue

            if primeiro:
                sinal = "-" if coef < 0 else ""
            else:
                sinal = " - " if coef < 0 else " + "

            valor_abs = abs(coef)
            if valor_abs == int(valor_abs):
                valor_abs = int(valor_abs)

            if grau == 0:
                termo = f"{valor_abs}"
            elif grau == 1:
                termo = "x" if valor_abs == 1 else f"{valor_abs}x"
            else:
                termo = f"x^{grau}" if valor_abs == 1 else f"{valor_abs}x^{grau}"

            partes.append(sinal + termo)
            primeiro = False
            atual = atual.proximo

        return "".join(partes) if partes else "0"

    def __str__(self):
        return self.exibir()


def ler_polinomio_da_linha(linha):
    numeros = list(map(float, linha.split()))
    polinomio = Polinomio()
    for i in range(0, len(numeros), 2):
        coeficiente = numeros[i]
        grau = int(numeros[i + 1])
        polinomio.inserir(coeficiente, grau)
    polinomio.simplificar()
    return polinomio


def processar_arquivo(caminho):
    with open(caminho, "r", encoding="utf-8") as arquivo:
        linhas = [linha.strip() for linha in arquivo if linha.strip() != ""]

    i = 0
    while i < len(linhas):
        operacao = linhas[i].lower()
        i += 1

        if operacao in ("+", "-", "*"):
            p1 = ler_polinomio_da_linha(linhas[i])
            i += 1
            p2 = ler_polinomio_da_linha(linhas[i])
            i += 1

            if operacao == "+":
                resultado = p1 + p2
            elif operacao == "-":
                resultado = p1 - p2
            else:
                resultado = p1 * p2

            print(f"Resultado ({operacao}): {resultado}")

        elif operacao == "g":
            p = ler_polinomio_da_linha(linhas[i])
            i += 1
            print(f"Grau: {p.grau()}")

        elif operacao == "t":
            p = ler_polinomio_da_linha(linhas[i])
            i += 1
            print(f"Tamanho: {p.tamanho()}")

        elif operacao == "p":
            p = ler_polinomio_da_linha(linhas[i])
            i += 1
            print(f"Polinômio: {p}")

        elif operacao == "a":
            x = float(linhas[i])
            i += 1
            p = ler_polinomio_da_linha(linhas[i])
            i += 1
            resultado = p.avaliar(x)
            print(f"p({x}) = {resultado}")

        else:
            print(f"Operação desconhecida: '{operacao}'")


if __name__ == "__main__":
    import os
    
    pasta_do_script = os.path.dirname(os.path.abspath(__file__))
    caminho_entrada = os.path.join(pasta_do_script, "entrada.txt")
    processar_arquivo(caminho_entrada)
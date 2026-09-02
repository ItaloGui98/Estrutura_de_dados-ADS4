def esta_balanceada(expressao):
    pilha = []
    pares = {')': '(', ']': '[', '}': '{'}
    abertura = '([{'
    fechamento = ')]}'

    for char in expressao:
        if char in abertura:
            pilha.append(char)
        elif char in fechamento:
            if not pilha:
                return False
            topo = pilha.pop()
            if topo != pares[char]:
                return False
    return len(pilha) == 0

expressoes = [
    "(a + b)",
    "{[a * (b + c)]}",
    "a + {b - [c * d]}",
    "a + (b",
    "{[a * b], (a + b)}",
    "a + {b - [c * d}"
]

for exp in expressoes:
    resultado = "balanceada" if esta_balanceada(exp) else "NÃO balanceada"
    print(f"'{exp}' -> {resultado}")
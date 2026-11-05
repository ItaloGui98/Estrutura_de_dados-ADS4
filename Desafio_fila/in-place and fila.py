from collections import deque

def mover_zeros(nums):
    posicao = 0

    for num in nums:
        if num != 0:
            nums[posicao] = num
            posicao += 1

    while posicao < len(nums):
        nums[posicao] = 0
        posicao += 1

    return nums

def mover_zeros_fila(nums):
    fila = deque()
    zeros = 0

    for num in nums:
        if num == 0:
            zeros += 1
        else:
            fila.append(num)

    posicao = 0

    while fila:
        nums[posicao] = fila.popleft()
        posicao += 1

    while zeros > 0:
        nums[posicao] = 0
        posicao += 1
        zeros -= 1

    return nums


# TESTES DAS DUAS SOLUÇÕES

testes = [
    [0, 1, 0, 3, 12],
    [0],
    [1, 2, 3],
    [0, 0, 0],
    [1, 0, 2, 0, 3, 0]
]

print("===== SOLUÇÃO IN-PLACE =====")

for teste in testes:
    print("Entrada:", teste.copy())
    print("Saída:", mover_zeros(teste.copy()))
    print()


print("===== SOLUÇÃO COM FILA =====")

for teste in testes:
    print("Entrada:", teste.copy())
    print("Saída:", mover_zeros_fila(teste.copy()))
    print()


print("===== FIM DOS TESTES =====")

"""
Complexidade --> Tempo e Espaço

Tempo: O(n), pois percorremos o array e reconstruímos seus elementos.

Espaço: O(n), pois a fila pode armazenar até n elementos.

3. Pergunta reflexiva: Por que a abordagem com fila viola a restrição de espaço O(1), mesmo mantendo tempo O(n)?

Porque a fila utiliza memória auxiliar para armazenar os elementos diferentes de zero. No pior caso, quando todos os elementos são diferentes de zero, a fila precisará armazenar todos os elementos do array. Assim, conforme o tamanho do array aumenta, o espaço utilizado pela fila também aumenta."""
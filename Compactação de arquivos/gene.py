# Compactação de uma sequência de DNA

# Cada letra será representada por 2 bits
codigos = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}

# Sequência de DNA
dna = input("Digite a sequência de DNA: ").upper()

# Verifica se a sequência é válida
valida = True

for letra in dna:
    if letra not in codigos:
        valida = False
        break

if valida:
    # Sequência compactada
    compactada = ""

    for letra in dna:
        compactada += codigos[letra]

    # Tamanho original:
    # cada caractere ocupa 8 bits
    tamanho_original = len(dna) * 8

    # Tamanho compactado:
    # cada nucleotídeo ocupa apenas 2 bits
    tamanho_compactado = len(dna) * 2

    print("\nSequência original:")
    print(dna)

    print("\nSequência compactada:")
    print(compactada)

    print("\nTamanho original:", tamanho_original, "bits")
    print("Tamanho compactado:", tamanho_compactado, "bits")

    reducao = tamanho_original - tamanho_compactado

    print("Espaço economizado:", reducao, "bits")

else:
    print("Erro: a sequência deve conter apenas A, C, G ou T.")
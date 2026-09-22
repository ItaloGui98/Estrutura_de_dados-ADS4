codigos = {
    'A': '00',
    'C': '01',
    'G': '10',
    'T': '11'
}

decodigos = {
    '00': 'A',
    '01': 'C',
    '10': 'G',
    '11': 'T'
}

with open("Compactação de arquivos/entrada.txt", "r") as arquivo:
    dna = arquivo.read().replace("\n", "").replace(" ", "").upper()

for letra in dna:
    if letra not in codigos:
        print("Erro: o arquivo possui caracteres inválidos.")
        exit()

bits = ""

for letra in dna:
    bits += codigos[letra]

dados = bytearray()

for i in range(0, len(bits), 8):
    byte = bits[i:i + 8]

    while len(byte) < 8:
        byte += "0"

    dados.append(int(byte, 2))

with open("Compactação de arquivos/compactado.bin", "wb") as arquivo:
    arquivo.write(dados)

bits_descompactados = ""

for byte in dados:
    bits_descompactados += format(byte, "08b")

bits_descompactados = bits_descompactados[:len(dna) * 2]


dna_descompactado = ""

for i in range(0, len(bits_descompactados), 2):
    dois_bits = bits_descompactados[i:i + 2]
    dna_descompactado += decodigos[dois_bits]

with open("Compactação de arquivos/descompactado.txt", "w") as arquivo:
    arquivo.write(dna_descompactado)

tamanho_original = len(dna) * 8
tamanho_compactado = len(dados) * 8
economia = tamanho_original - tamanho_compactado

print("Compactação realizada!")
print()
print("Sequência original:", dna)
print("Sequência descompactada:", dna_descompactado)
print()
print("Tamanho original:", tamanho_original, "bits")
print("Tamanho compactado:", tamanho_compactado, "bits")
print("Economia:", economia, "bits")
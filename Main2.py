# Aqui foi definido os resultados
resultados = [
    ("Equipe Infinity", [10, 20, 30]), # Infinity
    ("Equipe Pixels", [15, 25, 35]), # Pixels
    ("Equipe Gracon", [20, 30, 40]), # Gracon
    ("Equipe PixelsParquelandia", [5, 15, 25]) # Pixelsparquelandia
]

# 1. Calcular a média das pontuações de cada equipe
medias = []
for equipe, pontuacoes in resultados:
    media = sum(pontuacoes) / len(pontuacoes)  # Sum soma as pontuações, Len da a media dessa soma
    medias.append((equipe, media))  # Armazena o dados e adiciona

# 2. Ordenar a lista medias em ordem decrescente
medias.sort(key=lambda x: x[1], reverse=True)

# 3. Criar a lista classificacao
classificacao = [(equipe, media) for equipe, media in medias]

# 4. Exibir a classificação final
print("Classificação Final:")
for equipe, media in classificacao:
    print(f"{equipe}: {media:.2f}")
linhas_e_colunas = [
    (x, y)
    if x != 2 else (x, y * 100)
    for x in range(1, 11)
    for y in range(1, 6)
    if x != 2
]

print(linhas_e_colunas)
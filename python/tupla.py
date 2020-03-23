# ================= Operacoes com tuplas (IMUTAVEIS)

# Usada para definir listas que nao precisam ser alteradas. Por exemplo:
meses = ("Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

tupla = (1, 2, 3, "Teste")

# tupla.sort() # gera erro

for item in tupla:
    print(item)

print(tupla)

print(tupla[2])

# tupla.append(3) # gera um erro
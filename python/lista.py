# ================= Operacoes com listas (MUTAVEIS)

lista = [101, 29, 3]

lista.sort()

for item in lista:
    print(item)

lista.append("Jonnes")

# neste ponto:
# [3, 29, 101, "Jonnes"]

lista_nomes = ["Jonnes", "Carlos Eduardo", "Zé", "Kadu"]
lista_nomes.sort()

for item in lista:
    print(item)

lista.remove("Jonnes")

for item in lista:
    print(item)
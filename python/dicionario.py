# ================= Operacoes com mapas ou dicionarios (MUTAVEIS)

dicionario = {
    "nome" : "Jonnes Nascimento",
    "idade" : 38,
    "altura" : 1.67
}

# para adicionar itens ao meu dicionario:
dicionario["interesses"] = ["programacao", "eletronica", "viagem"]
dicionario["profissao"] = "engenheiro"
dicionario["estado_civil"] = "casado"

for chave, valor in dicionario.items():
    print("%s : %s" % (chave, valor))

print("=" * 50)

dicionario["interesses"].append("esportes")

for chave, valor in dicionario.items():

    if(isinstance(valor, list)):
        print("%s :" % chave)

        for interesse in valor:
            print("\t (*) %s" % interesse)
    else:
        print("%s : %s" % (chave, valor))

print("=" * 50)

# para remover um item do dicionario:
dicionario.pop("estado_civil")

for chave, valor in dicionario.items():

    if(isinstance(valor, list)):
        print("%s :" % chave)

        for interesse in valor:
            print("\t (*) %s" % interesse)
    else:
        print("%s : %s" % (chave, valor))
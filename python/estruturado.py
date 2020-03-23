
# Programacao estruturada = receita de bolo (passo a passo)

pedido = {}

# procedimento para criar o numero do pedido
def gerarNumeroPedido(pedido, numero):
    pedido["numero"] = numero

# procedimento para incluir cliente do pedido
def incluirClientePedido(pedido, nome_cliente):
    pedido["cliente"] = nome_cliente

# procedimento para incluir itens no pedido
def incluirItemPedido(pedido, item):
    if "items" in pedido:
        pedido["items"].append(item)
    else:
        lista = []
        lista.append(item)

        pedido["items"] = lista

# procedimento para definir valor do pedido
def definirValorPedido(pedido, valor):
    pedido["valor"] = valor

#imprime o pedido
def imprimirPedido(pedido):
    print("-" * 50)
    print("PEDIDO " + (43 * ">"))
    print("-" * 50)
    
    for chave, valor in pedido.items():
        if isinstance(valor, list):
            print("%s:" % chave)

            for item in valor:
                print("   (o)  %s" % item)
        else:
            print("%s: %s" % (chave, valor))

    print("-" * 50)
    
# executa a lista de procedimentos
gerarNumeroPedido(pedido, 7563)
incluirClientePedido(pedido, "Jonnes Nascimento")

incluirItemPedido(pedido, "Notebook Intel Core i7")
incluirItemPedido(pedido, "Mouse Microsoft Arc")
incluirItemPedido(pedido, "Monitor Samsung Gamer 49\" Curvo")

definirValorPedido(pedido, 13500.00)

imprimirPedido(pedido)
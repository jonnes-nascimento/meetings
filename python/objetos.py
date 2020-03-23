
class Profissao:
    def __init__(self, descricao):
        self.descricao = descricao

class Pessoa:

    def __init__(self, nome, idade, altura, profissao, interesses):
        self.nome = nome
        self.idade = idade
        self.altura = altura
        self.profissao = Profissao(profissao)
        self.interesses = interesses

    def mostrarInteresses(self):
        print("%s é %s e se interessa por:" % (self.nome, self.profissao.descricao))

        for item in self.interesses:
            print("  * %s" % item)

class Funcionario(Pessoa):
    def __init__(self, nome, idade, altura, profissao, interesses, empresa):
        super().__init__(nome, idade, altura, profissao, interesses)
        self.empresa = empresa

    def mostrarInteresses(self):
        print("%s é %s, trabalha na(o) %s e se interessa por:" % (self.nome, self.profissao.descricao, self.empresa))

        for item in self.interesses:
            print("  * %s" % item)


pessoa1 = Pessoa("Jonnes", 38, 1.68, "engenheiro", ["programacao", "eletronica"])
pessoa1.mostrarInteresses()

funcionario1 = Funcionario("Massimo Argento", 65, 1.72, "professor", ["continhas", "engenharia"], "USJT")
funcionario1.mostrarInteresses()

def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome, sobrenome):
    print(f"Seja bem vindo {nome} {sobrenome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2("Riquelmy", "Henrique")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

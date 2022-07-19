from VERIFICARCPFSENHA import * #importação do modulo que verifica se o cpf e senha estao corretos

def valordoPedido():
    while True:    #estrutura de repetição
        cpf = str(input("CPF:")) #usuario fornece cpf
        senha = str(input("SENHA:")) #usuario fornece senha

        if verificar(cpf=cpf, senha=senha) == True: #se o cpf e senha estiverem corretos:
            with open("valor_%s.txt"%cpf, "r") as listavalores:
                a = listavalores.read()    #"a" é uma lista do arquivo que contem o valor dos produtos de um determinado pedido
                a_lista = a.split("\n")    #divide a lista pelas quebras de linha
                tam = len(a_lista)         # tam = tamanho de a_lista
                a_lista.pop(tam - 1)       #retira o ultimo index pois ele é ''
                b = [float(i) for i in a_lista]#transforma os elementos da lista em float
                valor = sum(b) #realiza a soma do valor dos produtos
                print("O valor do pedido é de R$%.2f"% valor) #print o valor dos produtos
            break
        elif verificar(cpf=cpf, senha=senha) == False: #se o cpf, senha ou ambos estiverem incorretos:
            escolha = int(input("""
            Pedido não encontrado. Tente novamente ou volte ao menu principal.
            0 - Voltar ao menu.
            1 - Tentar novamente.
            """)) #tentar novamente ou voltar ao menu principal
            if escolha == 1:
                continue
            elif escolha == 0:
                break
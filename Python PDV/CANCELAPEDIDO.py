from NOVOPEDIDO import *    #importação dos módulos e bibilotecas necessários
from VERIFICARCPFSENHA import *
import os

def cancelarPedido():       
    while True:    #estrutura de repetição caso o pedido nao seja encontrado
        cpf = str(input("CPF:")) #usuario fornece cpf
        senha = str(input("SENHA:")) #usuario fornece senha

        if verificar(cpf=cpf, senha=senha) == True: #se a senha e cpf estiverem corretos:
            os.remove("%s.txt" % cpf) #deleta o arquivo com o extrato e dados do usuario
            os.remove("valor_%s.txt" % cpf) #deleta o arquivo com os valores dos produtos do usuario
            print("Pedido cancelado com sucesso.")
            break
        elif verificar(cpf=cpf, senha=senha) == False: #se o usuario inserir dados errados:
            escolha = int(input("""
            Pedido não encontrado. Tente novamente ou volte ao menu principal.
            0 - Voltar ao menu.
            1 - Tentar novamente.
            """)) #opçao de tentar novamente ou voltar ao menu principal
            if escolha == 1:
                continue
            elif escolha == 0:
                break
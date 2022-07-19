from COMP_ADDPROD import * #importação de funções através dos módulos
from VERIFICARCPFSENHA import *

def inserirProduto():
    while True:    
        cpf = str(input("CPF:")) #recebe cpf do usuario
        senha = str(input("SENHA:")) #recebe senha do usuario

        if verificar(cpf=cpf, senha=senha) == True: #verifica se as informações recebidas estão corretas
            compAddProd(cpf=cpf) #chama a funçao do menu dos pedidos para inserir um novo produto
            while True: #estrutura de repetição para o caso do usuario querer adicionar outros produtos
                continuar = int(input("""
                +---------------------------------+
                | Deseja adicionar outro produto? |
                +---------------------------------+
                | 0 - Não                         |
                +---------------------------------+
                | 1 - Sim                         |
                +---------------------------------+
                """))
                
                if continuar == 1: #se sim: chama novamente a função do menu dos produtos
                    compAddProd(cpf=cpf)
                    continue
                elif continuar == 0:
                    break
                else:
                    print("Digite um opção válida.")
                    continue
            break
        elif verificar(cpf=cpf, senha=senha) == False: #se os dados fornecidos pelo usuario estiverem incorretos:
            escolha = int(input("""
            Pedido não encontrado. Tente novamente ou volte ao menu principal.
            0 - Voltar ao menu.
            1 - Tentar novamente.
            """)) #voltar ao menu ou tentar novamente
            if escolha == 1:
                continue
            elif escolha == 0:
                break
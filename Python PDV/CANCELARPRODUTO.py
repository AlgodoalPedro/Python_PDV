from VERIFICARCPFSENHA import *
from COMP_REMPROD import *

def cancelarProduto():
    while True:    
        cpf = str(input("CPF:")) #recebe cpf do usuário
        senha = str(input("SENHA:"))#rebece senha do usuário

        if verificar(cpf=cpf, senha=senha) == True: #verifica se a senha e cpf estão corretos:
            compRemProduto(cpf=cpf) #chamada da função que remove produto
            while True: #estrutura de repetição que pergunta ao usuário se ele deseja remover outros produtos ou deseja voltar ao menu principal
                continuar = int(input("""
                +---------------------------------+
                | Deseja cancelar outro produto?  |
                +---------------------------------+
                | 0 - Não                         |
                +---------------------------------+
                | 1 - Sim                         |
                +---------------------------------+
                """))
                
                if continuar == 1: #se desejar remover outros produtos chama a função novamente
                    compRemProduto(cpf=cpf) 
                    continue
                elif continuar == 0:
                    break
                else:
                    print("Digite um opção válida.")
                    continue
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
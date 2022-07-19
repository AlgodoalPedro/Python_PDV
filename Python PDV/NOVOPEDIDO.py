from COMP_ADDPROD import * #importação das funções necessárias através de módulos
from datetime import * 
import os

def novoPedido():

    while True: #estrutura de repetição para que o usuário digite o nome corretamete
        nome = str(input("Nome:")) #input que recebe o nome do usuario
        if nome.isalpha() == True: #condicional para que o nome contenha apenas letras
            break
        else: #se o nome tiver caracteres que nao sejam letras: continuar a repetiçao
            print("""
            Nome inválido. Tente novamente.
            """)
            continue
    
    while True: #estrutura de repetição para que o usuário digite o CPF corretamente
        cpf = str(input("CPF:"))#input que recebe o CFP
        if os.path.exists("%s.txt"%cpf) == False and len(cpf) == 11 and cpf.isnumeric() == True: #condicional que aceita o CPF somente se: tiver 11 digitos, apenas números e não estar cadastrado.
            break
        else: #se o CPF não cumprir com as condições do if acima: print mensagem de erro e continua o ciclo
            print("""
            Esse CPF já está registrado ou é inválido. Tente novamente.
            """)
            continue
    
    senha = str(input("Senha:")) #input que recebe a senha do usuario
        
    with open("%s.txt"%cpf, "a") as extrato: #cria arquivo com o nome sendo o CPF do usuario
        extrato.write("%s\n"%senha) #escreve a senha do usuario
        extrato.write("Nome: %s\n"%nome)#escreve o nome do usuario
        extrato.write("CPF: %s\n"%cpf)#escreve CFP do usuário
        extrato.write("Total:\n")#escreve "Total:" sem valor por enquanto
        extrato.write(datetime.now().strftime("%d-%m-%Y %H:%M\n"))#escreve a data e hora que o pedido foi criado

    compAddProd(cpf=cpf)#chamada da função que mostra o menu dos produtos e adiciona pedido

    while True: #estrutura de repetição que pergunta ao usuário se ele deseja adicionar outros produtos ou deseja voltar ao menu principal
        
        continuar = int(input("""
        +---------------------------------+
        | Deseja adicionar outro produto? |
        +---------------------------------+
        | 0 - Não                         |
        +---------------------------------+
        | 1 - Sim                         |
        +---------------------------------+
        """))
        
        if continuar == 1:
            compAddProd(cpf=cpf)
            continue
        elif continuar == 0:
            break
        else:
            print("Digite um opção válida.")
            continue
from VALORDOPEDIDO import * #importação de funções através dos módulos
from VERIFICARCPFSENHA import *

def extratodoPedido():
    while True:    
        cpf = str(input("CPF:"))#usuario fornece cpf
        senha = str(input("SENHA:"))#usuario fornece senha

        if verificar(cpf=cpf, senha=senha) == True:#condicional para verificar se o cpf e senha estao corretos
            with open("%s.txt"%cpf, "r") as extrato:#abre o arquivo do pedido do usuario para leitura
                with open("valor_%s.txt"%cpf, "r") as listavalores:#abre o arquivo com os valores dos produtos do usuario
                    a = listavalores.read()
                    a_lista = a.split("\n")#dividindo a lista pelos "\n"
                    tam = len(a_lista) #atribuindo uma variavel ao tamanho da lista
                    a_lista.pop(tam - 1)#retirando o ultimo indice da lista pois ele é ''
                    b = [float(i) for i in a_lista] #transformando todos os itens da lista em floats
                    valor = sum(b)#somando os valores da lista
                ex = extrato.readlines()
                ex[3] = "Total: R$ %.2f"%valor#print do valor total no momento da chamada da função
                with open("%s.txt"%cpf, "w") as ex_final:
                    ex_final.writelines(ex)
                with open("%s.txt"%cpf, "r") as printex:
                    c = printex.readlines()
                    cc = c[1:len(c)] #leitura do extrato sem exibir senha
                    print(*cc, sep="")
            break
        elif verificar(cpf=cpf, senha=senha) == False: #se os dados fornecidos pelo usuario estiverem incorretos:
            escolha = int(input("""
            Pedido não encontrado. Tente novamente ou volte ao menu principal.
            0 - Voltar ao menu.
            1 - Tentar novamente.
            """))#voltar ao menu ou tentar novamente
            if escolha == 1:
                continue
            elif escolha == 0:
                break
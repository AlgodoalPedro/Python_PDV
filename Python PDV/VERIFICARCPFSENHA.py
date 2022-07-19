import os #importação da biblioteca os

def verificar(cpf, senha):
	
    if os.path.exists("%s.txt"%cpf): #condicional para verificar se existe um pedido com esse CPF
        with open("%s.txt"%cpf, "r") as extrato:    #abrindo arquivo do extrato para leitura
            if senha+"\n" in extrato.readlines():   #verificando se a senha fornecida pelo usuário é a mesma que esta registrada no arquivo
                return True #se a senha e o cpf estiverem corretos retorna True
            else:
                return False #se estiver errado retorna False
    else: #se o arquivo nao existir retorna False
        return False
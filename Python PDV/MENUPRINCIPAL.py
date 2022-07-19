from NOVOPEDIDO import *  #importação de funções através dos módulos
from CANCELAPEDIDO import *
from INSERIRPODUTO import *
from CANCELARPRODUTO import *
from VALORDOPEDIDO import *
from EXTRATO import *

def menuprincipal():
    while True: #while utilizado para que o menu princial seja chamado chamado sempre que não
        escolha = input("""
        +-------------------------+
        |  1 - Novo Pedido        |
        +-------------------------+
        |  2 - Cancelar pedido    |
        +-------------------------+
        |  3 - Inserir Produto    |
        +-------------------------+
        |  4 - Cancelar Produto   |
        +-------------------------+
        |  5 - Valor do Pedido    |
        +-------------------------+
        |  6 - Extrato do Pedido  |
        +-------------------------+
                                 
        +-------------------------+
        |  0 - Sair               |
        +=------------------------+
        """)#input para escolha da opção do menu principal
        if escolha == "1":#opçao 1
            novoPedido()
        
        elif escolha == "2":#opçao 2
            cancelarPedido()
        
        elif escolha == "3":#opçao 3
            inserirProduto()
        
        elif escolha == "4":#opçao 4
            cancelarProduto()
        
        elif escolha == "5":#opçao 5
            valordoPedido()
        
        elif escolha == "6":#opçao 6
            extratodoPedido()
        
        elif escolha == "0":#opçao 0(termina o programa)
            break
        
        else:
            print("Digite um opção válida!") #else para caso o usuario digite um código diferente
            menuprincipal()

menuprincipal() #chamada da função principal para a execução do programa
def compAddProd(cpf):    #exibe a tabela e pede para o usuário um código
    np = int(input("""
    +--------+------------------+---------+
    | CÓDIGO |     PRODUTOS     |  PREÇO  |
    +--------+------------------+---------+
    |   1    | X-Salada         | R$10,00 |
    |   2    | X-Burger         | R$10,00 |
    |   3    | Cachorro Quente  | R$7,50  |
    |   4    | Misto Quente     | R$8,00  |
    |   5    | Salada de Frutas | R$5,50  |
    |   6    | Refrigerante     | R$4,50  |
    |   7    | Suco Natural     | R$6,25  |
    +--------+------------------+---------+
    
    +-------------------------------------+
    | Digite o código do produto desejado |
    +-------------------------------------+
    """))
    #solicita a quantidade de itens que o usuário deseja
    qntd = int(input("""
    +-----------------------+
    |  Digite a quantidade  |
    +-----------------------+
    """))
    
    tab_precos = [10,10,7.5,8,5.5,4.5,6.25] #lista com os valores de cada produto
    
    #lista com o nome dos produtos para formatação do extrato
    tab_produtos = ["X-Salada           -", "X-Burger           -", "Cachorro Quente    -", "Misto Quente       -", "Salada de Frutas   -", "Refrigerante       -", "Suco Natural       -"]
    
    #lista com o nome dos produtos para formatação do extrato
    tab_printpreco = ["10.00","10.00"," 7.50"," 8.00"," 5.50"," 4.50"," 6.25"]
    
    #preço que será usado no calculo do valor
    preco = tab_precos[np - 1]
    
    #valor total do produto
    valor = preco * qntd
    prod = tab_produtos[np - 1]
    f = float(valor) #transformando o valor em float

    with open("%s.txt"%cpf, "a") as extrato:
        extrato.write("%s  -  %s Preço unitário:  %s  Valor:  + %.2f\n"%(qntd, prod, tab_printpreco[np - 1], valor))#escrevendo os pedidos no extrato
    with open("valor_%s.txt"%cpf, "a") as listavalores: #escrevendo os valores dos produto no arquivo valor_(cpf do cliente)
        listavalores.write("%.2f\n"%f)
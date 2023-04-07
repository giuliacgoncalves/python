'''O programa a seguir simula um sistema de armazenamento de preços dos itens
de hortifrutis de um supermercado. Em que o usuário determina o número de itens
que serão cadastrados no armazém. Após finalizar o cadastro dos itens e dos seus
preços, o usuário poderá consultar o valor de uma quantidade de itens desejado
até que digite a palavra >Fim<'''

def cadastro(quantidade):
    '''A função cadastro serve para realizar o cadastro do itens do armazém'''
    lista = []
    i = 0
    while i<quantidade:
        nome = input()
        preco = float(input())
        if nome not in lista:
            lista.append(nome)
            lista.append(preco)
        else: #Se tentar cadastrar um produto com o mesmo nome o programa emite a msg:
            print("Produto ja cadastrado")
            i=i-1
        i = i+1
    return lista

def impressao(args):
    'A função impressao imprime o valor dos produto cadastrados que deseja consultar'
    nome = input()
    i = 0
    while nome != 'Fim':
        if nome not in args:#Se o nome do produto não estiver na lista o programa emite a mensagem:
            print('Produto nao cadastrado')
        else:
            i = args.index(nome) + 1
            print(args[i])
        nome = input()

listaCadastro = []
verifica = 0

#Abaixo o usuário deve inserir a quantidade de produtos que serão cadastrados:
n = int(input())

'''Abaixo chamamos a função que realiza o cadastro passando como parâmetro a
quantidade informada anteriormente'''
listaCadastro = cadastro(n)

'''Abaixo chamamos a função para verificar o preço dos hortifrutis até que o user
digite >Fim<, passando a lista de produtos cadastrados como parâmetro da função'''
verifica = impressao(listaCadastro)

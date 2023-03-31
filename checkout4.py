def cadastro(quantidade):
    lista = []
    i = 0
    while i<quantidade:
        nome = input()
        preco = float(input())
        if nome not in lista:
            lista.append(nome)
            lista.append(preco)
        else:
            print("Produto já cadastrado")
            i=i-1
        i = i+1
    return lista

def impressao(args):
    print(args)
    nome = input()
    precinho = []
    while nome != 'Fim':
        if nome not in args:
            print('Produto não cadastrado')
        else:
            print('funcionou')
        nome = input()

listaCadastro = []
verifica = 0

n = int(input())
listaCadastro = cadastro(n)
verifica = impressao(listaCadastro)

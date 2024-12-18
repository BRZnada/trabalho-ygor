from datetime import datetime
print('Bem vindo ao cadastro da epic games!!')
def ler_valor_nao_vazio(nome_variavel):
    valor_lido = input(f'Digite o/a {nome_variavel}: ')
    while valor_lido == '': 
        print(f'{nome_variavel} não pode ficar vazio!')
        valor_lido = input(f'Digite o/a {nome_variavel}:')
    return valor_lido

def confirmaSenha(senha):
    senha = input(f'Digite sua senha: ')
    while senha == '':
        print(f'Senha não pode ser vazio!')
        senha = input(f'Digite sua senha: ')
    confirmacaoSenha = input(f'Confirme sua senha: ')
    while confirmacaoSenha != senha:
        print("As senhas não coincidem!")
        confirmacaoSenha = input(f'Confirme sua senha: ')
    return senha



def cadastroEpicGames():
    nome = ler_valor_nao_vazio('nome')
    plataforma = ler_valor_nao_vazio('plataforma')
    senha = confirmaSenha('senha')
    email = ler_valor_nao_vazio('email')

    cadastro = {
        'nome': nome,
        'plataforma': plataforma,
        'senha': senha,
        'email': email
    }

    return cadastro

def imprimir_cadastro(cadastro):
    print(f"Nome:\t\t{cadastro['nome']}")
    print(f"Plataforma:\t{cadastro['plataforma']}")
    print(f"Email:\t\t{cadastro['email']}")
    print(f"senha:\t\t{cadastro['senha']}")

cadastro = cadastroEpicGames()

imprimir_cadastro(cadastro)

print("Cadastro feito com sucesso!!! YAY!!!")
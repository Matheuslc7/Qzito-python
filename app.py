import os

pedidos = ['Tayane' , 'Francisco' , 'Thayne']

def volta_menu():
    input('\n Pressione enter para retornar ao menu principal')
    main()

def exibir_nome():
    print('🆀 🆉 🅸 🆃 🅾   🅹 🅴 🅰  🅽 🆂\n')

def exibir_opcoes ():
    print('1. Criar pedido')
    print('2. Alterar status')
    print('3. Finalizar pedido')
    print('4. Pedidos Finalizados')
    print('5. Sair \n')

def finalizar_app():
    exibir_subtitulo('Finalizando o app.')
    
def opcao_invalida():
    print('Opção Inválida \n')
    volta_menu()

def exibir_subtitulo(texto):
    os.system('cls')
    print(texto)
    print()

def criar_pedido():
    exibir_subtitulo('Cadastrar cliente')
    nome_cliente = input ('Digite o nome do cliente : ')
    pedidos.append(nome_cliente)
    print(f'O Cliente {nome_cliente} foi cadastrado com sucesso \n')
    volta_menu()

def clientes_salvos():
    exibir_subtitulo('Clientes cadastrados')
    for cliente in pedidos:
        print(f'.{cliente}')
    volta_menu()


def escolher_opcoes():
    try:
        opcao_escolhida = int(input('Escolha uma opção : '))
        print(f'Você escolheu a opção {opcao_escolhida}')

        if opcao_escolhida == 1:
            criar_pedido()
        elif opcao_escolhida == 2:
            clientes_salvos()
        elif opcao_escolhida == 3:
            print('Finalizar pedido')
        elif opcao_escolhida == 4:
            print('Pedidos finalizados')
        elif opcao_escolhida == 5:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    os.system('cls')
    exibir_nome()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()
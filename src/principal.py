from utils import config
from utils.splash_screen import SplashScreen
from reports.relatorios import Relatorio
from controller.controller_livro import Controller_Livro
from controller.controller_usuario import Controller_Usuario
# from controller.controller_fornecedor import Controller_Fornecedor
# from controller.controller_pedido import Controller_Pedido
# from controller.controller_item_pedido import Controller_Item_Pedido

tela_inicial = SplashScreen()
relatorio = Relatorio()
ctrl_livro = Controller_Livro()
ctrl_usuario = Controller_Usuario()
# ctrl_fornecedor = Controller_Fornecedor()
# ctrl_pedido = Controller_Pedido()
# ctrl_item_pedido = Controller_Item_Pedido()

def reports(opcao_relatorio:int=0):

    if opcao_relatorio == 1:
        relatorio.get_relatorio_livros()
    if opcao_relatorio == 2:
        relatorio.get_relatorio_usuarios()

    # elif opcao_relatorio == 2:
    #     relatorio.get_relatorio_pedidos()
    # elif opcao_relatorio == 3:
    #     relatorio.get_relatorio_livros()
    # elif opcao_relatorio == 4:
    #     relatorio.get_relatorio_clientes()
    # elif opcao_relatorio == 5:
    #     relatorio.get_relatorio_fornecedores()
    # elif opcao_relatorio == 6:
    #     relatorio.get_relatorio_itens_pedidos()

    input("Pressione Enter para fechar o relatório")

def inserir(opcao_inserir:int=0):

    if opcao_inserir == 1:                               
        novo_livro = ctrl_livro.inserir_livro()
    elif opcao_inserir == 2:
        novo_cliente = ctrl_usuario.inserir_usuario()

    # elif opcao_inserir == 3:
    #     novo_fornecedor = ctrl_fornecedor.inserir_fornecedor()
    # elif opcao_inserir == 4:
    #     novo_pedido = ctrl_pedido.inserir_pedido()

def atualizar(opcao_atualizar:int=0):

    if opcao_atualizar == 1:
        relatorio.get_relatorio_livros()
        livro_atualizado = ctrl_livro.atualizar_livro()
    elif opcao_atualizar == 2:
        relatorio.get_relatorio_usuarios()
        usuario_atualizado = ctrl_usuario.atualizar_usuario()


    # elif opcao_atualizar == 2:
    #     relatorio.get_relatorio_clientes()
    #     cliente_atualizado = ctrl_cliente.atualizar_cliente()
    # elif opcao_atualizar == 3:
    #     relatorio.get_relatorio_fornecedores()
    #     fornecedor_atualizado = ctrl_fornecedor.atualizar_fornecedor()
    # elif opcao_atualizar == 4:
    #     relatorio.get_relatorio_pedidos()
    #     pedido_atualizado = ctrl_pedido.atualizar_pedido()
    # elif opcao_atualizar == 5:
    #     relatorio.get_relatorio_itens_pedidos()
    #     item_pedido_atualizado = ctrl_item_pedido.atualizar_item_pedido()

def excluir(opcao_excluir:int=0):

    if opcao_excluir == 1:
        relatorio.get_relatorio_livros()
        ctrl_livro.excluir_livro()
    elif opcao_excluir == 2:
        relatorio.get_relatorio_usuarios()
        ctrl_usuario.excluir_usuario()

    # elif opcao_excluir == 2:                
    #     relatorio.get_relatorio_clientes()
    #     ctrl_cliente.excluir_cliente()
    # elif opcao_excluir == 3:                
    #     relatorio.get_relatorio_fornecedores()
    #     ctrl_fornecedor.excluir_fornecedor()
    # elif opcao_excluir == 4:                
    #     relatorio.get_relatorio_pedidos()
    #     ctrl_pedido.excluir_pedido()
    # elif opcao_excluir == 5:
    #     relatorio.get_relatorio_itens_pedidos()
    #     ctrl_item_pedido.excluir_item_pedido()

def run():
    print(tela_inicial.get_updated_screen())
    config.clear_console()

    while True:
        print(config.MENU_PRINCIPAL)
        opcao = int(input("Escolha uma opção [1-5]: "))
        config.clear_console(1)
        
        if opcao == 1: # Relatórios
            
            print(config.MENU_RELATORIOS)
            opcao_relatorio = int(input("Escolha uma opção [0-6]: "))
            config.clear_console(1)

            reports(opcao_relatorio)

            config.clear_console(1)

        elif opcao == 2: # Inserir Novos Registros
            
            print(config.MENU_ENTIDADES)
            opcao_inserir = int(input("Escolha uma opção [1-4]: "))
            config.clear_console(1)

            inserir(opcao_inserir=opcao_inserir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 3: # Atualizar Registros

            print(config.MENU_ENTIDADES)
            opcao_atualizar = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            atualizar(opcao_atualizar=opcao_atualizar)

            config.clear_console()

        elif opcao == 4:

            print(config.MENU_ENTIDADES)
            opcao_excluir = int(input("Escolha uma opção [1-5]: "))
            config.clear_console(1)

            excluir(opcao_excluir=opcao_excluir)

            config.clear_console()
            print(tela_inicial.get_updated_screen())
            config.clear_console()

        elif opcao == 5:

            print(tela_inicial.get_updated_screen())
            config.clear_console()
            print("Obrigado por utilizar o nosso sistema.")
            exit(0)

        else:
            print("Opção incorreta.")
            exit(1)

if __name__ == "__main__":
    run()
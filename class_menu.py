from class_agenda import *

class Menu:
    def __init__(self):
        #Criar o objeto agenda -- Menu de navegação
        agenda = Agenda()

        while True: 
            entrada = input(' 1 - Novo Cadastro\n 2 - Listar Usuarios Cadastrados\n 3 - Sair\n')

            if entrada == '1':
                agenda.salvar_contato()

            elif entrada == '2':
                agenda.listar_contato()

            elif entrada == '3':
                print('Obrigado por usar nosso sistema')
                break
            else:
                print('Opção invalida!!!')
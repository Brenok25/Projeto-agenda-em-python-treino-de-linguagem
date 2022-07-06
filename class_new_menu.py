from class_db_agenda import *


class Menu:
    def __init__(self):
        agenda = DBAgenda()
    
        while True:
            entrada = input('Digite!\n'
                                 '1 - Salvar novo contato\n'
                                 '2 - Listar contatos\n'
                                 '3 - Alterar Nome\n'
                                 '4 - Alterar Telefone\n'
                                 '5 - Alterar E-mail\n'
                                 '6 - Excluir\n'
                                 '0 - Sair\n')


            if entrada == '1':
                cod = None
                nome = input('Entre com o Nome: ')
                telefone = input('Entre com o Telefone: ')
                email = input('Entre com o E-mail: ')
                agenda.salva_contato(cod, nome, telefone, email)

            elif entrada == '2':
                agenda.lista_contatos()

            elif entrada == '3':
                cod = int(input('Informe o código do contato: '))
                valor = input('Entre com o novo Nome: ')
                atributo = 'nome' # Atributo lá da tabela o nome do q vai ser mudado
                agenda.alterar_contato(atributo,cod, valor)
                
            elif entrada== '4':
                cod = int(input('Informe o código do contato: '))
                valor= input('Entre com o novo Telefone: ')
                atributo = 'telefone'
                agenda.alterar_contato(atributo, valor, cod)
            
            elif entrada== '5':
                cod = int(input('Informe o código do contato: '))
                valor= input('Entre com o novo email: ')
                atributo = 'email'
                agenda.alterar_contato(atributo, valor, cod)
            
            elif entrada == '6':
                cod = int(input('Informe o código do contato: '))
                agenda.delete_contato(cod)

            elif entrada == '0':
                break
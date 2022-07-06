from class_contato import *
class Agenda:
    def __init__(self): # Argumento é algop que um usuario pode alterar
        self.listaContatos = [] # Cria uma lista que realmente é uam lista kkk

    def salvar_contato(self):
        self.listaContatos.append(Contato())

    def listar_contato(self):
        for i in range(len(self.listaContatos)):
            print('\nCódigo: ',self.listaContatos[i].cod,
                '\nNome: ',self.listaContatos[i].nome,
                '\nTelefone:',self.listaContatos[i].tel,'\n') #Lista objetos = print(self.listaContatos[i]) mas se quer os atributos 

    
    def trocar_tel(self):
        resp = input('Digite o seu Id: ')

        for i in range(len(self.listaContatos)):
            if resp == self.listaContatos[i].cod:
                self.listaContatos[i].tel = input('Digite o novo telefone: ')

    def trocar_mome(self):
        resp = input('Digite o seu Id: ')

        for i in range(len(self.listaContatos)):
            if resp == self.listaContatos[i].cod:
                self.listaContatos[i].nome= input('Digite o novo Nome ')

    def exclui_contato(self, cod):
        for i in range(len(self.listaContatos)):
            if cod == self.listaContatos[i].cod:
                del self.listaContatos[i]
            else:
                print('Codigo de Contato não existe!')
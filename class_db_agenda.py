import mysql.connector
from class_contato import *


class DBAgenda:
    def __init__(self):
        self.conexao = mysql.connector.connect(
            host= '127.0.0.1',
            user= 'root',
            password= 'q1w2e3',
            database='Agenda'
        )
    
        self.my_cursor = self.conexao.cursor()



    def salva_contato(self, cod, nome, telefone, email): # Create
        obj_contato = Contato(cod, nome, telefone, email)
        sql = f'insert into Contatos (nome, telefone, email) value ("{obj_contato.nome}", "{obj_contato.tel}", "{obj_contato.email}")'
        # Values -- Mais de uma linha
        self.my_cursor.execute(sql) # Essas duas linhas servem para alterar o banco Create sempre vai ter 
        self.conexao.commit()

    
    def lista_contatos(self): # Read 
        sql = 'select * from Contatos'
        self.my_cursor.execute(sql)
        lista = self.my_cursor.fetchall()
        for i in lista:
            print(i)

    def alterar_contato(self, atributo, valor, cod):  # Update
        sql = f'update Contatos set {atributo} = "{valor}" where id = {cod}'
        self.my_cursor.execute(sql)
        self.conexao.commit()
    
    def delete_contato(self, cod): # Delete
        sql = f'delete from Contatos where id = {cod}'
        self.my_cursor.execute(sql)
        self.conexao.commit()
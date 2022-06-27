# class Nomeclass: # Cria uma nova classe contato - Usar maiscula 
#     def __init__(self, atributo1, atributo2, atributo3): # Cria objetos na classe contato / Innit constroi [ um objeto - metodo ( argumentos ) ]
#         self.cod = atributo1  # Cria os atributos d e contato -- self.code é um atributo do objeto
#         self.tel = atributo2
#         self.nome = atributo3
#         pass



class Contato: 
    def __init__(self): 
        # self.cod = cod  #input('Digite o seu Código') pode tbm
        # self.tel = tel
        # self.nome = nome

        self.cod = input('Digite o seu Código: ')  #input('Digite o seu Código') pode tbm
        self.nome = input('Digite o seu Nome: ') # Com input em baixo n coloca argumentos em cima 
        self.tel = input('Digite o seu Telefone: ')

        print('Cadastro realizado')

        
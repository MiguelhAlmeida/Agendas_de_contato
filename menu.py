from validacoes import validar_nome, validar_telefone
import os

class Menu:
    def __init__(self, agenda):
        self.agenda = agenda

    def exibir_menu(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            
            print("\n--- Menu ---")
            print("1. Adicionar contato")
            print("2. Remover contato")
            print("3. Ver lista de contatos")
            print("4. Sair")
            
            opcao = input("Escolha uma opção (1/2/3/4): ")
            
            if opcao == '1':
                self.adicionar_contato()
            elif opcao == '2':
                self.remover_contato()
            elif opcao == '3':
                self.listar_contatos()
            elif opcao == "4":
                print("Saindo...")
                break
            else:
                print("Opção inválida. Por favor, escolha uma opção válida.")
                
    def adicionar_contato(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        nome = self.validar_nome()
        telefone = self.validar_telefone()
        email = input("Insira seu email: ")
        
        self.agenda.adicionar_contato(nome, telefone, email)
        print(f"\nContato de {nome} adicionado com sucesso!")
        input("\nPressione Enter para continuar...")
        
    def remover_contato(self):
        os.system('cls' if os.name == 'nt' else 'clear')

        if not self.agenda.listar_contatos():
            print("Nenhum cliente encontrado.")
            input("\nPressione Enter para continuar...")
            return
        
        nome_remover = input("\nQual contato deseja remover? Insira o nome: ")
        
        if self.agenda.remover_contato(nome_remover):
            print(f"\nContato de {nome_remover} removido com sucesso!")
        else:
            print(f"\nContato de {nome_remover} não encontrado.")
        
        input("\nPressione Enter para continuar...")
        
    def listar_contatos(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nLista de contatos:")
        
        if not self.agenda.listar_contatos():
            print("Nenhum cliente encontrado.")
        else:
            for contato in self.agenda.listar_contatos():
                print(f"Nome: {contato['Nome']}, Telefone: {contato['Telefone']}, Email: {contato['Email']}")
        
        input("\nPressione Enter para continuar...")
    
    def validar_nome(self):
        while True:
            nome = input("Insira seu nome aqui: ")
            if validar_nome(nome):
                return nome
            else:
                print("Nome inválido. O nome deve conter apenas letras e espaços.")
    
    def validar_telefone(self):
        while True:
            telefone = input("Insira seu telefone (DD NNNN-NNNN): ")
            if validar_telefone(telefone):
                return telefone
            else:
                print("Telefone inválido. O formato deve ser: DD NNNN-NNNN.")

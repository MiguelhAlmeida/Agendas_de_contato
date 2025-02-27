class Agenda:
    def __init__(self):
        self.contatos = []
    
    def adicionar_contato(self, nome, telefone, email):
        contato = {
            "Nome": nome,
            "Telefone": telefone,
            "Email": email
        }
        self.contatos.append(contato)
        
    def listar_contatos(self):
        return self.contatos
        
    def adicionar_multiplos_contatos(self):
        while True:
            nome = input("Insira seu nome aqui: ")
            telefone = input("Insira seu telefone: ")
            email = input("Insira seu email: ")
            
            self.adicionar_contato(nome, telefone, email)
            print(f"Contato de {nome} adicionado com sucesso!")
            
            continuar = input("\nDeseja adicionar outro contato? (s/n): ")
            if continuar.lower() != 's':
                break
            
    def remover_contato(self, nome):
        for contato in self.contatos:
            if contato["Nome"].lower() == nome.lower():
                self.contatos.remove(contato)
                return True
        return False

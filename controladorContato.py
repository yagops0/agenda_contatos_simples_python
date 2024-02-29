from contato import Contato

lista_contatos = []

def existe_contato(codigo):
    for c in lista_contatos:
        if c.id == codigo:
            return True
    return False

def cadastrar_contatos(id, nome, telefone, email):
    novo_contato = Contato(id=id, nome=nome, telefone=telefone, email=email)
    
    if existe_contato(novo_contato.id):
        print("Não foi possível adicionar o contato pois ele já existe na agenda.")
        return 
    else:
        lista_contatos.append(novo_contato)
        print("Contato adicionado com sucesso!")
        return novo_contato
        
def editar_contato(id, nome, telefone, email):
    pass

def consultar_contato():
    pass

def pesquisar_contato():
    pass

def remover_contatos():
    pass

def listar_contatos():
    return lista_contatos
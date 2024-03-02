from contato import Contato

lista_contatos = []

def retornar_indice(codigo):
    for c in lista_contatos:
        if c.id == codigo:
            return lista_contatos.index(c)
    return -1
            
def existe_contato(codigo):
    for c in lista_contatos:
        if c.id == codigo:
            return True
    return False

def cadastrar_contatos(c : Contato):
    if existe_contato(c.id):
        print("Não foi possível adicionar o contato pois ele já está na agenda.")
        return False
    else:
        lista_contatos.append(c)
        print("Contato adicionado com sucesso!")
        return True
        
def editar_contatos(c):
    if existe_contato(c.id):
        lista_contatos[retornar_indice(c.id)] = c
        print("Contato alterado com sucesso!")
        return True
    else:
        print("Não foi possível alterar o contato o contato.")
        return False

def pesquisar_contatos(codigo):
    for c in lista_contatos:
        if existe_contato(codigo):
            if codigo == c.id:
                return c
    return 

def remover_contatos(c):
    if existe_contato(c.id):
        lista_contatos.remove(c)
        return True
    else:
        return False
    

def listar_contatos():
    return lista_contatos
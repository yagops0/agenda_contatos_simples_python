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
        
def editar_contato(c):
    for co in lista_contatos:
      if existe_contato(c.id):
          lista_contatos[retornar_indice(c.id)] = c
          print("Contato alterado com sucesso!")
          return True
    return False

def consultar_contato():
    pass

def pesquisar_contato():
    pass

def remover_contatos():
    pass

def listar_contatos():
    return lista_contatos
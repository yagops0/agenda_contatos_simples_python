from contato import Contato

lista_contatos : Contato = []

def existeContato(codigo):
    for c in lista_contatos:
        if codigo in lista_contatos.id:
            return True
        else:
            return False

def cadastrarContatos(id, nome, telefone, email):
    if existeContato(id):
        return
    else:
        novo_contato = Contato(id=id, nome=nome, telefone=telefone, email=email)
        
        lista_contatos.append(novo_contato)
        
        return novo_contato
        
def editarContato(id, nome, telefone, email):
    pass

def consultarContatos():
    pass

def pesquisarContato():
    pass

def removerContato():
    pass

def listarContato():
    pass
        
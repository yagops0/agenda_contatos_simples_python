from controlador_contato import (cadastrar_contatos, editar_contatos, listar_contatos, remover_contatos, pesquisar_contatos)
from contato import Contato
from time import sleep

#! ----------------------------------------------------------------------------
def linha():
    print("="*54)
    
def menu():
    print("======================= MENU =========================")
    linha()
    sleep(1)
    print("= 1 - Adicionar contato")
    linha()
    sleep(1)
    print("= 2 - Editar contato")
    linha()
    sleep(1)
    print("= 3 - Pesquisar contato")
    linha()
    sleep(1)
    print("= 4 - Remover contato")
    linha()
    sleep(1)
    print("= 5 - Listar contatos")
    linha()
    sleep(1)
    print("= 6 - Sair")
    linha()
    sleep(1)

#! ----------------------------------------------------------------------------  

continuar : str
escolha : int

linha()
print("================= AGENDA DE CONTATOS =================")
linha()
sleep(1)
try:
    while True:
        menu()
        sleep(1)
        escolha = int(input("Digite o que deseja fazer: "))
        linha()
        sleep(1)
        
        if escolha == 1:
            print("= Adicionar contatos")
            linha()
            sleep(1)
            while True:
                c = Contato(int(input("- Digite o id do contato: ")), 
                str(input("- Digite o nome do contato: ")), 
                str(input("- Digite o telefone do contato: ")),
                str(input("- Digite o email do contato: ")))
    
                
                cadastrar_contatos(c)
                
                continuar = str(input("Deseja cadastrar mais algum contato(S/N)? ").lower())
                
                if continuar == 'n':
                    break
                
        continuar = str(input("Deseja continuar usando o programa(S/N)?\n")).lower()
        linha()
        sleep(1)
        if continuar == 'n':
            break
        
    print("Obrigado por usar o programa!")
    linha()
    sleep(1)       
except:
    print("Ocorreu um erro.")































'''#! CADASTRAR CONTATOS
while True:
    c = Contato(int(input("Digite o id do contato: ")), 
                str(input("Digite o nome do contato: ")), 
                str(input("Digite o telefone do contato: ")),
                str(input("Digite o email do contato: ")))
    
    cadastrar_contatos(c)
    
    continuar = str(input("Deseja cadastrar mais algum contato(S/N)? ").lower())
    
    if continuar in 'Nn':
        break

for c in listar_contatos():
    print(c.id, c.nome, c.telefone, c.email) 
    print("="*40)
    

#! ALTERAR    
while True:
    id_alterar = int(input("Digite o id do contato que deseja alterar: "))
    
    for c in listar_contatos():
        if existe_contato(id_alterar):
            if c.id == id_alterar:
                print(f"O contato que deseja alterar é {c.nome}.")
                c.id = int(input("ID: "))
                c.nome = str(input("Nome: "))
                c.telefone = str(input("Tele: "))
                c.email = str(input("Email: "))
                
                editar_contato(c)
        
    continuar = str(input("Alterar mais algum contato(S/N)? ")).lower()
    
    if continuar == "n":
        break    
        
#! CONSULTAR CONTATOS
while True:
    id_pesquisar = int(input("Digite o id do contato que deseja pesquisar: "))
    for c in listar_contatos():
        print(pesquisar_contato(id_pesquisar).id)
        print(pesquisar_contato(id_pesquisar).nome)
        print(pesquisar_contato(id_pesquisar).telefone)
        print(pesquisar_contato(id_pesquisar).email)
        break
    break
        
while True:
    id_remover = int(input("Digite o id do contato que deseja remover: "))
    for c in listar_contatos():
        if id_remover == c.id:
            if remover_contatos(c):
                print("Contato removido com sucesso!")
                break        
    break

for c in listar_contatos():
    print(c.id, c.nome, c.telefone, c.email) 
    print("="*40)
    
print(listar_contatos())
cod = int(input("Digite o id do contato: "))

print(retornar_indice(cod))
'''
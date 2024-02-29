from controlador_contato import cadastrar_contatos, listar_contatos, retornar_indice, existe_contato
from contato import Contato

lista = []

continuar = ''

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
    if existe_contato(c.id):
        
    
print(listar_contatos())
cod = int(input("Digite o id do contato: "))

print(retornar_indice(cod))

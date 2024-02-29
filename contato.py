from dataclasses import dataclass

@dataclass
class Contato:
    id : int
    nome : str
    telefone : str
    email : str
    
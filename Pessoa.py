from datetime import date
class Endereco:
    def __init__(self, logradouro="", numero="", endereco_comercial=False):
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_comercial = endereco_comercial

class pessoa:
    def __init__(self, nome="", rendimento=0.0, endereco=None):
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento
    
    
class PessoaFisica(pessoa):
    def _init_(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:

            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()
        super().__init__(nome, rendimento, endereco)

        self.cpf = cpf
        self.dataNascimento = dataNascimento

def calcular_imposto(self, rendimento: float) -> float:

    if rendimento <= 1500:
        return 0
    elif 1500 < rendimento <= 3500:
        return (rendimento / 100) * 2
    elif 3500 < rendimento <= 6000:
        return (rendimento / 100) * 3.5 
    else:
        return rendimento * 5
    
class PessoaJuridica(pessoa):
    pass
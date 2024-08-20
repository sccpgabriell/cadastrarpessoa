from Pessoa import PessoaFisica, Endereco       
from datetime import date, datetime


def main():
    lista_pf = []

    while True:
        opcao=int(input("Escolha uma opcao: 1 - Pessoa Fisica / 2 - Pessoa Juridica / 0 - Sair"))
        if opcao == 1:
            while True:
                opcao_pf = int(input("Escolha uma opcao: 1 - Cadastrar Pessoa Fisica / 2 - Listar Pessoa Fisica / 3 - Voltar ao menu anterior"))

                if opcao_pf == 1:
                    novapf = PessoaFisica()
                    novo_end_pf = Endereco()

                    novapf.nome = input("Digite o nome da pessoa fisica")
                    novapf.cpf = input("Digite o CPF")
                    novapf.rendimento = float(input("Digite o rendimento mensal (Digite somente numeros):"))

                    data_nascimento = input(("Digite a data de nascimento (dd/mm/aaaa):"))
                    novapf.dataNascimento = datetime.strptime(data_nascimento, '%d/%m/%Y').date()
                    idade = (date.today() - novapf.dataNascimento).days // 365

                    if idade >= 18:
                        print("A pessoa tem mais de 18 anos")
                    else:
                        print("A pessoa tem menos de 18 anos. Retorne ao menu...")
                        continue 

                    novo_end_pf.lograudoro = input("Digite o logradouro: ")
                    novo_end_pf.numero = input("Digite o numero: ")
                    end_comercial = input("Este endereco é comercial? S/N")
                    novo_end_pf.endereco_Comercial = end_comercial.strip().upper() == "S"

                    novapf.endereco = novo_end_pf

                    lista_pf.append(novapf)

                    print("Cadastro realizado com sucesso!!")

                elif opcao_pf == 2:
                    if lista_pf:
                        for cada_pf in lista_pf:
                            print(f"Nome: {cada_pf.nome}")
                            print(f"Nome: {cada_pf.cpf}")
                            print(f"Endereco: {cada_pf.endereco.logradouro}, {cada_pf.endereco.numero}")
                            print(f"Data Nascimento: {cada_pf.data_nascimento.strftime("%d/%m/%Y")}")
                            print(f"Imposto a ser pago: {cada_pf.calcular_imposto(cada_pf.rendimento)}")
                            print("Digite 0 para sair")
                            input()

                    else:
                        print("Lista Vazia")
                elif opcao_pf == 0:
                    print("Voltando ao menu anterior")
                    break
                else:
                    print("opcao invalida, por favor digite uma das opcoes indicadas")
        elif opcao == 2:
            print("Funcionalidade para pessoa juridicas nao implementadas")
            pass
        elif opcao == 0:
            print("Obrigado por utilizar nosso sistema valeu")
            break
        else:
            print("Opcao invalida, por favor digite uma das opcoes validas")
if __name__ == "__main__":
    main()
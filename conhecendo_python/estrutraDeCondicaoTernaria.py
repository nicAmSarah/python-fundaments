saque = 100000
saldo = 20000

status = "Sucesso" if saque < saldo else "Falha"

print(f"{status} ao realizar o saque")

series = int(input("Qual a melhor serie:\n [1]- the office\n [2]- how i met your mother\n [3]- modern family"))

verdade = "Você é uma boa pessoa" if series == 1 else "Não é boa pessoa"

print(f"{verdade}")

opcao = int(input("Você é uma boa pessoa?\n[1]-Sim, sou uma boa pessoa\n[2]-Não, Não sou uma boa pessoa\n"))

series = int(input("Qual a melhor serie:\n [1]- the office\n [2]- how i met your mother\n [3]- modern family"))

if opcao == 1:
    if series == 1:
        print("Boa pessoa")
    elif series == 2:
        print("Dá pro gasto") 
    elif series == 3:
        print("Total Má pessoa")
    else:
        print("opção não valida")
elif opcao == 2:
    print("Má pessoa")
else:
    print("opção não valida")


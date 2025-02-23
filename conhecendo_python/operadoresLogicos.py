saque = 700
limite = 500
saldo = 1000

print(saldo >= saque and saque >= limite)
print(saldo <= saque and limite >= saque )

print(not(saque <= saldo)) #falso
print(not(limite >= saque)) #true

print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False) #Caso tenha uma verdadeira, ela é verdadeira
print(False or False)

print((saldo <= saque and limite <= saque) or (saldo >= saque and limite <= saque))#True
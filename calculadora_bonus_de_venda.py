nome = (input("Me informe o seu nome: "))
salario_fixo = float (input ("Me informe o seu salario fixo: "))
vendas = int(input("Me informe quantas vendas você fez: "))
comissao = salario_fixo* 0.30
salario_recebido = salario_fixo+comissao
if vendas >=20:
    print(f"Seu salario é R${salario_recebido}, Parabéns camarada! ‼️🤑💰")
else:
    print(f"Você não bateu a meta dessa vez seu salario é {salario_fixo}!😔😢")
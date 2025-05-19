print(" 😄😄​​​Seja bem vindo 😄😄  ")
print(" 🚙🚙🚙  ​​​Esse programa soma o aluguel do veiculos  🚙🚙🚙")

preco_dia = 90.00
preco_km = 0.20
dias = int(input("Quantos dias o carro foi alugado? "))
kms = float(input("Quantos KMs foram percorridos? "))
custo_dias = dias * preco_dia
custo_kms = kms * preco_km
total = custo_dias + custo_kms
print("===== RECIBO DE ALUGUEL =====")
print(f"Dias alugados: {dias} dias x R${preco_dia} = R${custo_dias}")
print(f"KM rodados: {kms} km x R${preco_km} = R${custo_kms}")
print(f"TOTAL A PAGAR: R${total}")
print("==============================")
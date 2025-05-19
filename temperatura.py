temp=float(input("Me informe a temperatura: "))
print(" 1- Transformar a temperatura em Fahreinheit ")
print("2- Transformar a temperatura em Kelvin")
op1=int(input("Me informe sua escolha:"))
if op1==1:
    fah=(temp*9/5)+32
    print(f"A temperatura informada em Fahreinheit é {fah}")
if op1==2:
    kel= temp+273,15
    print(f"A temperatura informada em Kelvin é {kel}")
if op1>2:
    print("Opção invalida!!!")
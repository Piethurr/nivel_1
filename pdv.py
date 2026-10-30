listadecompras = []
descontos = []
Valorfinal = []
while True:
    print("\n===================================================")
    opcao1 = print("Digite (1) se deseja realizar uma compra")
    opcao2 = print("Digite (0) se deseja parar de realizar compras")
    print("===================================================")
    escolha = int(input("\nDigite a opcão de escolha: ")) 
    if escolha == 1:
        valordacompra = float(input("\nDigite o valor da compra: R$"))
        listadecompras.append(valordacompra)
        idade = int(input("Digite sua idade: "))
        if idade <= 0 or valordacompra <= 0:
            print("O valor digitado é inválido, tente novamente")
            continue
        else:
            if idade >= 65:
                desconto = valordacompra*0.2
                valorfinal = valordacompra - desconto #20% de desconto
            elif idade < 65:
                desconto = valordacompra*0
                valorfinal = valordacompra - desconto #0% de desconto
            if valorfinal > 100: 
                desconto = (valorfinal*0.1)
                valorfinal = valorfinal - desconto
                print(f"O valor com desconto aplicado foi R${valorfinal:.2f}")
            else:
                if desconto == valordacompra*0.2:
                    print(f"O valor com desconto aplicado foi R${valorfinal:.2f}")
                elif desconto == valordacompra*0:
                    print(f"O valor sem desconto foi R${valordacompra:.2f}")
            desconto_total = valordacompra - valorfinal
            descontos.append(desconto_total)
            Valorfinal.append(valorfinal)      
               
    
    elif escolha == 0:
        print("\n================RESUMO DO DIA=================")
        print(f"Quantidade de compras registradas: ",len(listadecompras))
        print(f"Total bruto do valor de compra sem desconto: ",sum(listadecompras))
        print(f"Total de descontos concedidos: ",sum(descontos))
        print(f"Total final do valor de compra com descontos: ",sum(Valorfinal))
        break
    else: 
        print("Digite uma opcão válida por favor...")
        continue
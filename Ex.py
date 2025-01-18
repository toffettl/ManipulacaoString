nome = input("Digite seu nome: ")
idade = input("Digite usa idade: ")

if nome and idade:
    nomeInvertido = nome[-1:-10:-1]
    tamanho = len(nome)
    primeiraLetra = nome[0]
    ultimaLetra = nome[-1]

    print(f"Seu nome é {nome}")

    print(f"Seu nome invertido é {nomeInvertido}")

    if " " in nome:
        print("Seu nome contém espaços!")
    else:
        print("Seu nome não contém espaços!")

    print(f"Seu nome tem {tamanho} letras")

    print(f"A primeira letra do seu nome é {primeiraLetra}")

    print(f"A última letra do seu nome é {ultimaLetra}")
else:
    print("Você deixou campos vazios!")

nome = input("Digite seu nome:")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media = (nota1 + nota2 + nota3) / 3
print(f"{nome}, sua média é {media}")
if media >= 6:
    print("Aprovada")
else:
    print("Reprovada")

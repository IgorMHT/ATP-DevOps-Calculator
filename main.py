from fastapi import FastAPI

app = FastAPI()

resultado = 0

@app.get("/")
async def root():
    print(" Bem vindo a calculadora")

print("Para começar, digite seu nome")

nome = input("Seu nome: ")

numero1 = int(input("Olá " + nome + ", digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("Agora selecione o tipo de conta")
print("Somar")
print("Subtrair")
tipoConta = input("Desejo ")

if tipoConta == "somar":
    print("O resultado da conta é ", numero1 + numero2)
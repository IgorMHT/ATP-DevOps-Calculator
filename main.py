from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    print(" Bem vindo a calculadora")

print("Para começar, digite seu nome")

nome = input("Seu nome: ")

print("Olá", nome, "agora selecione o tipo de conta")
print("Somar")
print("Subtrair")

tipoConta = input("Desejo ")
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/calcular")
async def calcular(nome: str, numero1: int, numero2: int, operacao: str):
    if operacao == "somar":
        resultado = numero1 + numero2
    elif operacao == "subtrair":
        resultado = numero1 - numero2
    else:
        return {"erro": "Operação não suportada"}

    return {"nome": nome, "resultado": resultado}

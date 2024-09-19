from src.main import *
from unittest.mock import patch

def test_root():
    result = root()
    yield result
    assert result == {"message": "Hello World"}

def test_calcular(nome: str, numero1: int, numero2: int, operacao: str):
    if operacao == "somar":
        resultado = numero1 + numero2
    elif operacao == "subtrair":
        resultado = numero1 - numero2
    else:
        return {"erro": "Operação não suportada"}
    result = calcular
    yield result
    assert calcular == result

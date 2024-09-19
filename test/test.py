from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_calcular(nome: str, numero1: int, numero2: int, operacao: str):
    if operacao == "somar":
        resultado = numero1 + numero2
    elif operacao == "subtrair":
        resultado = numero1 - numero2
    else:
        return {"erro": "Operação não suportada"}
    result = await calcular ()
    assert calcular == result

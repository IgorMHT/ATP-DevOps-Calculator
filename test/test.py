from src.main import *
from unittest.mock import patch

import pytest
import pytest_asyncio

@pytest.mark.asyncio
async def test_root():
    result = await root()
    assert result == {"message": "Hello World"}

@pytest.mark.asyncio
async def test_calcular():
    result = await calcular (10, 20, "somar")
    assert result == 30



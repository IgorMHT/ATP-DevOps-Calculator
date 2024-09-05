from fastapi import FastAPI

app = FastAPI()

resultado = 0

@app.get("/")
async def root():
    return {"message": "Hello World"}
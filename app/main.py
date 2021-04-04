from fastapi import FastAPI

from fastapi.responses import JSONResponse

app = FastAPI()


@app.get("/")
async def read_root():
    return {"message": "Hello World from my container"}

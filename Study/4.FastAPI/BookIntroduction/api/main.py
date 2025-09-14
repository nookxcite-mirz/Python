from fastapi import FastAPI

app = FastAPI(title="Book Introduction API", version="0.1.0")

@app.get("/")
async def read_root():
    return {"message": "Welcome to Book Introduction API v0.1.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy update"}

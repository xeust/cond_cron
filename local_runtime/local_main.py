from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def http():
    return "Hello, I'm running locally"

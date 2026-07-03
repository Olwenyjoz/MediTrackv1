from fastapi import FastAPI

app = FastAPI(title="MediTrack API")

@app.get("/")
def root():
    return {"message": "Welcome to MediTrack"}
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "This project is a FastAPI application deployed using Azure Web Apps for Containers. Each update to the app is packaged into a Docker image and pushed to Azure, where the container automatically runs the latest version."}

@app.get("/health")
def health_check():
    return {"status": "ok"}

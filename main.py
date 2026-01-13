from fastapi import FastAPI
from routes.quiz import router as quiz_router

app = FastAPI(title="AI Quiz Application")

app.include_router(quiz_router, prefix="/quiz")

@app.get("/")
def root():
    return {"message": "AI Quiz API is running "}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host='0.0.0.0',
        port=8000,
        reload=False,
    )
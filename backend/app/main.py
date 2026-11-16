from fastapi import FastAPI

app = FastAPI(
    title="DashboardStudents API",
    description="API for managing students and schedules",
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"message": "Welcome to DashboardStudents API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}

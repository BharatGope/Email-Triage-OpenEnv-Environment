from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Email Env Running"}


def main():
    """Entry point for OpenEnv"""
    uvicorn.run(app, host="127.0.0.1", port=7860)


if __name__ == "__main__":
    main()
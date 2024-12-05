import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run
from dotenv import load_dotenv

current_path = os.getcwd()
env_path = f"{current_path}/.env"
load_dotenv(dotenv_path=env_path)

def configure_cors(api: FastAPI):
    origins = [
        "http://localhost:3000",
    ]
    api.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )


def start_api():
    api = FastAPI()
    configure_cors(api)
    return api


app = start_api()


@app.get("/")
async def read_root():
    return "Welcome to the ESG V3 AI API"

@app.get("/get-user")
async def get_user():
    return {
        "name": "John Doe",
        "age": 30,
        "llm": os.getenv("OPENAI_LLM_MODEL_4O")
    }

if __name__ == "__main__":
    run(app, host="localhost", port=80)

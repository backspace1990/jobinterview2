from fastapi import FastAPI
from app.crud import create_questions
from app.schemas import CreateQuestionPayload, Item
import httpx

app = FastAPI(
    title="Python3 простой веб сервис Умита",
    )

JSERVICE_URL = "https://jservice.io/api/random"


@app.post('/question/')
async def create_question(payload:CreateQuestionPayload):
    # Sending GET request
    async with httpx.AsyncClient() as client:
        r = await client.get(url=JSERVICE_URL, params={"count": payload.questions_num})
    # Extracting data in JSON format
    lists = [Item(**item_dict) for item_dict in r.json()]
    for item in lists:
        create_questions(item)

    return 


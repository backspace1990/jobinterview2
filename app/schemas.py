from pydantic import BaseModel


class Item(BaseModel): #serializer
    id:int
    question:str
    answer:str
    created_at:str

    class Config:
        orm_mode=True


class CreateQuestionPayload(BaseModel):
    questions_num:int
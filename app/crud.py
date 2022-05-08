from app.database import SessionLocal
from app import models
from app.schemas import Item

db=SessionLocal()

def get_or_none_question(id: int):
    return db.query(models.ItemModel).filter(
        models.ItemModel.id==id
    ).first()

def create_questions(item: Item):
    db_item = get_or_none_question(item.id)
    if db_item is None:
        new_item=models.ItemModel(
        id=item.id,
        text_question=item.question,
        text_answer=item.answer,
        data_created_at_user=item.created_at,
        )
        db.add(new_item)    
        db.commit()
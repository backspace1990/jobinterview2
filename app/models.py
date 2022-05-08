from datetime import datetime
from app.database import Base
from sqlalchemy import String,Integer,Column,Date



class ItemModel(Base):
    __tablename__='questions'

    id=Column(Integer,primary_key=True)
    text_question = Column(String(350))
    text_answer = Column(String(100))
    data_created_at_user=Column(String(100))
    date = Column(Date, default=datetime.now)
    


    def __repr__(self):
        return f"<Item id={self.id} created_at={self.date}>"
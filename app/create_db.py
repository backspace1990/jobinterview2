from app.database import Base,engine
from app.models import ItemModel

print("Creating database ....")

Base.metadata.create_all(engine)
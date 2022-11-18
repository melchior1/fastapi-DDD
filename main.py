from fastapi import FastAPI

from app.infrastructure.db.database import engine
from app.infrastructure.db.user.user_models import Base
from app.infrastructure.user import user_command, user_query

app = FastAPI()
app.include_router(user_query.router)
app.include_router(user_command.router)

Base.metadata.create_all(engine)

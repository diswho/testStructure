from fastapi import FastAPI
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError

from app.db.session import SesEXT, engEXT, SesLOC, engLOC
from app.model.employee import HREmployee
from datetime import datetime
from app.api.api_v1.api import api_router
from app.core.config import settings

app = FastAPI()

app.include_router(api_router, prefix=settings.API_V1_STR)

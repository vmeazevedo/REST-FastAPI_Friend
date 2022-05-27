from sqlalchemy import null
from app.src.connection.db_connection import engine
from app.src.connection.db_connection import SessionLocal
from app.src.connection.db_connection import Base

def test_engine():
    response = engine
    assert response is not None or response is not null

def test_session_local():
    response = SessionLocal
    assert response is not None or response is not null

def test_base():
    response = Base
    assert response is not None or response is not null

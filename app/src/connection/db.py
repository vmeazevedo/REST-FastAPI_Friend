from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Definindo a conexão com o banco de dados
SQLALCHEMY_DATABASE_URL = "sqlite:///./database/friends_api.db"

# Criando a conexão com o banco de dados
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Criando o Sessionmaker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
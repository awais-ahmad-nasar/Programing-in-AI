from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///Library.db"
engine = create_engine(db_url)
Base = declarative_base()

class Book(Base):
    __tablename__ = "Book"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)

Base.metadata.create_all(engine)
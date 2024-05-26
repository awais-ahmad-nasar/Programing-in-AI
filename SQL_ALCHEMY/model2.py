from  sqlalchemy import Column, Integer, String, create_engine,ForeignKey
from sqlalchemy.orm import declarative_base

db_url = "sqlite:///biit_students.db"

engine = create_engine(db_url)

Base = declarative_base()


class Student(Base):
    __tablename__ = "student"

    id = Column(Integer,primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

class Course(Base):
    __tablename__ = "course"

    id = Column(Integer,primary_key=True)
    title = Column(String)
    credit_hour = Column(Integer)

class Enrollment(Base):
    __tablename__ = "enrollment"

    id = Column(Integer,primary_key=True)

    student_id = Column(Integer, ForeignKey('student.id'))
    course_id = Column(Integer, ForeignKey('course.id'))
    session = Column(String)

Base.metadata.create_all(engine)

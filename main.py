import datetime
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, DateTime, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# mysql engine
engine = create_engine('mysql://root:@localhost:3306/pythondb')

try:
    engine.connect()
    print('Connection successful')

except Exception as e:
    print(e)

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.datetime.now())

    def __str__(self):
        return f'{self.username}'
    
Session = sessionmaker(engine)
session = Session()

if __name__ == '__main__':
    print('Creating table')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

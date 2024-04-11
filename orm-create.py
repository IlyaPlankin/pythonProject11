from sqlalchemy import Table, Index, Integer, String, Column, Boolean, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint, create_engine,Text, DateTime
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db2")
session=Session(bind=engine)
base=declarative_base()

class User (base):
    __tablename__='telsprav'
    id=Column(Integer)
    username=Column(String(100), nullable=False)
    firstname= Column(String(100), nullable=False)
    secondname = Column(String(100), nullable=False)
    phone = Column(String(100), nullable=False)
    email = Column(String(100), nullable=False)


    __table_args__=(
        PrimaryKeyConstraint('id',name='telsprav_pk'),
        UniqueConstraint('username'),
        UniqueConstraint('email'),
        UniqueConstraint('phone')
    )

#base.metadata.create_all(engine)

u1=User()
u1.email='kmorozov@gmail.com'
u1.phone ='5955555555'
u1.username='kirill'
u1.firstname ='kirill'
u1.secondname = 'morozov'


u2=User()
u2.email='ivanovi@gmail.com'
u2.phone ='5455522222'
u2.username='ivani'
u2.firstname ='ivan'
u2.secondname = 'Ivanov'

#session.add (u1)
session.add_all([u1,u2])
session.commit()
from sqlalchemy import Table, Index, Integer, String, Column, Boolean, PrimaryKeyConstraint, UniqueConstraint, ForeignKeyConstraint, create_engine,Text, DateTime, Numeric
from sqlalchemy.orm import declarative_base, relationship, Session
from datetime import datetime
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db2")
session=Session(bind=engine)
base=declarative_base()

class Customer (base):
    __tablename__ = 'customers'
    id = Column(Integer,primary_key=True)
    #id_customer = Column(Integer, ForeignKey('customer.id'))
    first_name = Column(String(200), nullable=False)
    last_name = Column(String(200), nullable=False)
    username=Column(String(50), nullable=False)
    email = Column(String(200), nullable=False)
    create_on=Column(DateTime,default=datetime.now)
    update_on=Column(DateTime,default=datetime.now,onupdate=datetime.now)
    orders=relationship("Order")
#class vipcustomer (Customer):
    #__tablename__ = 'vipcustomers'
    #id_customer = relationship('customer.id', backref='vipcustomers')
    #vipstatus = Column(String(200), nullable=False)

class Item (base):
    __tablename__ = 'Items'
    id = Column(Integer,primary_key=True)
    name = Column(String(200), nullable=False)
    cost_price=Column(String(10,2), nullable=False)
    seling_price = Column(Numeric(10, 2), nullable=False)
    count=Column(Integer)


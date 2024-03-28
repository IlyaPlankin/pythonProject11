from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, ForeignKey, CheckConstraint, Boolean, DateTime, insert
from datetime import datetime

metadata = MetaData()
# engine = create_engine("mysql+pymysql://alch:123456@10.10.101.193:3306/mydb")
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db2")

telsprav = Table('telsprav', metadata,
                 Column('id', Integer(), primary_key=True),
                 Column('name', String(50), nullable=False, index=True),
                 Column('surname', String(50), nullable=True, index=True),
                 Column('phone', String(20), nullable=False),
                 Column('about', Text(), nullable=True),
                 Column('address', String(200), nullable=True)
                 )
ed = Table('extradata', metadata,
           Column('id', Integer(), primary_key=True),
           Column('client_id', Integer, ForeignKey('telsprav.id')),
           Column('age', Integer, nullable=False),
           Column('heigest', Integer, nullable=True),
           Column('country', String(50), nullable=False),
           Column('City', String(50), nullable=False),
           Column('businessman', Boolean, default=False),
           Column('created', DateTime, default=datetime.now),
           CheckConstraint('age > 18', name='age_check')
           )

connection = engine.connect()
metadata.create_all(engine)


ins = telsprav.insert().values(
    name = 'Kirill',
    surname = 'Morozov',
    phone = '8999999999',
    about ='prepod',
    address = 'Sovetskiy pr'
)
print(ins)
print(ins.compile())
connection.execute(ins)





connection.commit()

print(engine)
from sqlalchemy import create_engine
from table_structure import  metadata, telsprav, ed

engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db2")

connection=engine.connect()
# Выборка без фильтров
# sel1=telsprav.select()
# print(sel1.compile())
# result=connection.execute(sel1)
# #print(result.fetchall())
# print(result.fetchmany(3))


sel1=telsprav.select().where (telsprav.c.id<4)
print(sel1.compile())
result=connection.execute(sel1)
print(result.fetchmany(3))
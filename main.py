from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text
metadata= MetaData ()
engine = create_engine('postgresql+psycopg2://postgres:123456@10.10.101.193:5432/mydb')

telsprav = Table ('telsprav', metadata, Column ('id',Integer(), primary_key = True),
Column ('name', String (50), nullable=False, index = True),
Column ('surname', String (50), nullable=True, index = True),
Column ('phone',String (20), nullable=False),
Column ('about',Text(),nullable=True)
)

connection =engine.connect()
metadata.create_all(engine)
connection.commit()
print(engine)

from sqlalchemy import create_engine, insert

from table_structure import metadata, telsprav, ed
# engine = create_engine("mysql+pymysql://alch:123456@10.10.101.193:3306/mydb")
engine = create_engine("postgresql+psycopg2://postgres:123456@10.10.101.193:5432/db2")

connection = engine.connect()
metadata.create_all(engine)

# ins = telsprav.insert().values(
#     name = 'Kirill',
#     surname = 'Morozov',
#     phone = '8999999999',
#     about ='prepod',
#     address = 'Sovetskiy pr'
# )
# block_insert=insert(telsprav)
#
# result = connection.execute(block_insert,[
# {
#     "name" : 'Ivan',
#     "surname" : 'Ivanov',
#     "phone" : '54555552',
#     "about" : 'doktor',
#     "address" : 'Nevskiy'
#
# },
#
# {
#     "name" : 'Petr',
#     "surname" : 'Petrov',
#     "phone" : '5545562122',
#     "about" : 'voditel',
#     "address" : 'Sennaya sq'
#
# }
# ])
#
# items = [
# {
#     "name" : 'Oleg',
#     "surname" : 'Plankin',
#     "phone" : '4545546514',
#     "about" : 'strelok',
#     "address" : 'Prospekt prosveshenia'
# },
# {
#     "name" : 'Ilya',
#     "surname" : 'Plankin',
#     "phone" : '46456258588',
#     "about" : 'povar',
#     "address" : 'Kypchino'
# }
# ]
#
# result = connection.execute(block_insert,items)
#
#
# print(ins)
# print(ins.compile())
# connection.execute(ins)


connection.commit()

print(engine)

ed_block_insert=insert(ed)
ed_items = [{
        "client_id":3,
        "age":1000,
        "heigest":200,
        "country":"Romnia",
        "City":"Sigishoara",
        "businessman":True}]
result3=connection.execute(ed_block_insert, ed_items)
connection.commit()
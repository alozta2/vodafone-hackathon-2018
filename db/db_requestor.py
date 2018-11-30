from sqlalchemy import create_engine

engine = create_engine("*")
connection = engine.connect()

print(engine)

result = connection.execute('select 1 from dual')

for row in result:
	#print(row)
    print("count:", row[0])

import sqlalchemy as db

engine = db.create_engine('mysql://root:Ishar321.@localhost:3306/touchstone')
connection = engine.connect()
metadata = db.MetaData()
touchstone = db.Table('test_case',metadata,autoload_with= engine)

print(touchstone.columns.keys())  
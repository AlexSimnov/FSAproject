from sqlalchemy import Table, Column, Integer, String, MetaData

metadata = MetaData()


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('usename', String, nullable=False),
    Column('password', String, nullable=False)
)

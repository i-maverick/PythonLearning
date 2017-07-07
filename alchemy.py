from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

Base = declarative_base()


class Driver(Base):
    __tablename__ = 'driver'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False)
    birthday = Column(Date)
    country = Column(String)
    number = Column(Integer)

    def __init__(self, name, birthday, country, number):
        self.name = name
        self.birthday = birthday
        self.country = country
        self.number = number

    def __repr__(self):
        return '<Driver(name={0}, birthday={1}, country={2}, number={3})>'.format(
            self.name, self.birthday, self.country, self.number)


engine = create_engine('sqlite:///:memory:', echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

drivers = session.query(Driver)
if drivers.count() == 0:
    session.add_all([
        Driver('Lewis Hamilton', date(1985, 1, 7), 'Great Britain', 44),
        Driver('Daniel Ricciardo', date(1989, 7, 1), 'Australia', 3)
    ])
    session.commit()

for d in session.query(Driver).order_by(Driver.number):
    print '{:>2} {}'.format(d.number, d.name)

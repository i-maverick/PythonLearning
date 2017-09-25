from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Float, String, Date, Time, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import date

Base = declarative_base()


class Driver(Base):
    __tablename__ = 'drivers'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    birthday = Column(Date)
    country = Column(String)
    number = Column(Integer)


class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    full_name = Column(String)


class Season(Base):
    __tablename__ = 'seasons'

    id = Column(Integer, primary_key=True)
    driver_id = Column(Integer, ForeignKey('drivers.id'))
    team_id = Column(Integer, ForeignKey('teams.id'))
    year = Column(Integer)

engine = create_engine('sqlite://', echo=False)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

drivers = session.query(Driver)
if drivers.count() == 0:
    session.add_all([
        Driver(name='Lewis Hamilton', birthday=date(1985, 1, 7), country='Great Britain', number=44),
        Driver(name='Daniel Ricciardo', birthday=date(1989, 7, 1), country='Australia', number=3),
        Team(name='Mercedes', full_name='Mercedes'),
        Team(name='Red Bull', full_name='Red Bull Racing'),
    ])
    session.commit()

    lh = session.query(Driver).filter(Driver.name == 'Lewis Hamilton').one()
    dr = session.query(Driver).filter(Driver.name == 'Daniel Ricciardo').one()
    mc = session.query(Team).filter(Team.name == 'Mercedes').one()
    rb = session.query(Team).filter(Team.name == 'Red Bull').one()
    session.add(Season(driver_id=lh.id, team_id=mc.id))
    session.add(Season(driver_id=dr.id, team_id=rb.id))
    session.commit()

for d in session.query(Driver).order_by(Driver.number):
    print '{:>2} {}'.format(d.number, d.name)

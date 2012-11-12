from sqlalchemy import (
    Column,
    Integer,
    Text,
    ForeignKey,
    )

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    relationship,
    backref,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))
Base = declarative_base()

class MyModel(Base):
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True)
    value = Column(Integer)

    def __init__(self, name, value):
        self.name = name
        self.value = value


class Route(Base):
    __tablename__ = 'routes'
    route_id = Column(Integer, primary_key=True)
    route_number = Column(Integer)

    def __init__(self, route_number):
        self.route_number = route_number

class Stop(Base):
    __tablename__ = 'stops'
    stop_id = Column(Integer, primary_key=True)
    stop_number = Column(Integer)
    route_id = Column(Integer, ForeignKey("routes.route_id"))
    route = relationship('Route', backref=backref('routes', order_by=route_id))

    def __init__(self, stop_number, route_id):
        self.stop_number = stop_number
        self.route_id = route_id

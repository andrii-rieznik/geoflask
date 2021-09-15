from geoalchemy2 import Geography
from geoalchemy2.shape import to_shape
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Location(Base):
    __tablename__ = 'locations'

    id = Column(Integer(), primary_key=True, nullable=False)
    name = Column(String(), nullable=False)
    latlon = Column(Geography(
        geometry_type='POINT', srid=4326), nullable=False
    )
    elevation = Column(Float(), nullable=False)

    def __repr__(self):
        return "<Location(name='{}', latlon='{}', elevation={}"\
                .format(self.name, self.latlon, self.elevation)

    def to_dict(self):
        point = to_shape(self.latlon)

        return {
            "id": self.id,
            "name": self.name,
            "longitude": point.x,
            "latitude": point.y,
            "elevation": self.elevation,
        }

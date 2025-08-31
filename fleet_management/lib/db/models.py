from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class Vehicle(Base):
    __tablename__ = "vehicles"
    id = Column(Integer, primary_key=True)
    reg_no = Column(String, unique=True, nullable=False)
    make = Column(String, nullable=False)
    capacity_tons = Column(Float, nullable=False)
    trips = relationship("Trip", back_populates="vehicle", cascade="all,delete-orphan")
    fuel_logs = relationship("FuelLog", back_populates="vehicle", cascade="all,delete-orphan")
    maintenance_logs = relationship("MaintenanceLog", back_populates="vehicle", cascade="all,delete-orphan")

class Driver(Base):
    __tablename__ = "drivers"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    trips = relationship("Trip", back_populates="driver", cascade="all,delete-orphan")

class Route(Base):
    __tablename__ = "routes"
    id = Column(Integer, primary_key=True)
    origin = Column(String, nullable=False)
    destination = Column(String, nullable=False)
    distance_km = Column(Float, nullable=False)
    trips = relationship("Trip", back_populates="route", cascade="all,delete-orphan")

class Trip(Base):
    __tablename__ = "trips"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    driver_id = Column(Integer, ForeignKey("drivers.id"), nullable=False)
    route_id = Column(Integer, ForeignKey("routes.id"), nullable=False)
    cargo = Column(String, nullable=False)
    distance_km = Column(Float, nullable=False)
    revenue = Column(Float, nullable=False)
    vehicle = relationship("Vehicle", back_populates="trips")
    driver = relationship("Driver", back_populates="trips")
    route = relationship("Route", back_populates="trips")

class FuelLog(Base):
    __tablename__ = "fuel_logs"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    liters = Column(Float, nullable=False)
    unit_price = Column(Float, nullable=False)
    odometer_km = Column(Float, nullable=False)
    vehicle = relationship("Vehicle", back_populates="fuel_logs")

class MaintenanceLog(Base):
    __tablename__ = "maintenance_logs"
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"), nullable=False)
    description = Column(String, nullable=False)
    cost = Column(Float, nullable=False)
    vehicle = relationship("Vehicle", back_populates="maintenance_logs")

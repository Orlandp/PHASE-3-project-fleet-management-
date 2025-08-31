from .db import SessionLocal
from .db.models import Vehicle, Driver, Route, Trip, FuelLog, MaintenanceLog
s = SessionLocal()

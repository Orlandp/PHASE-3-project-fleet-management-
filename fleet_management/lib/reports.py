from sqlalchemy import func
from .db import SessionLocal
from .db.models import Trip, FuelLog, MaintenanceLog

def vehicle_profit(vehicle_id):
    s = SessionLocal()
    revenue = s.query(func.coalesce(func.sum(Trip.revenue), 0.0)).filter(Trip.vehicle_id==vehicle_id).scalar()
    fuel_cost = s.query(func.coalesce(func.sum(FuelLog.liters*FuelLog.unit_price), 0.0)).filter(FuelLog.vehicle_id==vehicle_id).scalar()
    maintenance_cost = s.query(func.coalesce(func.sum(MaintenanceLog.cost), 0.0)).filter(MaintenanceLog.vehicle_id==vehicle_id).scalar()
    s.close()
    return {"vehicle_id": vehicle_id, "revenue": float(revenue), "fuel_cost": float(fuel_cost), "maintenance_cost": float(maintenance_cost), "profit": float(revenue - fuel_cost - maintenance_cost)}

def vehicle_fuel_efficiency(vehicle_id):
    s = SessionLocal()
    distance = s.query(func.coalesce(func.sum(Trip.distance_km), 0.0)).filter(Trip.vehicle_id==vehicle_id).scalar()
    liters = s.query(func.coalesce(func.sum(FuelLog.liters), 0.0)).filter(FuelLog.vehicle_id==vehicle_id).scalar()
    s.close()
    km_per_l = float(distance) / float(liters) if liters else 0.0
    return {"vehicle_id": vehicle_id, "distance_km": float(distance), "liters": float(liters), "km_per_liter": km_per_l}

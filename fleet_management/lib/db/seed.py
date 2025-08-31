from datetime import date
from . import SessionLocal, Base, engine
from .models import Vehicle, Driver, Route, Trip, FuelLog, MaintenanceLog

def reset_and_seed():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    s = SessionLocal()
    v1 = Vehicle(reg_no="KDD123A", make="Isuzu FRR", capacity_tons=10.8)
    v2 = Vehicle(reg_no="KDE456B", make="Isuzu NQR", capacity_tons=5.0)
    d1 = Driver(name="Peter Maina", phone="0700000001")
    d2 = Driver(name="Jane Waweru", phone="0700000002")
    r1 = Route(origin="Nairobi", destination="Nakuru", distance_km=160.0)
    r2 = Route(origin="Nakuru", destination="Kisii", distance_km=180.0)
    t1 = Trip(date=date.today(), vehicle=v1, driver=d1, route=r1, cargo="Cement", distance_km=160.0, revenue=45000.0)
    t2 = Trip(date=date.today(), vehicle=v1, driver=d1, route=r2, cargo="Steel", distance_km=180.0, revenue=52000.0)
    f1 = FuelLog(date=date.today(), vehicle=v1, liters=83.0, unit_price=190.0, odometer_km=120000.0)
    m1 = MaintenanceLog(date=date.today(), vehicle=v1, description="Service A", cost=12000.0)
    s.add_all([v1, v2, d1, d2, r1, r2, t1, t2, f1, m1])
    s.commit()
    s.close()

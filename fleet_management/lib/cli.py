import argparse
from datetime import date
from .db import Base, engine, SessionLocal
from .db.models import Vehicle, Driver, Route, Trip, FuelLog, MaintenanceLog
from .db.seed import reset_and_seed
from .helpers import print_table, parse_float, parse_int
from .reports import vehicle_profit, vehicle_fuel_efficiency

def init_db():
    Base.metadata.create_all(bind=engine)

def cmd_add_vehicle(args):
    s = SessionLocal()
    v = Vehicle(reg_no=args.reg, make=args.make, capacity_tons=parse_float(args.capacity))
    s.add(v)
    s.commit()
    print(v.id, v.reg_no, v.make, v.capacity_tons)
    s.close()

def cmd_list_vehicles(args):
    s = SessionLocal()
    rows = [(v.id, v.reg_no, v.make, v.capacity_tons) for v in s.query(Vehicle).all()]
    s.close()
    print_table(rows, ["id","reg_no","make","capacity_tons"])

def cmd_add_driver(args):
    s = SessionLocal()
    d = Driver(name=args.name, phone=args.phone)
    s.add(d)
    s.commit()
    print(d.id, d.name, d.phone)
    s.close()

def cmd_list_drivers(args):
    s = SessionLocal()
    rows = [(d.id, d.name, d.phone) for d in s.query(Driver).all()]
    s.close()
    print_table(rows, ["id","name","phone"])

def cmd_add_route(args):
    s = SessionLocal()
    r = Route(origin=args.origin, destination=args.destination, distance_km=parse_float(args.distance))
    s.add(r)
    s.commit()
    print(r.id, r.origin, r.destination, r.distance_km)
    s.close()

def cmd_list_routes(args):
    s = SessionLocal()
    rows = [(r.id, r.origin, r.destination, r.distance_km) for r in s.query(Route).all()]
    s.close()
    print_table(rows, ["id","origin","destination","distance_km"])

def cmd_add_trip(args):
    s = SessionLocal()
    t = Trip(date=date.fromisoformat(args.date), vehicle_id=parse_int(args.vehicle_id), driver_id=parse_int(args.driver_id), route_id=parse_int(args.route_id), cargo=args.cargo, distance_km=parse_float(args.distance), revenue=parse_float(args.revenue))
    s.add(t)
    s.commit()
    print(t.id)
    s.close()

def cmd_list_trips(args):
    s = SessionLocal()
    q = s.query(Trip).all()
    rows = [(t.id, t.date.isoformat(), t.vehicle.reg_no, t.driver.name, t.route.origin, t.route.destination, t.cargo, t.distance_km, t.revenue) for t in q]
    s.close()
    print_table(rows, ["id","date","vehicle","driver","origin","destination","cargo","distance_km","revenue"])

def cmd_add_fuel(args):
    s = SessionLocal()
    f = FuelLog(date=date.fromisoformat(args.date), vehicle_id=parse_int(args.vehicle_id), liters=parse_float(args.liters), unit_price=parse_float(args.unit_price), odometer_km=parse_float(args.odometer))
    s.add(f)
    s.commit()
    print(f.id)
    s.close()

def cmd_list_fuel(args):
    s = SessionLocal()
    q = s.query(FuelLog).all()
    rows = [(f.id, f.date.isoformat(), f.vehicle.reg_no, f.liters, f.unit_price, f.odometer_km, f.liters*f.unit_price) for f in q]
    s.close()
    print_table(rows, ["id","date","vehicle","liters","unit_price","odometer_km","cost"])

def cmd_add_maintenance(args):
    s = SessionLocal()
    m = MaintenanceLog(date=date.fromisoformat(args.date), vehicle_id=parse_int(args.vehicle_id), description=args.description, cost=parse_float(args.cost))
    s.add(m)
    s.commit()
    print(m.id)
    s.close()

def cmd_list_maintenance(args):
    s = SessionLocal()
    q = s.query(MaintenanceLog).all()
    rows = [(m.id, m.date.isoformat(), m.vehicle.reg_no, m.description, m.cost) for m in q]
    s.close()
    print_table(rows, ["id","date","vehicle","description","cost"])

def cmd_report_profit(args):
    r = vehicle_profit(parse_int(args.vehicle_id))
    print_table([tuple(r.values())], list(r.keys()))

def cmd_report_eff(args):
    r = vehicle_fuel_efficiency(parse_int(args.vehicle_id))
    print_table([tuple(r.values())], list(r.keys()))

def cmd_init_db(args):
    init_db()
    print("ok")

def cmd_seed(args):
    reset_and_seed()
    print("ok")

def build_parser():
    p = argparse.ArgumentParser(prog="fleet")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("init-db")
    s.set_defaults(func=cmd_init_db)

    s = sub.add_parser("seed")
    s.set_defaults(func=cmd_seed)

    s = sub.add_parser("add-vehicle")
    s.add_argument("--reg", required=True)
    s.add_argument("--make", required=True)
    s.add_argument("--capacity", required=True)
    s.set_defaults(func=cmd_add_vehicle)

    s = sub.add_parser("list-vehicles")
    s.set_defaults(func=cmd_list_vehicles)

    s = sub.add_parser("add-driver")
    s.add_argument("--name", required=True)
    s.add_argument("--phone", required=True)
    s.set_defaults(func=cmd_add_driver)

    s = sub.add_parser("list-drivers")
    s.set_defaults(func=cmd_list_drivers)

    s = sub.add_parser("add-route")
    s.add_argument("--origin", required=True)
    s.add_argument("--destination", required=True)
    s.add_argument("--distance", required=True)
    s.set_defaults(func=cmd_add_route)

    s = sub.add_parser("list-routes")
    s.set_defaults(func=cmd_list_routes)

    s = sub.add_parser("add-trip")
    s.add_argument("--date", required=True)
    s.add_argument("--vehicle-id", required=True)
    s.add_argument("--driver-id", required=True)
    s.add_argument("--route-id", required=True)
    s.add_argument("--cargo", required=True)
    s.add_argument("--distance", required=True)
    s.add_argument("--revenue", required=True)
    s.set_defaults(func=cmd_add_trip)

    s = sub.add_parser("list-trips")
    s.set_defaults(func=cmd_list_trips)

    s = sub.add_parser("add-fuel")
    s.add_argument("--date", required=True)
    s.add_argument("--vehicle-id", required=True)
    s.add_argument("--liters", required=True)
    s.add_argument("--unit-price", required=True)
    s.add_argument("--odometer", required=True)
    s.set_defaults(func=cmd_add_fuel)

    s = sub.add_parser("list-fuel")
    s.set_defaults(func=cmd_list_fuel)

    s = sub.add_parser("add-maintenance")
    s.add_argument("--date", required=True)
    s.add_argument("--vehicle-id", required=True)
    s.add_argument("--description", required=True)
    s.add_argument("--cost", required=True)
    s.set_defaults(func=cmd_add_maintenance)

    s = sub.add_parser("list-maintenance")
    s.set_defaults(func=cmd_list_maintenance)

    s = sub.add_parser("report-profit")
    s.add_argument("--vehicle-id", required=True)
    s.set_defaults(func=cmd_report_profit)

    s = sub.add_parser("report-fuel-eff")
    s.add_argument("--vehicle-id", required=True)
    s.set_defaults(func=cmd_report_eff)

    return p

def main():
    p = build_parser()
    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

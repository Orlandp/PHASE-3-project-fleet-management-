PRAGMA foreign_keys = ON;
INSERT INTO vehicles (reg_no, make, capacity_tons) VALUES
('KDD123A','Isuzu FRR',10.8), ('KDE456B','Isuzu NQR',5.0);
INSERT INTO drivers (name, phone) VALUES
('Peter Maina','0700000001'), ('Jane Waweru','0700000002');
INSERT INTO routes (origin, destination, distance_km) VALUES
('Nairobi','Nakuru',160.0), ('Nakuru','Kisii',180.0);
INSERT INTO trips (date, vehicle_id, driver_id, route_id, cargo, distance_km, revenue) VALUES
(date('now'),1,1,1,'Cement',160.0,45000.0),
(date('now'),1,1,2,'Steel',180.0,52000.0);
INSERT INTO fuel_logs (date, vehicle_id, liters, unit_price, odometer_km) VALUES
(date('now'),1,83.0,190.0,120000.0);
INSERT INTO maintenance_logs (date, vehicle_id, description, cost) VALUES
(date('now'),1,'Service A',12000.0);

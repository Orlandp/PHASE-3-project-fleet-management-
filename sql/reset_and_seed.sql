PRAGMA foreign_keys = OFF;
DROP TABLE IF EXISTS maintenance_logs;
DROP TABLE IF EXISTS fuel_logs;
DROP TABLE IF EXISTS trips;
DROP TABLE IF EXISTS routes;
DROP TABLE IF EXISTS drivers;
DROP TABLE IF EXISTS vehicles;
PRAGMA foreign_keys = ON;

.read sql/schema.sql
.read sql/seed.sql


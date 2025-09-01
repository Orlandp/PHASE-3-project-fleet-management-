# Fleet Management
This is a Command line interface that is for managing and interacting with the transport fleet. The app helpsone to manage the vehicles drivers routes and trips.
it gives reports on every trip based on profit margins
The data is stored in the SQL LITE.

## Features
-Add and list **vehicles** (reg no, capacity, type of vehicle)
-Add and list **Drivers** (name,phone)
-Add and list **routes** (origin,destination,distance)
-Record and list **trips** (date, vehivle,driver, route,cargo, distance, revenue)
-Record and list **fuel logs** (date, litres, unit price, odometer )
-Record and list **maintaenance logs** (date, description, cost)

-Reports:
 **vehicle profit** = revenue-fuel-maintenance.
 **Fuel Effeciency** = km per litre per vehicle.

 ## Requirements
 -Python 3.8+ (3.12 works)
 - SQLALchemy
 - tabulate
 -SQLlite 3
 -pipenv

 ## Installion
 1. Clone the repository
     ```bash
   git clone https://github.com/your-username/fleet-manager-cli.git
   cd fleet-manager-cli
 2. Install Dependencies
   pipenv install
 3. Activate the virtual environment.
    pipenv shell.
 ## Usage
 1. Run the CLI
    To start the module 
    - use Pipenv run app or python -m (for the specific module.)
 2. Available commands
   The fleet management should be able to do these commands
   -add vehcles
   -show a list of vehicles
   -add drivers
   -show a list of drivers
   -add routes
   -show a list of routes
   -add trips
   -show a list of trips
   -add fuel
   -show a list of fuel trips
   -add maintenance
   -show a list of maintenance in each vehicle
   - REPORTS
   - show for each vehicle profit made
   - show for each vehcle each report on fuel.
## Database Schema

-The database consists of the following tables:

-vehicles: id, reg_no (unique), make, capacity_tons

-drivers: id, name, phone

-routes: id, origin, destination, distance_km

-trips: id, date, vehicle_id, driver_id, route_id, cargo, distance_km, revenue

-fuel_logs: id, date, vehicle_id, liters, unit_price, odometer_km

-maintenance_logs: id, date, vehicle_id, description, cost

## Relationships

-A Vehicle has many Trips, FuelLogs, and MaintenanceLogs.

-A Driver has many Trips.

-A Route has many Trips.

-A Trip belongs to one Vehicle, one Driver, and one Route.

## License 
The project is under a MIT License

## Acknowledgements 
-Inspired by real-world fleet operations and reporting workflows
-Built with tabulate (CLI) and SQL ALchemy. 






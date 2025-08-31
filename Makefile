DB ?= $(if $(FLEET_DB),$(FLEET_DB),Fleet.db)
SQL_DIR := sql

.PHONY: help db-schema db-seed db-reset db-rebuild db-open db-tables db-query cli-init cli-seed run

help:
	@echo "make db-schema          # apply schema.sql to $(DB)"
	@echo "make db-seed            # run seed.sql"
	@echo "make db-reset           # drop + recreate + seed (reset_and_seed.sql)"
	@echo "make db-rebuild         # alias for db-reset"
	@echo "make db-open            # open sqlite3 shell"
	@echo "make db-tables          # list tables"
	@echo "make db-query Q='SQL'   # run an ad-hoc query, prints table"
	@echo "make cli-init           # CLI: init-db"
	@echo "make cli-seed           # CLI: seed"
	@echo "make run ARGS='list-vehicles'  # CLI passthrough"

db-schema:
	sqlite3 $(DB) < $(SQL_DIR)/schema.sql

db-seed:
	sqlite3 $(DB) < $(SQL_DIR)/seed.sql

db-reset:
	sqlite3 $(DB) < $(SQL_DIR)/reset_and_seed.sql

db-rebuild: db-reset

db-open:
	sqlite3 $(DB)

db-tables:
	sqlite3 $(DB) '.tables'

db-query:
	@test '$(Q)' || (echo "Usage: make db-query Q=\"SELECT * FROM vehicles;\"" && exit 2)
	sqlite3 -header -column $(DB) "$(Q)"

cli-init:
	pipenv run app init-db

cli-seed:
	pipenv run app seed

run:
	@test '$(ARGS)' || (echo "Usage: make run ARGS=\"list-vehicles\"" && exit 2)
	pipenv run app $(ARGS)

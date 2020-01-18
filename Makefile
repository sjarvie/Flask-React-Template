

psql:
	psql -p 5432

create_db:
	cd backend && python manage.py db init && cd ../
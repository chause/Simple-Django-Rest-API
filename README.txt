MarvelAPI is a simple RESTful API built in a Django framework supported by a MongoDB database via djongo

- Source data -
    marvel_heroes.csv: 		Contains a list of heroes
    marvel_villains.csv: 	Contains a list of villains
    marvel_stats.csv: 		Contains stats for each hero and villain

- Installion requirements -
    Python 3.6.7
    Django 2.1.3
    djangorestframework 3.9.0
    MongoDB 3.4.4
    djongo 1.2.3
    pymongo 3.7.2

- Setting up -
    Create migrations:          python manage.py makemigrations
    Run migrations:             python manage.py migrate

- Running unit tests -
    Run the MongoDB service:    monogd
    Run tests:                  python manage.py test

- Importing data via CSV -
    Run the MongoDB service:    monogd
    Run the Django server:      python application/import_csv.py -m <MODEL> -f <FILENAME>

- Running the API -
    Run the MongoDB service:    monogd
    Run the server (port 8000): python manage.py runserver 8000

- Navigating the API -
    Get hero list:              127.0.0.1:8000/hero/
    Get specific hero:          127.0.0.1:8000/hero/<ID>
    Get specific hero stats:    127.0.0.1:8000/hero/<ID>/stats
    Get villain list:           127.0.0.1:8000/villain/
    Get specific villain:       127.0.0.1:8000/villain/<ID>
    Get specific villain stats: 127.0.0.1:8000/villain/<ID>/stats

- Troubleshooting -
    MongoDB permissioning:      sudo chmod -R 777 /data/db

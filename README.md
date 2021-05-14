# Young Innovations internship challenge 2021.

## How to Run on LocalHost:

First of all, clone the project from the [link](https://pip.pypa.io/en/stable/).
```bash
git clone https://aakas@bitbucket.org/aakas/yipl-intern-petroleum-report-web.git
```
Navigate to the folder
```bash
cd yipl-intern-petroleum-report-web
```

create a virtual environment with virtualenv
```bash
virtualenv  {envName}
```

Install the required packages and library listed in requirements.txt
```bash
pip install -r requirements.txt
```

Makemigrations, so that the script to create table with attributes in database can be created.
```bash
python manage.py makemigrations
```

Migrate, so that the above made script by django actually creates table in db.
```bash
python manage.py migrate
```

fetchdata is the command. It fetches the data from api endpoint and saves the relations to the table.
```bash
python manage.py fetchdata
```

And finally run server, and enter [http://localhost:8000](http://localhost:8000) or [http://127.0.0.1:8000](http://127.0.0.1:8000) on the browser url. 
#Note : the port can be changed as per client wish.
```bash
python manage.py runserver
```
# File Structure
    Auto-Crawler
    ├── .venv                           # Virtual envirnoment containing necessary python packages
    ├── AutoCrawlerWebsite              # Django Python package for project
    │   ├── __init__.py                 # Empty Python file telling interpreter that AutoCrawlerWebsite is a Python package
    │   ├── __pycache__
    │   │   ├── __init__.cpython-310.pyc
    │   │   └── settings.cpython-310.pyc
    │   ├── settings.py                 # Main configuration file for a Django project
    │   ├── urls.py                     # URL configurations for website
    │   ├── asgi.py    
    │   └── wsgi.py
    ├── cars                            # Defines the database structure
    │   ├── data                        # Location of stored data
    │   │   └── mysql-files
    │   ├── migrations                  # Records for all migrations recording changes in Django app
    │   │   └── __init__.py             # Empty Python file telling interpreter that cars is a Python package
    │   ├── templates                   # Contains HTML Display logic files of Auto Crawler website 
    │   │   ├── home.html               # Template for Homepage of Auto Crawler
    │   │   ├── search_results.html     # Template for Searchpage of Auto Crawler
    │   │   └── test.html               # File for testing html code of Auto Crawler
    │   ├── testing                     # Files/scripts used for testing search & Django functionalities
    │   │   ├── car.py                  # Testing reading a .csv file
    │   │   ├── import_csv_to_mysql.py  # Testing script to import .csv into mysql
    │   │   └── search.py               # Testing a search class
    │   ├── admin.py                    # File used to register and display models in Django admin panel
    │   ├── apps.py                     # Default configuration file for Django apps
    │   ├── forms.py                    # Contains functions to handle form fields in website
    │   ├── __init__.py                 # Empty Python file telling interpreter that cars is a Python package
    │   ├── models.py                   # Contains Car class and defines database structure
    │   ├── tests.py                    # Test Codes for Django app
    │   └── views.py                    # Connects models and templates togetherr and provides an interface for Django website
    ├── crawlers                        # contains crawler files
    │   ├── AutoTrader-Crawler.py       # Ver3 of Crawler; site:AutoTrader.com
    │   ├── Beautifulsoup2.py           # Ver1 of Crawler; site: cars.com
    │   └── Web-Crawler.py              # Ver2 of Crawler; site: cars.com
    ├── manage.py                       # Command-line utility for Django web app
    └── README.md                       # THIS FILE

# How to run the code

## To run the development server and see the django wepage:
1. Clone the repository
2. Open a terminal in the folder at the level where you can see manage.py
3. Run virtual environment with `.venv\Scripts\activate.bat`
6. Run `python manage.py runserver`
7. Open browser and navigate to `http://127.0.0.1:8000/` to view webpage
8. CNTRL + C to close server
9. To deactivate virtual environment enter `deacativate` into terminal

## To run Web-Crawler.py:
1. Open terminal and navigate to Auto-Crawler Directory
2. Install and import Beautifulsoup4 with `pip install beautifulsoup4`
2. Install and import Request lib with `pip install request`
3. Install Pandas with `pip install pandas`
4. Install openpyxl with `pip install openpyxl`
5. Run the code, `Web-Crawler.py`, there will be an excel .csv file created in the /cars/data directory 

## Connecting to MySQL Server:
1. In terminal, enter `pip install mysql`
2. Go to the bin folder under the base directory of your MySQL installation with `cd mysql/bin`
3. Open MySQL shell by issueing the following command: `mysql -u root -p`
    - If you have logged in using a temporary root password that was generated during the installation or initialization process, change your root password by typing the following statement at the prompt: `ALTER USER 'root'@'localhost' IDENTIFIED BY 'Autocrawler';`
4. Create database using SQL queries with `create database carlistings`
5. Exit MySQL shell with `quit`
6. Update the update the database section in settings.py with the correct database configuration
7. Allow Python project to connect to the MySQL server`pip install mysqlclient`
8. Create a migration for the 'cars' app that contains the car model that will be used for tables `manage.py makemigrations cars`
9. Run the migrate command and it will create the exiting tables in Django into the MySQL database `manage.py migrate cars`
10. A table called 'cars_car' should apear in the 'Carlist' Database
11. Load csv in database from MySQL shell:
LOAD DATA LOCAL INFILE 'C:/Users/schand2/Auto-Crawler/cars/data/Autotrader_page1.csv'
INTO TABLE carlist.cars_car FIELDS TERMINATED BY ','
ENCLOSED BY '"' LINES TERMINATED BY '\n';

# Errors:
- ERROR 3948 (42000): Loading local data is disabled; this must be enabled on both the client and server sides
    1. Check the local_infile is disabled or enable
            mysql> show global variables like 'local_infile';
        Set the global variables by using this command:
            mysql> SET GLOBAL local_infile=1;
            Query OK, 0 rows affected (0.00 sec)
    2. Quit current server:
            mysql> quit
            Bye
    3. Connect to the server with local-infile system variable :
            mysql --local-infile=1 -u root -pAutocrawler carlist



# Resources
- https://studygyaan.com/django/best-practice-to-structure-django-project-directories-and-files
- https://python.plainenglish.io/how-to-structure-your-django-project-a5d50333a644
- https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/
- https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html
- https://docs.djangoproject.com/en/4.1/topics/db/search/
- https://stackoverflow.com/questions/11429827/how-to-import-a-csv-file-into-mysql-workbench
- https://stackoverflow.com/questions/59993844/error-loading-local-data-is-disabled-this-must-be-enabled-on-both-the-client
- https://stackoverflow.com/questions/63361962/error-2068-hy000-load-data-local-infile-file-request-rejected-due-to-restrict
- https://stackoverflow.com/questions/1310166/how-to-import-an-excel-file-in-to-a-mysql-database
- https://python.plainenglish.io/comparison-of-methods-for-importing-bulk-csv-data-into-mysql-using-python-5890dbf57419
- https://bootsnipp.com/snippets/aMOOD
- https://docs.djangoproject.com/en/4.1/ref/models/querysets/
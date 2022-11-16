To run the development server and see the django wepage:
1. Clone the repository
2. Open a terminal in the folder at the level where you can see manage.py
3. Run virtual environment with `.venv\Scripts\activate.bat`
4. 
5. Run `python manage.py runserver`
6. Open browser and navigate to `http://127.0.0.1:8000/` to view webpage
7. CNTRL + C to close server
8. To deactivate virtual environment enter `deacativate` into terminal

To run Web-Crawler.py:
1. Open terminal and navigate to Auto-Crawler Directory
2. Install and import Beautifulsoup4 with `pip install beautifulsoup4`
2. Install and import Request lib with `pip install request`
3. Install Pandas with `pip install pandas`
4. Install openpyxl with `pip install openpyxl`
5. Run the code, `Web-Crawler.py`, there will be an excel .csv file created in the /cars/data directory 



Resources:
https://www.geeksforgeeks.org/how-to-integrate-mysql-database-with-django/
https://dev.mysql.com/doc/refman/8.0/en/creating-tables.html
https://docs.djangoproject.com/en/4.1/topics/db/search/
https://stackoverflow.com/questions/11429827/how-to-import-a-csv-file-into-mysql-workbench
https://stackoverflow.com/questions/59993844/error-loading-local-data-is-disabled-this-must-be-enabled-on-both-the-client
https://stackoverflow.com/questions/63361962/error-2068-hy000-load-data-local-infile-file-request-rejected-due-to-restrict
https://stackoverflow.com/questions/1310166/how-to-import-an-excel-file-in-to-a-mysql-database
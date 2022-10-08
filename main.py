import os
from dotenv import load_dotenv ## to use the .env file 
from sqlalchemy import create_engine
import pandas as pd 

load_dotenv('credentials.env')

##### Connecting to mySQL through PYTHON ##### 

MYSQL_HOSTNAME = os.getenv('MYSQL_HOSTNAME')
MYSQL_USER = os.getenv('MYSQL_USER')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD')
MYSQL_DATABASE = os.getenv('MYSQL_DATABASE')

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}/{MYSQL_DATABASE}'
db = create_engine(connection_string)

##### Loading in a random dataset into the mySQL server ##### 

query = 'select * from movies_dataset.Movies;'
df = pd.read_sql(query, con=db)
real_df = pd.read_csv('movies.csv')
real_df.to_sql('Movies', con=db, if_exists='replace')

##### Running a Test Query ##### 

## was not able to run due to when runnign line 30 it says unsupported character ''' 

## sql_query = """ SELECT * FROM Movies WHERE genres LIKE 'comedy%' """;
## results_comedy = pd.read_sql(sql_query, con=db)
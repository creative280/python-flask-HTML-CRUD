from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['MYSQL_USER']
password = os.environ['MYSQL_PASSWORD']
host = os.environ['MYSQL_HOST']
port = os.environ['MYSQL_PORT']
db = os.environ['MYSQL_DATABASE']


DATABASE_CONNECTION_URI = f'mysql://{user}:{password}@{host}/{db}'
print(DATABASE_CONNECTION_URI)
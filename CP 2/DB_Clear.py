import psycopg2
import psycopg2.extras
import urllib.parse
from psycopg2 import Error
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

from config import *

def connect_to_DB():
    urllib.parse.uses_netloc.append("postgres")
    url = urllib.parse.urlparse(databaseUrl)
    connection = psycopg2.connect(user=url.username,
                                  password=url.password,
                                  host=url.hostname,
                                  port=url.port,
                                  database=url.path[1:])
    return connection

try:
    connection = connect_to_DB()

    connection.autocommit = True
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE Company CASCADE""")
    cursor.execute("""DROP TABLE Manager CASCADE""")
    cursor.execute("""DROP TABLE Instructor CASCADE""")
    cursor.execute("""DROP TABLE Polygon CASCADE""")
    cursor.execute("""DROP TABLE Equipment CASCADE""")
    cursor.execute("""DROP TABLE Services CASCADE""")
    cursor.execute("""DROP TABLE Offer CASCADE""")
    print("Удаление произошло успешно!")

except (Exception, Error) as error:
    print("Ошибка при работе с PostgreSQL", error)

finally:
    if connection:
        cursor.close()
        connection.close()
        print("Соединение с PostgreSQL закрыто")
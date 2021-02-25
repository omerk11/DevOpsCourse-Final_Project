import os
import pymysql
from dotenv import load_dotenv
from pathlib import Path
from datetime import datetime

creation_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

""" Connection """

env_path = Path('/Users/omerk/PycharmProjects/Python/DevOpsCourse/Projects/Project1') / '.creds'
load_dotenv(dotenv_path=env_path)
db_table = os.environ['DB_NAME']
host = os.environ['HOST']
port = os.environ['PORT']
passwd = os.environ['DB_PASS']
user = os.environ['DB_USER']

conn = pymysql.connect(host='remotemysql.com',
                       port=3306,
                       user='Mmy2cCFQLM',
                       passwd='KDmN7fJmti',
                       db='Mmy2cCFQLM',
                       charset='utf8mb4',
                       cursorclass=pymysql.cursors.DictCursor)

# conn = pymysql.connect(host='remotemysql.com', port=3306, user='Mmy2cCFQLM', passwd='KDmN7fJmti',
#                            db='Mmy2cCFQLM', charset='utf8', cursorclass=pymysql.cursors.DictCursor)
conn.autocommit(True)


def add_username(user_name, user_id):
    try:
        conn.connect()
        cur = conn.cursor()
        cur.execute(f"INSERT INTO {db_table}.users VALUES (%s , %s ,%s )", (user_id, user_name,creation_date))
    except:
        print('Failed to connect!')
    finally:
        cur.close()
        conn.close()


def get_user_info(user_id):
    try:
        conn.connect()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {db_table}.users WHERE user_id = %s", user_id)
        for row in cur:
            name = row['user_name']
        return name
    except:
        print('Failed to connect!')
    finally:
        cur.close()
        conn.close()


def update_user_name(user_id, n_name):
    try:
        conn.connect()
        cur = conn.cursor()
        cur.execute(f"UPDATE {db_table}.users SET user_name = %s WHERE user_id =  %s", (n_name, user_id))
    except:
        print('Failed to connect!')
    finally:
        cur.close()
        conn.close()


def delete_user(user_id):
    try:
        conn.connect()
        cur = conn.cursor()
        cur.execute(f"DELETE FROM {db_table}.users WHERE user_id = %s", (user_id))
    except:
        print('Failed to connect!')
    finally:
        cur.close()
        conn.close()

def get_all_info():
    try:
        conn.connect()
        cur = conn.cursor()
        cur.execute(f"SELECT * FROM {db_table}.users")
        table = cur.fetchall()
        print(table)
    except:
        print('Failed to connect!')
    cur.close()
    conn.close()



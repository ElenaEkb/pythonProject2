import psycopg2

conn = psycopg2.connect(
    host='localhost',
    user='postgres',
    password='Ghfdlf1407$',
    database='diplom'
    )


def create_table_seen_person():
    """create table found_person"""
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS seen_person(
                id serial,
                id_vk varchar(50) PRIMARY KEY);"""
        )
def insert_data_seen_person(id_vk):
    """inserting data into the seen_users table"""
    with conn.cursor() as cursor:
        cursor.execute(
            f"""INSERT INTO seen_person (id_vk) 
           VALUES (%s)""",
            (id_vk,)
        )
def check():
    with conn.cursor() as cursor:
        cursor.execute(
            f"""SELECT sp.id_vk
            FROM seen_person AS sp;"""
        )
        return cursor.fetchall()


def delete_table_seen_person():
    """delete table seen_person by cascade"""
    with conn.cursor() as cursor:
        cursor.execute(
            """DROP TABLE  IF EXISTS seen_person CASCADE;"""
        )


def creating_database():
    delete_table_seen_person()
    create_table_seen_person()
    print("База данных создана!")

creating_database()

import psycopg2
from psycopg2 import sql, OperationalError

class Database:
    def __init__(self, database, user, password, host, port):
        self.database = database
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        
        try:
            self.connection = psycopg2.connect(
                database=self.database,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cursor = self.connection.cursor()
        except OperationalError as e:
            print(f"Error connecting to database: {e}")
            self.connection = None
            self.cursor = None

    def connect(self):
        return psycopg2.connect(
            database='Employee',
            user='postgres',
            password='123456',
            host='127.0.0.1',
            port='5432'
        )

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

    # Insert Function
    def insert(self, name, age, doj, email, gender, contact, address):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("INSERT INTO employees (name, age, doj, email, gender, contact, address) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                        (name, age, doj, email, gender, contact, address))
            conn.commit()

    # Fetch All Data from DB
    def fetch(self):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("SELECT * from employees")
            rows = cur.fetchall()
            # print(rows)
            return rows

    # Delete a Record in DB
    def delete(self, id):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute("DELETE FROM employees WHERE id = %s", (id,))
            conn.commit()

    # Update a Record in DB
    def update(self, id, name, age, doj, email, gender, contact, address):
        with self.connect() as conn:
            cur = conn.cursor()
            cur.execute(
                "update employees set name=%s, age=%s, doj=%s, email=%s, gender=%s, contact=%s, address=%s where id=%s",
                (name, age, doj, email, gender, contact, address, id))
            conn.commit()
    
    

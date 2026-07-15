import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv
load_dotenv()

DB_HOST = os.getenv("DB_HOST")
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
try:
    print("Connecting to AWS RDS MySQL Database...")
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )
    
    if connection.is_connected():
        cursor = connection.cursor()
        print(" Successfully connected to the database!")

        cursor.execute("DROP TABLE IF EXISTS Interns;")

        create_table_query = """
        CREATE TABLE Interns (
            InternID INT PRIMARY KEY,
            FirstName VARCHAR(50) NOT NULL,
            LastName VARCHAR(50) NOT NULL,
            Email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        cursor.execute(create_table_query)
        print(" Table 'Interns' created successfully with structural constraints.")

        insert_query = """
        INSERT INTO Interns (InternID, FirstName, LastName, Email) 
        VALUES (%s, %s, %s, %s);
        """
        dummy_records = [
            (101, 'Zulkifal', 'Shafiq', 'mzulkifal9@gmail.com'),
            (102, 'Alex', 'Mercer', 'alex.mercer@decodelabs.tech'),
            (103, 'Sarah', 'Connor', 'sarah.connor@example.com'),
            (104, 'John', 'Doe', 'john.doe@example.com')
        ]

        cursor.executemany(insert_query, dummy_records)
        connection.commit()
        print(f" Successfully inserted {cursor.rowcount} dummy records.")

        try:
            cursor.execute("INSERT INTO Interns (InternID, FirstName, LastName, Email) VALUES (105, 'Duplicate', 'User', 'mzulkifal9@gmail.com');")
            connection.commit()
        except Error as e:
            print(f"\nConstraint Test Successful! Blocked duplicate email entry: {e}")

        print("\n--- Verifying Data Persistence inside 'Interns' Table ---")
        cursor.execute("SELECT * FROM Interns;")
        records = cursor.fetchall()
        
        print(f"{'InternID':<10} | {'First Name':<12} | {'Last Name':<12} | {'Email Address':<30}")
        print("-" * 75)
        for row in records:
            print(f"{row[0]:<10} | {row[1]:<12} | {row[2]:<12} | {row[3]:<30}")

except Error as e:
    print(f"\n Error while connecting to or querying MySQL: {e}")
    print("Double-check your Endpoint, password, and that your AWS Security Group inbound rules allow your current IP address.")

finally:
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("\nDatabase connection closed securely.")
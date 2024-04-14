#!/usr/bin/python3
"""Script to lists all states from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

def list_states(username, password, database):
    # Connect to MySQL server
    conn = MySQLdb.connect(host="localhost",
                           user=username,
                           passwd=password,
                           db=database,
                           port=3306)

    # Create a cursor object to execute queries
    cur = conn.cursor()

    # Execute query to fetch states from database
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows
    states = cur.fetchall()

    # Display results
    for state in states:
        print(state)

    # Close cursor and connection
    cur.close()
    conn.close()

if __name__ == "__main__":
    # Get MySQL username, password, and database name from command line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call function to list states
    list_states(username, password, database)

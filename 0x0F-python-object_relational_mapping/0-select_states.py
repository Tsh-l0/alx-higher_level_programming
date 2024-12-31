#!/usr/bin/python3
import MySQLdb
import sys import argv

if __name__ == "__main__":

    # Get The 3 arguments
    u_name = sys.argv[1]
    u_password = sys.argv[2]
    u_dbname = sys.argv[3]

    # Connect to a MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         passwd=u_password, db=u_dbname)

    # Create a cursor
    db_cursor = db.cursor()

    # Execute query
    db_cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all results
    states = db_cursor.fetchall()

    # Use a loop to display results
    for state in states:
        print(state)

    # Close the cursor and connection
    db_cursor.close()
    db.close()

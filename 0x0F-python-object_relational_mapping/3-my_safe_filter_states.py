#!/usr/bin/python3
"""
Lists all the states from the database in ascending order
"""
import MySQLdb
import sys


def main():
    """
    A function to connect to the database and list states
    """
    u_name = sys.argv[1]
    u_passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=u_name,
                         passwd=u_passwd, db=db_name)

    # Create a cursor
    db_cursor = db.cursor()

    # Execute query
    qry = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    db_cursor.execute(qry, (state_name,))

    # Fetch all results
    states = db_cursor.fetchall()

    # Use a loop to display states
    for state in states:
        print(state)

    # Close cursor and connection
    db_cursor.close()
    db.close()


if __name__ == "__main__":
    main()

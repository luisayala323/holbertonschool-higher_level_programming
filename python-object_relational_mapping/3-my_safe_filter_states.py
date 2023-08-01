#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument (safe from MySQL injection)
"""
import MySQLdb
import sys


def filter_states_by_name(username, password, database_name, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database_name,
            port=3306
        )

        # Create a cursor object to interact with the database
        cursor = db.cursor()

        # Use parameterized query to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cursor.execute(query, (state_name,))

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        # If there is an error, print the error message
        print("Error:", e)

    finally:
        # Close the cursor and database connection
        cursor.close()
        db.close()


# Check if the script is run as the main module
if __name__ == "__main__":
    # if all 4 arguments are provided
    if len(sys.argv) != 5:
        # Print the usage message and exit with an error code of 1
        print("Usage: python script_name.py <username> <password> <db_name> <state_name>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Call function to display values in the states table
    filter_states_by_name(username, password, database_name, state_name)

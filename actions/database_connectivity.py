import psycopg2

def DataUpdate(user_name):
    """Inserts a new row into the rasa_slot table with the provided user_name.

    Args:
        user_name (str): The user name to be inserted.

    Returns:
        int: The number of rows inserted (should be 1 for successful insertion).

    Raises:
        psycopg2.OperationalError: If there's an issue connecting to the database.
    """

    try:
        # Establish a connection to the PostgreSQL database
        connection = psycopg2.connect(
            host="localhost",
            user="postgres",
            password="postgre",  # Assuming password is 'postgre'
            database="postgres",
            port=5432
        )

        # Create a cursor object to execute database operations
        cursor = connection.cursor()

        # Prepare the SQL statement with placeholder for user_name
        sql = "INSERT INTO rasa_slot (user_name) VALUES (%s)"

        # Create a tuple containing the user_name value
        val = (user_name,)

        # Execute the INSERT statement with the user_name value
        cursor.execute(sql, val)

        # Commit the changes to the database
        connection.commit()

        # Print the number of rows inserted (should be 1)
        print(cursor.rowcount, "record inserted")

    except psycopg2.OperationalError as err:
        print("Error connecting to PostgreSQL database:", err)
    finally:
        # Ensure proper connection closure (if established)
        if connection:
            cursor.close()
            connection.close()



